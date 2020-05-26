# file1 = open("File1.txt", "w") #write
file1 = open("File1.txt", "a") #append
print("Opening mode:", file1.mode)
while True:
    data = input("Enter your data: ")
    if data =="":
        break
    file1.write(data+'\n')
file1.close()

