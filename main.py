from functions import *


def main():
    file = load_file()
    res = []
    # command = input(f'Введите команду из доступных через |: filter, map, limit, sort, unique\n>>> ')
    command = 'filter GET | limit 10 | map 1 | unique - | sort asc'

    commands = command.split(' | ')
    try:
        for idx, item in enumerate(commands):
            format_item = item.split(' ')
            cmd_name = format_item[0]
            cmd_arg = format_item[1]

            if cmd_name == 'filter':
                res = filter_func(cmd_arg, file if idx == 0 else res)
            elif cmd_name == 'limit':
                res = limit_func(int(cmd_arg), file if idx == 0 else res)
            elif cmd_name == 'map':
                res = map_func(int(cmd_arg), file if idx == 0 else res)
            elif cmd_name == 'unique':
                res = unique_func(cmd_arg, file if idx == 0 else res)
            elif cmd_name == 'sort':
                res = sort_func(cmd_arg, file if idx == 0 else res)
    except IndexError:
        print('\nОшибка ввода')
        quit()

    for item in res:
        res = str(item).split(' ')
        ln = len(res)
        if ln < 6:
            print(f"{res[0]}")
        else:
            print(f"{res[0]} {res[3]}] {res[5]} {res[6]} {res[7]} {res[8]}")


if __name__ == '__main__':
    main()

