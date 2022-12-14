# https://cs50.harvard.edu/python/2022/psets/3/outdated/

# month day year
# zamienić na
# year month day
while True:
    try:
        month, day, year = input('Podaj datę w formacie MONTH-DAY-YEAR: ').split('/')
        print(year + '-' + month + '-' + day)

    except ValueError:
        try:
            month, day, year = input('Podaj datę w formacie MONTH-DAY-YEAR: ').split(' ')
            print(year + '-' + month + '-' + day)
        except:
            pass

