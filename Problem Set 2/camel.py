# https://cs50.harvard.edu/python/2022/psets/2/camel/

user_input = input("Wprowadź jakiś ciąg znaków: ")

for element in user_input:
    if element.isupper():
        print('_' + element.lower(), end='')

    else:
        print(element, end='')
print()