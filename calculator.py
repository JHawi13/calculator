#ay mate this be a python projekt fir calculatin
number1=eval(input("Enter a number"))
number2=eval(input("Enter another number"))
#DRY-Don't repeat yourself
operator=input("Enter an operator")
def add(num1,num2):
    result=num1+num2
    return[result]
def subtract(num1,num2):
    result=num1-num2
    return result

def divide(num1,num2):
    result=num1/num2
    return result

def multiply (num1,num2):
    result=num1*num2
    return result
    