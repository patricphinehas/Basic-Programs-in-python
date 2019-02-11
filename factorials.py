def factorial(num):
    sum = 1
    for i in range(1,num+1):
        sum=sum*i
    print(sum)

num = int(input("enter the number"))
factorial(num)
