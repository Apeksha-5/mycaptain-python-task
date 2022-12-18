#python program for fibonacci series using for loop
n=int(input("Enter the number of terms: "))
a=0 
b=1 
if n<=0:
    print("The Output of your input is",a)
else:
    print(a,b,end=" ")
    for x in range(2,n):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
