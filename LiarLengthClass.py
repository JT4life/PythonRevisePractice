class Liar(list):
    def __len__(self):
        a = super().__len__()
        return a+2

list1 = [1,2,3]

a = Liar(list1)
print(a)
print(len(a))