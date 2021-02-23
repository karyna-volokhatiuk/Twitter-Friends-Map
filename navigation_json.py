'''
This module helps user with navigation in json files.
'''
import json
from typing import Any


def read_json_file(json_file: str) -> Any:
    '''
    Return data from json_file.
    '''
    json_file = open(json_file, encoding='utf-8')
    data = json.load(json_file)
    return data


def emojis_for_types(type_name: str) -> str:
    '''
    Return an emoji that depends on input type_name.
    >>> emojis_for_types('list')
    '🦝'
    >>> emojis_for_types('dict')
    '🐑'
    >>> emojis_for_types('int')
    '🦥'
    '''
    if type_name == 'list':
        return '🦝'
    if type_name == 'dict':
        return '🐑'
    return '🦥'


def come_back(data, path, steps_back):
    '''
    Return data after passing the path
    without last steps_back steps.
    '''
    if len(path) - steps_back >= 0:
        path = path[:len(path)-steps_back]
        for i in path:
            data = data[i]
    return [data, path]


def navigation_list(start_data: list, data: list, path: list) -> Any:
    '''
    Return data from list data found with path that user input.
    '''
    print('Choose index of element from list: ')
    for index, element in enumerate(data):
        type_name = type(element).__name__
        element_info = (index, emojis_for_types(type_name), type_name)
        print(*element_info)
    while True:
        try:
            index_of_object = input('Write index: ')
            if '*' in index_of_object:
                after_coming_back = come_back(
                    start_data, path, index_of_object.count('*'))
                data, path = after_coming_back[0], after_coming_back[1]
            else:
                index_of_object = int(index_of_object)
                data = data[index_of_object]
                path.append(index_of_object)
            return data, path
        except:
            pass


def navigation_dict(start_data: dict, data: dict, path: list) -> Any:
    '''
    Return data from dict data found with path that user input.
    '''
    print('Choose one of the keys: ')
    data_structure = []
    for index, name_of_key in enumerate(data.keys()):
        type_name = type(data[name_of_key]).__name__
        key_info = (index, name_of_key,
                    emojis_for_types(type_name), type_name)
        data_structure.append(key_info)
        print(*key_info)
    while True:
        try:
            index_of_object = input('Write index of the key: ')
            if '*' in index_of_object:
                after_coming_back = come_back(
                    start_data, path, index_of_object.count('*'))
                data, path = after_coming_back[0], after_coming_back[1]
            else:
                index_of_object = int(index_of_object)
                key_by_user = data_structure[index_of_object][1]
                data = data[key_by_user]
                path.append(key_by_user)
            return data, path
        except:
            pass


def communication_with_user() -> Any:
    '''
    Return data found with path that user input gradually
    from file that user input.
    '''
    while True:
        try:
            json_file = input('Please, write the name of json file: ')
            start_data = read_json_file(json_file)
            break
        except FileNotFoundError:
            pass
    data = start_data
    path = []
    while True:
        if isinstance(data, dict) and data:
            data, path = navigation_dict(start_data, data, path)
        elif isinstance(data, list) and data:
            data, path = navigation_list(start_data, data, path)
        else:
            print('With path: ')
            print(path)
            print('you got: ')
            print(data)
            return
