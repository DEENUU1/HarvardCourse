# https://cs50.harvard.edu/python/2022/psets/1/meal/
# 7:00 - 8:00 -> breakfast time
# 12:00 - 13:00 -> lunch time
# 18:00 - 19:00 -> dinner time

def main():
    time = input('time: ')
    convert_time = convert(time)

    if convert_time >= 7 and convert_time <= 8:
        print('Breakfast time!')
    if convert_time >= 12 and convert_time <= 13:
        print('Lunch time!')
    if convert_time >= 18 and convert_time <= 19:
        print('Dinner time!')

def convert(time):
    hours, minutes = time.split(':')
    hours = float(hours) + (float(minutes)/60)
    return hours


if __name__ == "__main__":
    main()