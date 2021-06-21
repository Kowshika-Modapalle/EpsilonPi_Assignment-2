#defining the function reverse_string passing a parameter my_string

def reverse(my_string):
    output_string = ''
    for i in my_string:
        output_string = i + output_string
    print(output_string)

text= input()
reverse(text)

