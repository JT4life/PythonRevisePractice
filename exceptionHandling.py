try:
    with open('stuff.txt', 'r') as f:
        fileData = f.read()
        print(fileData)
except:
    print('File I/O error')
else:
    print("Operation success!!!")
finally:
    f.close()