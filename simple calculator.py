def  sum(a,b):
    s=a+b
    return s

def  sub(a,b):
    s=a-b
    return s

def  divide(a,b):
    s=a/b
    return s

def  multiply(a,b):
    s=a*b
    return s

a=int(input("Enter 1st number :"))
b=int(input("Enter 2nd number :"))
ot=(input("Enter operation to be performed :"))

if ot == "+" or ot == "add":
    print(sum(a,b))
elif ot == "-" or ot == "subtract":
    print(sub(a,b))
elif ot == "*" or ot == "multiply":
    print(multiply(a,b))
elif ot == "/" or ot == "divide":
    print(divide(a,b))