# If number divisible of 3 print fizz, if 5 print buzz, if both print fizzbuzz
def fizzbuzz(lst):
    for number in lst:
        if number % 15 == 0:
            print(number, ' fizzbuzz')
        elif number % 3 == 0:
            print(number, ' fizz')
        elif number % 5 == 0:
            print(number, ' buzz')
        else:
            print(number,' number not a part of fizzbuzz')
            
lst = [1,2,3,4,5,6,10,15]

fizzbuzz(lst)
