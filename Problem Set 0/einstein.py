# https://cs50.harvard.edu/python/2022/psets/0/einstein/



def converter():

    try:
        user_input = int(input("Podaj swoją wagę w kilogramach jako liczbę całkowitą: "))
        light_speed = 300000000**2
        total = int(user_input*light_speed)
        return total
    except ValueError:
        print("\nPodaj swoją wagę w liczbie całkowitej")

print(converter())