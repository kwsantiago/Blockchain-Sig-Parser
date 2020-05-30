#!/bin/bash
sort -k 3,3 test.log # sort filename by public key
awk -F\  '{print>"test/"$3}' test.log # print sigs for each public key in files seperated by public keys.
