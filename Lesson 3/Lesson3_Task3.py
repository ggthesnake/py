def my_func(num_1, num_2, num_3):
    my_list = [num_1, num_2, num_3]
    try:
        my_list.remove(min(my_list))
        return sum(my_list)
    except TypeError:
        return "Вводите только числа"


def my_func(arg1, arg2, arg3):
    my_list = [arg1, arg2, arg3]
    return sum(sorted(my_list)[1:])


print(my_func(6, 19, -3))
