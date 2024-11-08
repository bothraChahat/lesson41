#fibonacci series

def recur_fibo(n):
    if n<= 1:
        return n
    else:
        return(recur_fibo(n-1)+ recur_fibo(n-2))
    
nterms=int(input("enter number of terms:"))

#check if the number of terms is valid 
if nterms<= 0:
    print("please enter a positive integer")
else:
    print("fibonacci sequence")
for i in range(nterms):
    print(recur_fibo(i))
    

    