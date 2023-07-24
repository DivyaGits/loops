
#Q prime number

num=int(input("enter the num:"))
i=1
while i<=num:
    j=1
    count=0
    while j<= i:
        if i % j == 0:
            count += 1
        j = j + 1
    if count == 2:
        print(i,"prime number")
    i=i+1