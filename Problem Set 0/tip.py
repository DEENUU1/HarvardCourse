# https://cs50.harvard.edu/python/2022/psets/0/tip/


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    float_d = d.replace('$', '')
    return float(float_d)

def percent_to_float(p):
    float_p = p.replace('%', '')
    return float(float_p)/100


main()