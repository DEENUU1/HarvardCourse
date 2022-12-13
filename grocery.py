# https://cs50.harvard.edu/python/2022/psets/3/grocery/

grocery = {}
while True:
    try:
        user_input = input("Co chciałbyś kupić? ").lower()

        if user_input in grocery:
            grocery[user_input] += 1

        else:
            grocery[user_input] = 1

    except EOFError:
        for key in sorted(grocery.keys()):
            print(grocery[key], key.upper())
        break