'''defining the function multiplication passing the parameter 'number'
using while loop we multiply the number using the condition

In the main method we declare a variable 'value' which takes the input
we call the function and pass the argument value
'''
def multiplication(number):
    i=1
    while i<=10:
        output=i*number
        print(output)
        i += 1

value =int(input())
multiplication(value)

