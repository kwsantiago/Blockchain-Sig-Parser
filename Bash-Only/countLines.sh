#!/bin/bash

count=0

for FILENAME in *; 
do
    #numLines=$(wc -l $FILENAME | awk '{print $1}') # Use if naming convention is different
    numLines="${FILENAME##*.}" # Take number of lines from the filename which is the number after the '.'
    let count+=$numLines
done

echo The total number of lines in this folder is $count
