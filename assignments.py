#Q1

# num=int(input("enter the num:"))
# if num%5==0 and num%11==0:
#     print("both")
# elif num%5==0:
#     print(num,"divisible by 5 only")
# elif num%11==0:
#     print(num,"divisible by 11 only")    
# else:
#     print("non")

#Q3

# num1=int(input("\n enter the number:"))
# num2=int(input("enter the number:"))
# num3=int(input("\n enter the num:"))
# if num1>num2 :
#     if num1<num3:
#         print(num1)
# if num1>num3 :
#     if num1<num2:
#         print(num1)
# if num2>num1:
#     if num2<num3:
#         print(num2)
# if num2>num3:
#     if num2<num1:
#         print(num2)        
# if num3>num2:
#     if num3<num2:
#         print(num3)        
# if num3>num1:
#     if num3<num2:
#         print(num3)

#Q6

# n=int(input("enter the num:"))
# x=2
# sum=0
# i=1
# while i<=n:
#     sum=sum+x
#     print(x,"+",end=" ")
#     i=i+1
#     x=x*10+2
# print("=",sum)    


#Q7

# n=int(input("enter the num:"))
# i=1
# j=1
# while i<n:
#     while j<=i:
#         print(j,end=" ")
#         j=j+1
#     i=i+2
#     j=j+1
#     print()   



#Q9


# arr=list(map(int,input("enter the arr:").split()))
# sum=int(input("enter the sum:"))
# i=0
# j=1
# s=0
# y=2
# len=len(arr)
# while i<len:
#     while j<len:
#         while y<len:
#             c=arr[i]
#             x=arr[j]
#             z=arr[y]
#             s=x+c+z
#             i=i+1
#             j=j+1
#             y=y+1
#             if x==sum:
#                 print([x])
#             elif  c==sum:
#                 print([c])
#             elif z==sum:
#                 print([z])
#             elif s==sum:
#                 print([c,x,z])



#Q5


# num=int(input("enter the num:"))
# n=num*3
# i=2
# count=0
# while i<=n:
#     count=0
#     j=1
#     while j<=i:
#         if i%j==0:
#           count+=1
#         j=j+1
#     if count!=2:
#        print(i)

#     i=i+1


#Q7

# n=int(input("enter the num:"))
# i=1
# x=0
# while i<=n:
#     j=1
#     while j<=i:
#         print(x+j,end=" ")
#         j=j+1
#     i=i+1
#     x=x+1
#     print()    

#Q10

# arr=list(map(int,input("enter the num:").split()))
# len=len(arr)
# i=0
# list=[]
# list2=[]
# while i<=len:
#     c=arr[i]
#     if c>0:
#         list=list+[c]
#     else:
#         list2=list2+[c]    
#     i=i+1
#     print(list2+list)    


#Q4

# n=int(input("enter the num:"))
# s=0
# x=0
# while n>0:
#     r=n%10
#     s=s+r
#     n=n//10
# if s>9:
#     r=s%10
#     x=x+r
#     s=s//10
#     print(s)


#Q2


# a=int(input("enter the num:"))
# b=int(input("enter the num:"))
# c=int(input("enter the  num:"))

# if a+b>c or b+c>a or c+a>b:
#     print("validate tringle")
# elif a==b or b==c or c==a:
#     print("equilateral ")
# elif a!=b or b!=c or c!=a:
#     print("scalene")
# elif (a==b and a!=c) or (b==c and c!=a) or (c==a and c!=b):
#     print("isosceles ")
# if a*a+b*b==c or b*b+c*c==a*a or c*c+a*a==b*b:
#     print("right-angled triangle")
