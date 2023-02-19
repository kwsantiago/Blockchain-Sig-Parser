#!/bin/bash

for FILENAME in *; 
do
    numLines=$(wc -l $FILENAME | awk '{print $1}')
    mv $FILENAME $FILENAME.$numLines;
done
