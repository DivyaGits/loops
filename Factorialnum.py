# factorial number

n=int(input("\n enter the number:"))
x=n
sum=0
while n>0:
    r=n%10
    i=1
    fact=1
    while i<=r:
        fact=fact*i
        i=i+1
    sum=sum+fact
    n=n//10
if x==sum:
    print("this is a factorial",sum)
else:
    print("this is not a factorial",sum)   