#!/bin/bash
#sort -k 3,3 $1 | sponge $1 # sort filename by public key // May not be needed (Test accordingly)
awk -F\  '{print>"./"$3}' $1 # print sigs for each public key in files seperated by public keys.
