#Lets go
Equation=input("Enter the equation")
def any_simple_calculation (Equation):
    for i in range(len(Equation)):
        if Equation[i]=='/':
            operator=Equation.index('/')
            num1=int(Equation[0:operator])
            num2=int(Equation[operator+1:])
            return print(num1/num2)
        elif Equation[i]=='X':
            operator=Equation.index('X')
            num1=int(Equation[0:operator])
            num2=int(Equation[operator+1:])
            return print(num1*num2)
        elif Equation[i]=='x':
            operator=Equation.index('x')
            num1=int(Equation[0:operator])
            num2=int(Equation[operator+1:])
            return print(num1*num2)
        elif Equation[i]=='*':
            operator=Equation.index('*')
            num1=int(Equation[0:operator])
            num2=int(Equation[operator+1:])
            return print(num1*num2)
        elif Equation[i]=='+':
            operator=Equation.index('+')
            num1=int(Equation[0:operator])
            num2=int(Equation[operator+1:])
            return print(num1+num2)
        elif Equation[i]=='-':
            operator=Equation.index('-')
            num1=int(Equation[0:operator])
            num2=int(Equation[operator+1:])
            return print(num1-num2)
any_simple_calculation(Equation)