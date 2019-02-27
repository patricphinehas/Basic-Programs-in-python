def prime(upper):
    lower=1
    for num in range(lower,upper + 1):
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
        else:
           print(num)

upper = int(input("enter the upper bound"))
print("Prime numbers between 1 and",upper,"are:")
prime(upper)