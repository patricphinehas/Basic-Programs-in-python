num = int(input(" enter the number to check for perfect Number"))
sum = 0
for i in range(1,num):
    if(num%i==0):
        sum = sum+i
# print(sum)
if (sum==num) or (num==1):
    print("the number is a perfect Number")
else:
    print("the number is not a perfect Number")