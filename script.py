import linecache
import sys

# line[1] is the signature
# line[2] is the public key

def getLines():
    # -- Remove duplicates lines --
    pubkeys_seen = set() # public keys already seen
    sigs_seen = set() # signatures already seen

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
        if lineList[1] not in sigs_seen: # if line's signature has not been seen
            sigs_seen.add(lineList[1]) # add it to sigs_seen
            continue
        elif lineList[2] in pubkeys_seen: # else if line's pubkey has been seen, print
#            print("Amount of sigs: {}".format(len(sigs_seen)))
            print("Line {} Sig: {}".format(lineNum, lineList[1]))
            print("Line {} Pubkey: {}\n".format(lineNum, lineList[2]))
            file.write("Line {} Sig: {}".format(lineNum, lineList[1]))
            file.write("Line {} Pubkey: {}\n".format(lineNum, lineList[2]))

    file.close

def main():
    getLines()

main()
