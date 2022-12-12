# https://cs50.harvard.edu/python/2022/psets/1/interpreter/

first_num, symbol, second_num = input('Twoje działanie: ').split(' ')

if symbol == '+':
    total = float(first_num) + float(second_num)
    print(total)

if symbol == '-':
    total = float(first_num) - float(second_num)
    print(total)

if symbol == '/':
    total = float(first_num) / float(second_num)
    print(total)

if symbol == '*':
    total = float(first_num) * float(second_num)
    print(total)