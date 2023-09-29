import os


def func(directory_name):
    print(os.getcwd())
    if not os.path.exists(directory_name):
        os.mkdir(directory_name)
        print(f'{directory_name} created')


func('temp_folder')
