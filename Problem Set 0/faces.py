# https://cs50.harvard.edu/python/2022/psets/0/faces/


def main():
    user_input = input("O czym myslisz? ")
    user_input = emoticonConverter(user_input)
    print(user_input)

def emoticonConverter(user_input):
    user_input = user_input.replace(':)', '🙂')
    user_input = user_input.replace(':(', '🙁')
    return user_input

main()
