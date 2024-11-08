#factorial

def fact(n):
   if n==1: 
      return n
   else:
      return n*fact(n-1)

num=int(input("enter a num"))

if num<0:
    print("cannot find factorial for numbers less than 0")
elif num==0:
      print("factorial is 1")
else:
    print("factorial of", num, "is", fact(num))
    
