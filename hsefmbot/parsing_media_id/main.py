import re

def storage():
    with open('html.txt', 'r') as file:
        return file.read()
   

data = storage()

res = re.findall(r'data-full-id="[-\d_]+', data)

res = ''.join(['audio' + i[14:] + ' ' for i in res])

print(res)

input(...)
