import linecache
import sys

# -- Remove duplicates lines --
lines_seen = set() # lines already seen

count = 0

# -- Print lines --
while True:
    count += 1
    # Get next line from file 
    line = linecache.getline('test.log', count)
    size = sys.getsizeof(line)
    # if line is empty 
    # end of file is reached 
    if not line:
        break
    if line not in lines_seen: # not a duplicate
        print("Line {}: {}\nSize: {}\n".format(count, line.strip(), size))
        lines_seen.add(line)
