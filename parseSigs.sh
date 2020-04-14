#!/bin/bash


if [ $# == 1 ] # if only 1 argument
then
    python3 script.py $1 # execute the script with the first argument (.log file)
    # now sort the public keys by how many signatures they have as desired
    sort output.log | uniq -c | sort -rn | awk '{if($1 >= 100 && $1 <= 200){{print $1, $2}}}' | tail -n 10
    #sort output.log | uniq -c | sort -rn | head -n 10 # OPTIONAL: print top 10 public keys with most sigs
    rm output.log
elif [ $# == 2 ] # if 2 arguments
then
    python3 script.py $1 $2 # execute the script with the first arg (.log file) and second arg (pubkey)
    numLines=$(cat signatures.log | wc -l)
    mv signatures.log signatures.$numLines
else
    echo Error: Invalid input
fi
