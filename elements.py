st = input("enter the string")
upCount=0
lowCount=0
vowels=0
# for i in range (0,len(st)):
#     print(st[i])
for i in range (0,len(st)):
    # print(st[i])
    if(st[i].isupper()):
        upCount+=1
    else:
        lowCount+=1
for i in range(0,len(st)):
    if(st[i]=='a') or (st[i]=='A') or (st[i]=='e') or (st[i]=='E') or (st[i]=='i') or (st[i]=='I') or (st[i]=='o') or (st[i]=='O') or (st[i]=='u') or (st[i]=='U'):
        vowels+=1
print("upper case", upCount)
print("lower case", lowCount)
print("vowels", vowels)