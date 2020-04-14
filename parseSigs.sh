#!/bin/bash

declare -i numToDisplay=10 # This is the number of public keys to be displayed
declare -i MIN=1 # All public keys displayed will have more than this value of signatures
declare -i MAX=10 # All public keys displayed will have less than this value of signatures

if [ ! -d "./Signatures/"  ] 
then
    mkdir ./Signatures/ # Create Signatures folder if it doesn't exist
fi

getPubKeysInRange(){
    python3 script.py $1 # execute the script with the first argument (.log file)
    #sort output.log | uniq -c | sort -rn | head -n 10 # OPTIONAL: print top 10 public keys with most sigs
    # This prints the public keys into a file sorted from highest(top) to lowest(bottom)
    sort output.log | uniq -c | sort -rn | awk -v MIN="$MIN" -v MAX="$MAX" '{if($1 >= MIN && $1 <= MAX){{print $2}}}' > pubKeys.log
    # Read each line of pubKeys.log and execute the script using each public key
    while IFS= read -r line
    do
        ./parseSigs.sh $1 $line
    done < pubkeys.log
    rm output.log pubkeys.log
}

outputSigs(){
    python3 script.py $1 $2 # execute the script with the first arg (.log file) and second arg (pubkey)
    if [ ! -d "./Signatures/$2"  ] 
    then
        mkdir ./Signatures/$2 # Create Signatures folder if it doesn't exist
    fi
    numLines=$(cat signatures.log | wc -l)
    mv signatures.log ./Signatures/$2/signatures.$numLines
}

if [ $# == 1 ] # if only 1 argument
then
    getPubKeysInRange "$1"
elif [ $# == 2 ] # if 2 arguments
then
    outputSigs "$1" "$2"
else
    echo Error: Invalid input
fi
