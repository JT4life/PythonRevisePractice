# f = open('stuff.txt', 'w')
# while True:
#     s = input('Enter>>')
#     if not s:
#         break
#     f.write(s+ '\n')
# f.close()

# f = open('stuff.txt', 'r')
# files = f.read()
# print(files)
# f.close()

# f = open('stuff.txt', 'r')
# strList = f.readlines()
# for s in strList:
#     s = s.strip('\n')
#     print(s)
# f.close()

with open('stuff.txt', 'r') as f:
    fileData = f.read()
    print(fileData)