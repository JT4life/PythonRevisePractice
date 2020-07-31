#breaking down big parts to small parts, multitasking
#execution is always done with main thread
#Instead of run you use start for Threads which will call method run in Thread class
from threading import *
from time import sleep

class Hello(Thread): #Make it subclass of Thread
    def run(self):
        for i in range(5):
            #Use sleep so we don't have collisions
            print("Hello")
            sleep(1)

class Bye(Thread):
    def run(self):
        for i in range(5):
            print("Bye")
            sleep(1)

o1 = Hello()
o2 = Bye()

o1.start()
sleep(.02)
o2.start()

#let main thread wait for both threads to join before next execution
o1.join()
o2.join()

print("Hi")