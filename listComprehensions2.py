# List Comprehension
# [expression for value in collection]
# If you only want to include the expression for certain pieces of data you can add on an if clause after forloop
# [expression for value in collection if <test>] //the expression will be added only if the clause is True
# you can have more than 1 if clause [expression for val in collection if <test1> and <test2>] //added if both are True
# can loop over more than 1 collection [expr for val1 in col1 and val2 in col2]

squares = []
for i in range(1,101):
    squares.append(i**2)

print(squares)

squares2 = [i**2 for i in range(1,101)]
print(squares2)

#create list of remainders when you divide the first 100 squares
remainders5 = [x**2 % 5 for x in range(1,101)]
print(remainders5)

remainders11 = [x**2 % 11 for x in range(1,101)]
print(remainders11)

#Movies with list and without list comprehension
movies = ["Star Wars", "Gandi", "Casablanca", "Shawshank Redemption",
          "Gone with the Wind", "To Kill a Mockingbird", "Raiders of Lost Ark","Groundhog Day"]

gmovies = []
for title in movies:
    if title.startswith("G"):
        gmovies.append(title)

print(gmovies)

gmovies2 = [title for title in movies if title.startswith("G")]
print(gmovies2)

movies2 = [("Star Wars", 1941), ("Gandi", 2001), ( "Casablanca", 1946),  ("Shawshank Redemption", 1993),
           ("Gone with the Wind", 1954),  ("To Kill a Mockingbird", 1981),  ("Raiders of Lost Ark", 1981), ("Groundhog Day", 1993)]

#find movies released before 2000
m2 = [title for (title,year) in movies2 if year < 2000]
print(m2)

v = [2,-3,1]
#scalar multiplication
#If you try 4*v its the same as 4*v = v+v+v+v, which concatenate the lists
#output = [2,-3,1,2,-3,1,2,-3,1,2,-3,1,] e.g [2,4,5] + [1,3] = [2,4,6,1,3]

w = [4*x for x in v] #correct way
print(w)

#Cartesian Product
# If A and B are sets, then the Cartesian product is the set
# of pairs (a,b) where 'a' is in A and 'b' is in B.
# e.g A = {1,3} B = {x,y}
# AxB = {(1,x), (1,y), (3,x), (3,y)}

A = [1,3,5,7]
B = [2,4,6,8]
#write a for loop for elements of a, write one for b
cartesian_product = [(a,b) for a in A for b in B]
print(cartesian_product)
