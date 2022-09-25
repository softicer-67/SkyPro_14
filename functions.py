from typing import List


def load_file():
    with open('apache_logs.txt', 'r') as f:
        file = f.read()
        file = file.split('\n')

    res = []
    for item in file:
        res.append(item)
    return res


def filter_func(method: str, data):
    res = []
    if method == 'POST':
        for item in data:
            if 'POST' in item:
                res.append(item)

    elif method == 'GET':
        for item in data:
            if 'GET' in item:
                res.append(item)
    return res


def limit_func(num: int, data: list):
    return [data[item] for item in range(num)]


def map_func(num: int, data: list):
    res: List[str] = []
    if num > 5:
        print('Индекс превышен !')
        return res
    for item in data:
        tmp = item.split(' ')

        if num == 0:
            res.append(tmp[num])
        elif num == 1:
            res.append(tmp[3] + ']')
        elif num > 1:
            res.append(tmp[num + 3])
    return res


def unique_func(arg, data):
    if arg == '-':
        return set(data)
    return data


def sort_func(method, data):
    if method == 'asc':
        return sorted(data, key=lambda x: tuple(map(int, x.split('.'))))
    elif method == 'desc':
        return sorted(data, key=lambda x: tuple(map(int, x.split('.'))), reverse=True)
