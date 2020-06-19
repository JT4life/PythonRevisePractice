def cube(n):
    return n**3

def simplifiedGenerator(n):
    generatedResults = []
    currentN = 1
    while currentN <= n:
        generatedResults.append(cube(currentN)) #first run cube=1^3 currentN=1, 2nd run cube=2^3 currentN=2
        currentN += 1 #currentN =2, 2nd run currentN =3
    return generatedResults

def generatorUsingYield(n):
    currentN = 1
    while currentN <= n:
        yield cube(currentN)
        currentN += 1

print("Using the simplified generator code, we start with x=(1..10) and for each of them, we generate x^3")
print(simplifiedGenerator(10))

# Now we use the generator code which uses yield
# After this, only the generator object will be returned
print("Result using the Generator function with Yield")
generatedValues = generatorUsingYield(10)

print("We will traverse through the values from the generator object")
# Now, we actually compute and display the values from the generator object
print([i for i in generatedValues])

#List comprehension
#create list of nums
oList = range(1,11)
print("Original starting list of nums 1-10")
for x in oList:
    print(x)

#List comprehension to generate cubes
print("Displaying cubes by using list comprehension")
cubesUsingListComp = [cube(x) for x in oList]
print(cubesUsingListComp)

#This form is similar to the simple form of list comprehension, but
# it evaluates boolean-expression-involving-loop-variable for every item. It also
# only keeps those members for which the boolean expression is True.
listOfThreeMultiples = [x for x in range(10) if x % 3 == 0] # Multiples of 3 below 10

#This will step over every element in a sequence, successively setting
# the loop-variable equal to every element one at a time. It will then
# build up a list by evaluating the expression-involving-loop-variable
# for each one. This eliminates the need to use lambda forms and generally
# produces a much more readable code than using map() and a more
# compact code than using a for loop.
listOfNumbers = [ x for x in range(10) ] # List of integers from 0 to 9
print(listOfNumbers)