import linecache
import sys

count = 0

# Print lines
while True:
    count += 1
    # Get next line from file 
    line = linecache.getline(sys.argv[1], count)
    list = line.strip().split()
    if not line: # if line is empty, end of file is reached 
        break
    print("Line {} Sig: {}".format(count, list[1]))
    print("Line {} Pubkey: {}\n".format(count, list[2]))
