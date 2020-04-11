#!/bin/bash

if [ $# == 1 ] # if only 1 argument
then
    python3 script.py $1 # execute the script with the first argument (.log file)
    sort output.log | uniq -c | sort -rn | head -n 10 # print top 10 public keys with most sigs
    rm output.log
elif [ $# == 2 ] # if 2 arguments
then
    python3 script.py $1 $2 # execute the script with the first arg (.log file) and second arg (pubkey)
else
    echo Error: Invalid input
fi
