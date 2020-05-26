try:
    fileRead = open("File1.txt", "r")
    fileWrite = open("File2.txt", "w+")
except IOError:
    print("Error occurred", "File1.txt")
else:
    i=1
    for line in fileRead:
        print(line.rstrip())
        fileWrite.write(line)
        i=i+1
finally:
    fileRead.close()
    fileWrite.close()