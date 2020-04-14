import linecache
import sys
import os.path
from os import path

# lineList[1] is the signature
# lineList[2] is the public key

def getLines_WithSig(lineNum):
    file = open("signatures.log", "w")
    print("\nGrabbing Signatures of Public Key: {}\n".format(sys.argv[2]))

    # Print lines
    while True:
        line = linecache.getline(sys.argv[1], lineNum) # Get next line from file 
        if not line: # if line is empty, end of file is reached 
            break
        lineList = line.strip().split() # strip '\n' and put each string into an element of an array
        if(lineList[2] == sys.argv[2]): # if line's pubkey and user's pubkey matches, print line to file
            file.write("{}".format(line))
        lineNum += 1

    file.close
    print("Success! Check signatures.log for your ouput.\n")

def getLines_NoSig(lineNum):
    pubkeys_seen = set() # public keys already seen

    file = open("output.log", "w")

    print("\nThe public keys with the amount of corresponding signatures:\n")
    # Print lines
    while True:
        line = linecache.getline(sys.argv[1], lineNum) # Get next line from file 
        if not line: # if line is empty, end of file is reached 
            break
        lineList = line.strip().split() # strip '\n' and put each string into an element of an array
        if lineList[2] not in pubkeys_seen: # if line's pubkey has not been seen
            pubkeys_seen.add(lineList[2]) # add it to pubkeys_seen
        elif lineList[2] in pubkeys_seen: # else if line's pubkey has been seen, print pubkey to file
            file.write("{}\n".format(lineList[2]))
        lineNum += 1

    file.close

def main():
    lineNum = 1
    if(path.isfile(sys.argv[1])): # is this a valid file?
        if(len(sys.argv) == 2):
            try:
                getLines_NoSig(lineNum)
            except:
                print("An error has occurred or input invalid.")
        elif(len(sys.argv) == 3):
            try:
                getLines_WithSig(lineNum)
            except:
                print("An error has occurred or input invalid.")
        else:
            print("Error: Invalid Input")
    else:
        print("Error: Invalid Input")
main()
