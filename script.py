import linecache

count = 0

while True: 
    count += 1
  
    # Get next line from file 
    line = linecache.getline('LTC-Hashes.log', count)

    # if line is empty 
    # end of file is reached 
    if not line: 
        break
    print("Line {}: {}".format(count, line.strip())) 
