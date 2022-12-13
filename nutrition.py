user_input = str(input("Co chcesz zjeść? "))

food_calories = {
    'apple': 130,
    'banana': 120,
    'bread': 35,
    'fish': 100,
    'kebab': 990,
}

print(food_calories[user_input], 'tyle kcal ma ' + user_input)