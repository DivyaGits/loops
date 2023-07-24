a=10000
i=1
while i <= a:
    j = 1
    s = 0
    while j < i:
        if i % j == 0:
            s =s + j
        j = j + 1   
    if s == i:
        print(i,"perfect number")       
    i = i + 1