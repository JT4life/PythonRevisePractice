# 7.  Find the most frequent value in a list
lst = [1,2,3,3,4]
def lstFr(lst):
    return max(set(lst), key=lst.count)
print(lstFr(lst))

test = [1, 2, 3, 9, 2, 7, 3, 5, 9, 9, 9]
print(max(set(test), key = test.count))

# 8.  Print the file path of imported modules
import os;
print(os)

print(type(2//4))
n='l'
print(id(n))

def delete_book(book_id):
    books = [{'id':0,'title':u'harry'},{'id':1,'title':u'lord'}]
    book = [book for book in books if book['id'] == book_id]
    books.remove(book[0])
