string= input("Введите строку: ")
alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
new_string = ''

for char in string:
    if char in alphabet :
        new_string += alphabet[-alphabet.index(char)-1]
    else:
        new_string += char
print(new_string)
new_string=list(new_string)
my_list = new_string
c=list()
c1=list()
for i in range(len(my_list)):
    if my_list[i] != ' ':
        c.append(my_list[i])
    else: c1.append(i)

for i in range(0, len(c)-1, 2):
    c[i], c[i+1] = c[i+1], c[i]
for i in range(len(c1)):
    c.insert(c1[i],' ')
print(*c,sep='')