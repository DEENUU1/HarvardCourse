# https://cs50.harvard.edu/python/2022/psets/4/game/
import random

while True:
    try:
        level = int(input('Level: '))
        if level > 0:
            break
    except:
        pass

random_number = random.randint(0, level)

while True:
    try:
        quess = int(input('Quess: '))
        if quess > 0:
            if quess == random_number:
                print('Zgadłeś!!!!')
                break

            if quess > random_number:
                print('Za duża!')

            if quess < random_number:
                print('Za mała!')

    except:
        pass