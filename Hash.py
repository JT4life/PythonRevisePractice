#Python help, I think he/she was missing extra code because I had to define my own class, user was trying to call table without table being defined...

class A:
    def __init__(self,table):
        self.table = table

    def hash(self,string):
        total = 0
        for i in string:
            total = total + ord(i)
        rem = total % 13
        return rem


    def init_table(self,n):
        self.table = []
        self.table += [''] * n
        return self.table


    # TASK 3.2
    def hash_table(self,seq):
        for i in seq:
            x = hash(i)
            self.table.insert(x, i)
        return self.table


keys1 = ('onion', 'tomato', 'cabbage', 'okra', 'banana', 'salt', 'cucumber', 'mushroom', 'orange')
table1 = A()
table1.hash_table(keys1)