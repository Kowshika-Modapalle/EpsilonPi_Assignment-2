# defining a function square_rectangle with two parameters length and breadth
# if the value of length and breadth are equal then the if block will return is_square which is true
def square_Rectangle(length, breadth):
    is_square = True
    if length == breadth:
        return is_square


# l and b are variables which takes the input from user
# we will call the function square_Rectangle by passing the arguments l,b and the output is stored in a variable output
# if output== True then it prints yes,if it is Not True then it prints No
l = int(input())
b = int(input())
output = square_Rectangle(l, b)
if (output == True):
    print('yes')
else:
    print('No')
