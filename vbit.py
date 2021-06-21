'''To print the Net Bonus Amount
defining the function bonus_Amount we pass Two parameters 'salary' and 'year_of _service'
There will be two cases
if year_of_service>5 calculate and print the statement else print('no bonus')

In the main method
s=int(input()) which takes the value of salary
year=in(input()) which takes the years of servies
calling the function and passing the arguments s and year is done to execute
'''

def bonus_Amount(salary, year_of_service):
    if year_of_service>5 :
        bonus= int(salary*(5/100))
        print(f'Bonus is {bonus}')
    else:
        print('No Bonus')

s=int(input())
year=int(input())
bonus_Amount(s, year)



