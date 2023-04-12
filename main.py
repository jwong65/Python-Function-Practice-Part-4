def max_num(*args):
    largest = 0
    for i in args:
        if (i> largest):
            largest = i
    return largest
# print(max_num(1, 7, 4))