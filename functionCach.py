import time
from functools import lru_cache
@lru_cache(maxsize=3)
def abc(n):
    time.sleep(4)
    return n
if __name__=='__main__':
    print("Calling function")
    abc(10)
    print("Again Calling function")
    abc(10)
    print("2 Again Calling function")
    abc(10)