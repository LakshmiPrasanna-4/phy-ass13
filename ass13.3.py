# Write a program to print second minimum from the list.

n=int (input())
l=[]
for i in range(n):
    x=int(input())
    l.append(x)
min=l[0]
for i in range(0,n):
    if l[i]<min:
       min=l[i]
l.remove(min)
min=l[0]
for i in l:
    if i<min:
       min=i
print(min)
