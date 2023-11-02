# Write a program to print minimum value from the list.

n=int(input())
l=[]
for i in range(n):
    x=int(input())
    l.append(x)
min=l[0]
for i in range(0,n):
    if l[i]<min:
        min=l[i]
print(min)
