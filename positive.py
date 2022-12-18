# print positive Numbers in a List
  
# input of list
l=[]
n=int(input("Enter size of list "))
for i in range(0,n):
    e=int(input("Enter element of list "))
    l.append(e)

print("Positive numbers in",l,"are: ")
  
#traversing
for i in l:   
    # checking condition
    if i >= 0:
       print(i, end = " ")
