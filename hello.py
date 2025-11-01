n=int(input("Enter number of elements you want"))
next=0
first=0
second=1
for i in range (n):
    if(i<=1):
        next=i
    else:
        next=first+second
        first=second
        second=next
    print(next)
