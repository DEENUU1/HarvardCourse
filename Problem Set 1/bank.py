# https://cs50.harvard.edu/python/2022/psets/1/bank/

# Jeżeli Hello -> 0
# Jeżeli zaczyna się od 'H' ale nie jest to Hello -> 20
# Jeżeli coś innego -> 100

user_input = input('Przywitaj się: ')
first_letter = user_input[0]

if 'Hello' in user_input:
    print('$0')

if first_letter == 'H' and 'Hello' not in user_input:
    print('$20')

if first_letter != 'H':
    print('$100')
