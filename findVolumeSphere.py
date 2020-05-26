def volumeSphere(radius):
    #to Find volume you need to use the formula 4/3rd times 3.14 to the power of 3
    #then times 4 across the radius times pie, then divide by 3
    cubed = radius**3
    pieTimesCube = cubed * 3.14
    fourThree = 4 * pieTimesCube / 3
    print("Volume is = ", fourThree)

volumeSphere(5)