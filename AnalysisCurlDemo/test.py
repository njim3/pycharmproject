# coding: utf-8


def passarg(arg1, arg2, arg3=()):
    if not arg3:
        print('empty')


passarg(1, 2)


def return2res():
    x = 1
    y = 2

    return x, y


print(return2res())
