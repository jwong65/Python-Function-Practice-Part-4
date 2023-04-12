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
# print(reverse_string("Jello"))

def num_within( number, beginning, end):
    if (number<end and number>beginning):
        return True
    else:
        return False
# print(num_within( 5, 1, 10))
# print(num_within(2, 3, 10))

# Pascal triangle..?
# TO output multiple rows have a list to represent the rows
# Second number in the row will show how many rows.
triangle = [[1],[1,1]]
def pascal(n):
    if n==1:
        print(triangle[0])
    else:
        row_number= 2
        # Length of the triangle is 2 right now
        while len(triangle)<n:
            row = []
            row_prev = triangle[row_number-1]
            length = len(row_prev)+1
            for i in range(length):
                if i ==0:
                    row.append(1)
                elif i>0 and i< length-1:
                    row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
                else:
                    row.append(1)
            triangle.append(row)
            row_number+=1
        
        for row in triangle:
            print(row)

# pascal(3)