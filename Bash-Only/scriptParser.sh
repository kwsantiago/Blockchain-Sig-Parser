#!/bin/bash

if [ ! -d "./1/"  ]
then
    mkdir ./1/
fi

count=0
end=103350

for FILENAME in *;
do
    numLines=$(wc -l $FILENAME | awk '{print $1}')
    let count+=$numLines
    sum=$(($count+$numLines))
    if [ $sum -le $end ]
    then
        mv $FILENAME ./1/
    fi
done
