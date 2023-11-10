def add(m,n):
    return m+n

def diff(m,n):
    return m-n

def mul(m,n):
    return m*n

def div(m,n):
    return m/n

    
while True:
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
    n=int(input("Enter your choice:"))
    if n==1:
        a=int(input("Enter first number:"))
        b=int(input("Enter second nuumber:"))
        print(add(a,b))
    elif n==2:
        a=int(input("Enter first number:"))
        b=int(input("Enter second nuumber:"))
        print(diff(a,b))
    elif n==3:
        a=int(input("Enter first number:"))
        b=int(input("Enter second nuumber:"))
        print(mul(a,b))
    elif n==4:
        a=int(input("Enter first number:"))
        b=int(input("Enter second nuumber:"))
        print(div(a,b))
    elif n==5:
        break