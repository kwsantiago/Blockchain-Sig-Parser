#!/bin/bash

biggest=0

for FILENAME in *; 
do
    numLines="${FILENAME##*.}" # Take number of lines from the filename which is the number after the '.'
    if [ $numLines -gt $biggest ]
    then
        let biggest=$numLines
    fi
done

echo The file with the biggest amount of lines has $biggest lines.
