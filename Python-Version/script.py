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
    print("Success! Check the /Signatures/ folder for your ouput.\n")

def getLines_NoSig(lineNum):
    pubkeys_seen = set() # public keys already seen

    file = open("pubKeys.log", "w")
    sigsParsed = open("sigsParsed.log", "w")

    # Print lines
    while True:
        line = linecache.getline(sys.argv[1], lineNum) # Get next line from file 
        if not line: # if line is empty, end of file is reached 
            break
        lineList = line.strip().split() # strip '\n' and put each string into an element of an array
        if lineList[2] not in pubkeys_seen: # if line's pubkey has not been seen
            pubkeys_seen.add(lineList[2]) # add it to pubkeys_seen
        elif lineList[2] in pubkeys_seen: # else if line's pubkey has been seen, print pubkey to file
            sigsParsed.write("{}".format(line))
            file.write("{}\n".format(lineList[2]))
        lineNum += 1

    file.close
    sigsParsed.close

def parseSigs(lineNum): # this function parses the sigsParsed.log file for the public keys defined by the bash script
    pubkeys_seen = set() # public keys already seen

    file = open("pubKeys.log", "r")
    sigsParsed = open("output.log", "w")

    # Put desired public keys into set
    while True:
        lineKeys = linecache.getline("pubKeys.log", lineNum) # Get next line from file 
        if not lineKeys: # if line is empty, end of file is reached 
            break
        if lineKeys.strip() not in pubkeys_seen: # if line's pubkey has not been seen
            pubkeys_seen.add(lineKeys.strip()) # add it to pubkeys_seen
        lineNum += 1

    lineNum = 1 # reset counter
    # Print lines
    while True:
        line = linecache.getline("sigsParsed.log", lineNum) # Get next line from file 
        if not line: # if line is empty, end of file is reached 
            break
        lineList = line.strip().split() # strip '\n' and put each string into an element of an array
        if lineList[2] in pubkeys_seen: # if line's pubkey has been seen, print pubkey to file
            sigsParsed.write("{}".format(line))
        lineNum += 1

    file.close
    sigsParsed.close

def main():
    lineNum = 1
    if(len(sys.argv) == 1):
        try:
            parseSigs(lineNum)
        except:
            print("Parse Sigs: An error has occurred or input invalid.")
    elif(path.isfile(sys.argv[1])): # is this a valid file?
        if(len(sys.argv) == 2):
            try:
                getLines_NoSig(lineNum)
            except:
                print("No Sig: An error has occurred or input invalid.")
        elif(len(sys.argv) == 3):
            try:
                getLines_WithSig(lineNum)
            except:
                print("With Sig: An error has occurred or input invalid.")
        else:
            print("Error: Invalid Input")
    else:
        print("Error: Invalid Input")
main()
