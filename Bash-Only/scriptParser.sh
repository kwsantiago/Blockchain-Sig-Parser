#!/bin/bash

filenumber=14

if [ ! -d "../Bins/Bins-$filenumber"  ]
then
    mkdir ../Bins/Bins-$filenumber
fi

count=0
end=103350

for FILENAME in *;
do
    if [ $count -ge $end ]
    then
        let filenumber+=1
        let count=0
        if [ ! -d "../Bins/Bins-$filenumber"  ]
        then
            mkdir ../Bins/Bins-$filenumber
        fi
        continue
    else
        numLines=$(wc -l $FILENAME | awk '{print $1}')
        let count+=$numLines
        mv $FILENAME ../Bins/Bins-$filenumber
    fi
done
