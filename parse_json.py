import json


def read_file(path: str) -> dict:
    with open(path) as json_file:
        data = json.load(json_file)
    return data


def navigation(path: str):
    data = read_file(path)
    json_obj = data
    path = []
    while True:
        path.apend(json_obj)
        if type(json_obj) == list:
            print('This is a list. It contains {} elements.'.format(len(json_obj)))
        elif type(json_obj) == dict:
            print('This is a dictionary. It has following keys: {}.'.format(
                ', '.join(json_obj.keys())))
        else:
            print('This is a {}.'.format(type(json_obj)))
        option = input('Enter an option: ')
        if option == 'stop':
            break
        elif option == 'show':
            print(json_obj)
        elif option == 'up':
            json_obj = path.pop()[1]
        elif option == 'down':
            if (type(json_obj) != dict) and (type(json_obj) != list):
                print('You cant choose this option. Try another one.')
            else:
                if type(json_obj) == dict:
                    key = input('Enter a key: ')
                    json_obj = json_obj[key]
                else:
                    index = int(input('Enter an index: '))
                    json_obj = json_obj[index]
        else:
            print('You entered invalid option. Try again.')
