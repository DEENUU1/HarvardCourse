# https://cs50.harvard.edu/python/2022/psets/6/lines/

while True:
    try:
        user_input = input('Podaj nazwę pliku pythona: ')

        if user_input[-3:] != '.py':
            print('Błędna nazwa pliku')
            break

        count = 0

        if user_input[-3:] == '.py':
            with open(user_input, 'r') as f:
                for count, line in enumerate(f):
                    pass

                print(count+1)

    except FileNotFoundError:
        print("Plik nie istnieje")