from math import trunc


namen_list = []

print('voer de namen in van je vrienden: ')
while True:
    name = input('naam: ')
    if name:
        namen_list.append(name)
    else:
        break
for name in namen_list:
    print(name)


print(len(namen_list))
