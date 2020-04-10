import linecache
import sys

# -- Remove duplicates lines --
pubkeys_seen = set() # lines already seen

count = 0

# Print lines
while True:
    count += 1
    # Get next line from file 
    line = linecache.getline(sys.argv[1], count)
    list = line.strip().split()
    if not line: # if line is empty, end of file is reached 
        break
    if list[2] not in pubkeys_seen:
        pubkeys_seen.add(list[2])
        continue
    elif list[2] in pubkeys_seen:
        print("Line {} Sig: {}".format(count, list[1]))
        print("Line {} Pubkey: {}\n".format(count, list[2]))
