#!/bin/bash

filenumber=1

if [ ! -d "../Bins/Bins-$filenumber"  ]
then
    mkdir ../Bins/Bins-$filenumber
fi

count=0
end=103350 # The purpose is to send the files in batches of 50 folders. The total num of lines divided by 50 gives 103,350. Change if needed.

for FILENAME in *;
do
    if [ $count -ge $end ] # Reset once num of lines exceeds $end
    then
        let filenumber+=1
        let count=0
        if [ ! -d "../Bins/Bins-$filenumber"  ]
        then
            mkdir ../Bins/Bins-$filenumber
        fi
        continue
    else
        numLines="${FILENAME##*.}" # Take number of lines from the filename which is the number after the '.'
        let count+=$numLines
        mv $FILENAME ../Bins/Bins-$filenumber
    fi
done
