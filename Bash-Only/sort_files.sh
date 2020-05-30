#!/bin/bash
sort -k 3,3 filename # sort filename by public key
awk -F\  '{print>"02/"$3}' 02.log # print sigs for each public key in files seperated by public keys.
