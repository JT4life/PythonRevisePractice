from threading import *
from time import sleep
import sys

class Display1(Thread):
    def run(self):
        for i in range(1,11):
            print(i)
            sleep(1)
class Display2(Thread):
    def run(self):
        lst = ['one','two','three','four','five','six','seven','eight','nine','ten']
        for i in lst:
            print(i)
            sleep(1)

o1 = Display1()
o2 = Display2()

o1.start()
sleep(.02)
o2.start()

o1.join()
o2.join()

