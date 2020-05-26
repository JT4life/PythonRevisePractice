import random
random.randrange(4) #0-3
random.randrange(2,4) #2,3
random.randrange(1,10,2) #1,3,5,7,9

#start stop step

random.randint(2,4) #2,3,4 randint is inclusive

#random real numbers
n = random.random()

# n = random.uniform(start, stop)

# Exercise: Random Numbers
# What is the Python code to generate the following random numbers?
# Q1. 0, 1, 2, 3, 4, 5
random.randint(0,5)
# Q2. 3, 4, 5, 6
random.randint(3,6)
# Q3. 0, 3, 6, 9
a = random.randrange(0,10,3)
# print(a)
# Q4. 3, 5, 7, 9, 11
v = random.randrange(3,12,2)
# print(v)
# Q5. Float between 2 and 5?
oneTwo = random.randrange(2,6,3)
print(oneTwo)