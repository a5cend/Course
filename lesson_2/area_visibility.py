vid_1 = 12


def global_func():
    print(vid_1)


def func_two():
    vid_1 = 'local_value'
    print(vid_1)


def func_three():
    global vid_1
    vid_1 = 'rewrite'


global_func()
func_two()
print(vid_1)
func_three()
print(vid_1)
