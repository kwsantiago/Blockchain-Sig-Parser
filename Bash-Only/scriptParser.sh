#!/bin/bash

filenumber=1

if [ ! -d "../Bins/Bins-$filenumber"  ]
then
    mkdir ../Bins/Bins-$filenumber
fi

count=0
end=103350

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
        #numLines=$(wc -l $FILENAME | awk '{print $1}') # Use if naming convention is different
        numLines="${FILENAME##*.}" # Take number of lines from the filename which is the number after the '.'
        let count+=$numLines
        mv $FILENAME ../Bins/Bins-$filenumber
    fi
done
