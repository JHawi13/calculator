#Lets go
Equation=input("Enter the equation")
def any_simple_calculation (Equation):
    operators=['/','X','+','-']
    for i in range(len(Equation)):
        for x in range(len(operators)):
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
