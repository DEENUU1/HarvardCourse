# https://cs50.harvard.edu/python/2022/psets/3/fuel/

# 1/4 == 25%
# 1/2 == 50%
# 3/4 == 75%


first_num, symbol, second_num = input('Twoje działanie: ').split(' ')

try:
    total = float(first_num) / float(second_num)
    per_status = total*100

    if per_status <= 1:
        print('E')
    if per_status >= 99:
        print('F')
    else:
        print(per_status)

except (ZeroDivisionError, ValueError):
    print('')


