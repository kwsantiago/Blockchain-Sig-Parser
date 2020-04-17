#!/bin/bash

declare -i MIN=1 # All public keys displayed will have more than this value of signatures
declare -i MAX=10 # All public keys displayed will have less than this value of signatures

if [ ! -d "./Signatures/"  ] 
then
    mkdir ./Signatures/ # Create Signatures folder if it doesn't exist
fi

getPubKeysInRange(){
    python3 script.py $1 # execute the script with the first argument (.log file)
    # Sort public keys into a file sorted from highest(top) to lowest(bottom)
    sort pubKeys.log | uniq -c | sort -rn | awk -v MIN="$MIN" -v MAX="$MAX" '{if($1 >= MIN && $1 <= MAX){{print $2}}}' | sponge pubKeys.log
    # Parse signatures to only contain the public keys we're looking for 
    python3 script.py
    rm sigsParsed.log
    # Read each line of pubKeys.log and execute the script using each public key
    count=$(cat pubKeys.log | wc -l)
    while IFS= read -r line
    do
        let count-=1
        echo $count remaining...
        ./parseSigs.sh output.log $line
    done < pubKeys.log
    rm pubKeys.log output.log
}

outputSigs(){
    python3 script.py $1 $2 # execute the script with the first arg (.log file) and second arg (pubkey)
    numLines=$(cat signatures.log | wc -l)
    mv signatures.log ./Signatures/$2.$numLines
}

if [ $# == 1 ] # if only 1 argument
then
    echo What is the Minimum number of signatures a public key should have in order to be parsed?
    read MIN
    echo What is the Maximum number of signatures a public key should have in order to be parsed?
    read MAX
    getPubKeysInRange "$1"
elif [ $# == 2 ] # if 2 arguments
then
    outputSigs "$1" "$2"
else
    echo Error: Invalid input
fi
