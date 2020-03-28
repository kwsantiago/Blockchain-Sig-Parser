import linecache
import sys

count = 0

while True: 
    count += 1
  
    # Get next line from file 
    line = linecache.getline('test.log', count)
    size = sys.getsizeof(line)
    # if line is empty 
    # end of file is reached 
    if not line: 
        break
    print("Line {}: {}\nSize: {}".format(count, line.strip(), size))
