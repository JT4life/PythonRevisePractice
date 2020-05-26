# if a is non negative return a**(1/b)
# if a is negative and eve, return "Result is an imaginary number"
# if a is negative and odd, return -(-a)**(1/b)

def safe_root(a,b):
    if a >= 0:
        answer = a**(1/b)
    else:
        if a % 2 == 0:
            answer = "result imaginary"
        else:
            answer = -(-a)**(1/b)
    return answer
