user_input = input("Co tam u ciebie? ")

vowels = ['a', 'e', 'u', 'o', 'A', 'E', 'U', 'O', 'i', 'I']

short_sentence = []

for letters in user_input:
    if letters in vowels:
        user_input.replace(letters, '')
    else:
        short_sentence.append(letters)

str_short_sentence = ''.join(short_sentence)

print(str_short_sentence)