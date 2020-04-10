import linecache
import sys

# line[1] is the signature
# line[2] is the public key

def getLines_WithSig():
    # -- Remove duplicates lines --
    pubkeys_seen = set() # public keys already seen

    lineNum = 0

    file = open("output_withSig.log", "w")
    file.write("Pubkey: {}\n\n".format(sys.argv[2]))
    print("Pubkey: {}\n\n".format(sys.argv[2]))

    # Print lines
    while True:
        lineNum += 1
        line = linecache.getline(sys.argv[1], lineNum) # Get next line from file 
        if not line: # if line is empty, end of file is reached 
            break
        lineList = line.strip().split() # strip '\n' and put each string into an element of an array
        if lineList[2] not in pubkeys_seen: # if line's pubkey has not been seen
            if(sys.argv[2] == lineList[2]): # if line's public key and user entered public key match
                pubkeys_seen.add(lineList[2]) # add it to pubkeys_seen
                continue
            else:
                continue
        elif lineList[2] in pubkeys_seen: # else if line's pubkey has been seen, print
            print("Line {} Sig: {}".format(lineNum, lineList[1]))
            file.write("Line {} Sig: {}\n".format(lineNum, lineList[1]))

    file.close

def getLines_NoSig():
    # -- Remove duplicates lines --
    pubkeys_seen = set() # public keys already seen

    lineNum = 0

    file = open("output.log", "w")

    # Print lines
    while True:
        lineNum += 1
        line = linecache.getline(sys.argv[1], lineNum) # Get next line from file 
        if not line: # if line is empty, end of file is reached 
            break
        lineList = line.strip().split() # strip '\n' and put each string into an element of an array
        if lineList[2] not in pubkeys_seen: # if line's pubkey has not been seen
            pubkeys_seen.add(lineList[2]) # add it to pubkeys_seen
            continue
        elif lineList[2] in pubkeys_seen: # else if line's pubkey has been seen, print
            print("Line {} Sig: {}".format(lineNum, lineList[1]))
            print("Line {} Pubkey: {}\n".format(lineNum, lineList[2]))
            file.write("Line {} Sig: {}\n".format(lineNum, lineList[1]))
            file.write("Line {} Pubkey: {}\n\n".format(lineNum, lineList[2]))

    file.close

def main():
    if(len(sys.argv) == 3):
        getLines_WithSig()
    else:
        getLines_NoSig()
main()
