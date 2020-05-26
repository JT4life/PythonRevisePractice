inv = open("inv.txt", 'r')
eof = False
while eof == False:
    line = inv.readline()
    if line != '':
        if line != '\n':
            print(line)
    else:
        print("End of file")
        eof = True
        inv.close()