import pickle

grades = {'A':89, 'B':72, 'C':87}

with open('grades.pkl', 'wb') as pickleFile:
    pickle.dump(grades, pickleFile)

with open('grades.pkl', 'rb') as pickleRead:
    newData = pickle.load(pickleRead)

