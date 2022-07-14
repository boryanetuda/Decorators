import requests
from datetime import datetime


dec_logs = 'logs.txt'
path = '/Users/igorborisov/PycharmProjects/Decorators/logs.txt'


def logs(path):
    def _logs(old_func):
        def new_func(*args, **kwargs):
            date_time = datetime.now().strftime('%Y-%m-%d. Время: %H-%M-%S')
            result = old_func(*args, **kwargs)
            with open(path, 'a') as file:
                file.write(f'Дата вызова функции: {date_time}\n'
                           f'Имя функции: {old_func.__name__}\n'
                           f'Аргументы функции: {args, kwargs}\n'
                           f'Значение функции: {result}\n'
                           f'{"-"*50}\n')

            return result
        return new_func
    return _logs


@logs(dec_logs)
def get_status(*args):
    url = ','.join(args)
    response = requests.get(url=url)
    return response.status_code


@logs(dec_logs)
def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact


if __name__ == '__main__':
    get_status('https://habr.com/ru/all/')
    factorial(8)


# from datetime import datetime
# import requests
#
# dec_logs = 'logs.txt'
#
#
# def logs(path):
#     def _logs(oldfunc):
#         def newfunc(*args, **kwargs):
#             result = oldfunc(*args, **kwargs)
#             with open(path, 'a', encoding='utf-8') as file:
#                 file.write(f'\nДата вызова функции: {datetime.now().strftime("%Y-%m-%d. Время: %H-%M-%S")}\n'
#                            f'Имя функции: {oldfunc.__name__}\n'
#                            f'Аргументы функции: {args, kwargs}\n'
#                            f'Возвращаемое значение функции: {oldfunc(*args, **kwargs)}\n'
#                            f'{"-" * 50}\n')
#             return result
#
#         return newfunc
#
#     return _logs
#
#
# @logs(dec_logs)
# def get_status(*args):
#     url = ','.join(args)
#     response = requests.get(url=url)
#     return response.status_code
#
#
# @logs(dec_logs)
# def factorial(n):
#     fact = 1
#     for num in range(2, n + 1):
#         fact *= num
#     return fact
#
#
# if __name__ == '__main__':
#     get_status('https://habr.com/ru/all/')
#     factorial(8)