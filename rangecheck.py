num = int(input("enter the Number"))
st = int(input("start : "))
en = int(input("stop : "))
flag = 0
for i in range(st,en+1):
    if(i==num):
        flag = 1
if(flag==1):
    print("In Range")
else:
    print("element not found")