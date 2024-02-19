from calculator_art import logo
print(logo) 
x=True
n1=float(input("enter the number :"))
op=input('enter the operation you want to perfom + , - , * , / :')
n2=float(input("enter second number :"))
def cal(num1=n1,num2=n2,sym=op):
    if sym=='+':
        return num1+num2
    elif sym=='-':
        return num1-num2
    elif sym=='*':
        return num1*num2
    elif sym=='/':
        if(num2==0):
            print(" 0 can't be divisible by any number")
            return None
        else:
          return num1/num2
while x:
    value=cal(n1,n2,op)
    if value!=None:
        print(f"The result of {n1} {op} {n2} is: {value}")
        x=input("enter 'yes' if you want to continue with the value other wise 'no': ").lower()
        if x=='yes':
            n1=value
            op=input('enter the operation you want to perfom + , - , * , / :')
            n2=float(input('enter the number'))
            value=cal(n1,n2,op)
        else:
            break
    else:
        break
