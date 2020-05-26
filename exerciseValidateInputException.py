number = 0.0
while number <= 0:
    try:
        number = float(input('Enter a number to square: '))
        print(number ** 2)
    except TypeError:
        print("data type error")
        continue
    except NameError:
        print("Variable name error")
        continue
    except:
        print("Unknown error occured")
        continue
    finally:
        print('bye bye')
