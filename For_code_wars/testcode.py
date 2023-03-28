string = 'Pig latin is cool'
index = 0
string = string.split(' ')
list_str = []

while index < len(string):
    if index != '!':
        string1 = f'{string[index][1:]}{string[index][0]}ay'
        list_str.append(string1)
        index += 1
list_str = ' '.join(list_str)
if list_str[-3] == '!':
    print(list_str[0:-2])
else:
    print(list_str)
