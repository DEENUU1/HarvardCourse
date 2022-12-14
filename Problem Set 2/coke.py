# https://cs50.harvard.edu/python/2022/psets/2/coke/

coke = 50
user_money = 0

while user_money != coke:
    user_money_input = input('How much money you drop? ')
    accept_money = ['25', '10', '5']
    if user_money_input not in accept_money:
        print("Zły nominał")
        break
    user_money += int(user_money_input)

    total = coke - user_money
    print("Brakuje: " + str(total))

    if user_money == coke:
        print("Masz cole")
