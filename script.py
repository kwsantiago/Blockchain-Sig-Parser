import linecache
import sys

count = 0

# Print lines
while True:
    count += 1
    # Get next line from file 
    line = linecache.getline('LTC-Hashes.log', count)
    size = sys.getsizeof(line)
    if not line: # if line is empty, end of file is reached 
        break
    print("Line {}: {}\nSize: {}\n".format(count, line.strip(), size))
