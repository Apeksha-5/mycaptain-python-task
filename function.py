#Frequency Python Program for function 
s=str(input("Enter string:"))
def most_frequent(string):
    d=dict()
    for key in string:
        if key not in d:
            d[key]=1
        else:
            d[key]+=1
    return d
print(most_frequent(s))
