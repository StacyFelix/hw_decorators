import pickle
import traceback
import datetime
import os


def logger(func):
    path_file = os.path.join(os.path.dirname(__file__), 'logs.dat')

    def add_log(*args, **kwargs):
        time_log = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        func_name = func.__name__
        with open(path_file, 'ab') as file:
            try:
                result = func(*args, **kwargs)
            except Exception as err:
                tb = traceback.format_exc()
                pickle.dump((time_log, func_name, args, kwargs, tb), file)
            else:
                pickle.dump((time_log, func_name, args, kwargs, result), file)
                return result
    return add_log


@logger
def foo(a, b):
    return a / b


if __name__ == '__main__':
    foo(1, 0)
    foo(1, 'a')
    foo(1, 1)

    path_file = os.path.join(os.path.dirname(__file__), 'logs.dat')

    with open(path_file, 'rb') as file:
        log_data = pickle.load(file)
        for item in log_data:
            print(item)
