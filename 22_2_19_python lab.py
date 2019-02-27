# program for adding two list

# a=[1,2,3];b=[4,1,4];c=[]
# for i in range(0,3):
#     c.append(int(a[i]+b[i]))

# print(c)

# even numbers and odd numbers
# a=[1,2,3,4,5,6,7,8,9,10,18,15]

# for


# multi dimesions in a list
# l = [[1,2],[3,4],[5,6]]
# print(l[2][0])
# print(l)


# #list simgle flip check
a=['1','0','1','1','1','1']
print(len(a))
oneCount=0
zeroCount=0
for i in range(0,len(a)):
    print(a[i])
    if(a[i]=='1'):
        oneCount=oneCount+1
    else:
        zeroCount=zeroCount+1

print(oneCount)
print(zeroCount)
t = len(a)-1
print(t)
if((t==oneCount) or (t==zeroCount)):
    print("possible")
else:
    print("not possible")

# if oneCount==t:
#     print("single flip change possible"
# else:
#     print("single flip not possible")