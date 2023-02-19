# Blockchain Signature Parser

This script is a tool I made for blockchain security research, specifically for analyzing digital signatures in the blockchain. It parses raw blockchain signatures and outputs the signatures corresponding to public keys. It is a useful tool for identifying potential issues in the blockchain and ensuring its overall security. The script sorts blockchain signatures by public key in the form of a seperate file of each public key corresponding to all its signatures and the amount of signatures in the filename.

## Usage
1. ```./sort_files.sh FILENAME``` to make files for all the signatures of each unique public key in FILENAME.
2. ```./changeFilenames.sh``` to count the lines of each file and add it to the end to make it easier for parsing.
3. ```./scriptParser.sh``` to parse all the signatures based on how much lines per folder. Remember to create the folder ```../Bins``` before starting.

The other scripts in this folder are only for ease of use for informational purposes.
