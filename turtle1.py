import turtle

# turtle.color('green')
# turtle.forward(100)
# turtle.right(45)
# turtle.color('blue')
# turtle.forward(50)
# turtle.right(45)
# turtle.color('pink')
# turtle.forward(100)

# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
#
# for steps in range(4):
#     turtle.forward(100)
#     turtle.right(90)


# for steps in range(4):
#     turtle.forward(100)
#     turtle.right(90)
#     for extraSteps in range(4):
#         turtle.forward(50)
#         turtle.right(90)

# for steps in range(5):
#     turtle.forward(100)
#     turtle.right(360/5)
#     for extraSteps in range(5):
#         turtle.forward(50)
#         turtle.right(360/5)

#Challenge Octagon
user = int(input("How many sides enter a number"))
for steps in range(user):
    turtle.forward(100)
    turtle.right(360/user)