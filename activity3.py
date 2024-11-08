#calculator

def add(a,b):
    return a+b

def product(a,b):
    return a*b

def quotient(a,b):
    return a/b

def difference(a,b):
    return(a-b)

n1=int(input("enter first number"))
n2=int(input("enter second number"))


print("sum of {0} and {1} is {2}".format (n1,n2,add(n1,n2)))
print("difference of {0} and {1} is {2}".format (n1,n2,difference(n1,n2)))
print("product of {0} and {1} is {2}".format (n1,n2,product(n1,n2)))
print("quotient of {0} and {1} is {2}".format (n1,n2,quotient(n1,n2)))