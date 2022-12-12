# https://cs50.harvard.edu/python/2022/psets/1/extensions/

user_input = input('Podaj nazwę pliku: ')

image_extensions = ['gif', 'jpg', 'jpeg', 'png']
application_extensions = ['pdf', 'txt', 'zip']
all_extensions = image_extensions + application_extensions

for element in image_extensions:
    if element in user_input:
        print('Image/' + element)

for element_dwa in application_extensions:
    if element_dwa in user_input:
        print('Application/' + element_dwa)

if '.' not in user_input:
    print('Application/octet-stream')
