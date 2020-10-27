## Bash Only
Sorting blockchain signatures by public key in the form of a seperate file of each public key corresponding to all its signatures and the amount of signatures in the filename.

## Usage
1. ```./sort_files.sh FILENAME``` to make files for all the signatures of each unique public key.
2. ```./changeFilenames.sh``` to count the lines of each file and add it to the end to make it easier for parsing.
3. ```./scriptParser.sh``` to parse all the signatures based on how much lines per folder. Remember to create the folder ```../Bins``` before starting.

The other scripts in this folder are only for ease of use for informational purposes.
