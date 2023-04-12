def max_num(*args):
    largest = 0
    for i in args:
        if (i> largest):
            largest = i
    return largest
# print(max_num(1, 7, 4))

def mult_list(list):
    product = 1
    for i in list:
        product = i*product
    return product
# print(mult_list([1,3,5]))
# print(mult_list([3,5,0]))

def reverse_string(string):
    return string[::-1]
print(reverse_string("Jello"))

def num_within( number, beginning, end):
    if (number<end and number>beginning):
        return True
    else:
        return False
# print(num_within( 5, 1, 10))
# print(num_within(2, 3, 10))

