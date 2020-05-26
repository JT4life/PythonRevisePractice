import os
def read_lines():
    if os.path.isfile('text1.text'):
        with open('text1.text', 'r') as file:
            return file.readline()
    else:
        return None