def load_file():
    with open('apache_logs.txt', 'r') as f:
        file = f.read()
        file = file.split('\n')

    res = []
    for item in file:
        res.append(item)
    return res


def filter_func(method: str, data: str):
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


def limit_func(num: int, data: str):
    return [data[item] for item in range(num)]


def map_func(num: int, data):
    res = []
    for item in data:
        tmp = item.split(' ')
        tmp[1] = tmp[3] + ']'
        tmp[2] = tmp[5]
        tmp[3] = tmp[6]
        tmp[4] = tmp[7]
        tmp[5] = tmp[8]
        res.append(tmp[num])
    return res


def unique_func(arg, data):
    pass


def sort_func(method: str, data):
    pass
