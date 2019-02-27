# f = open("/Volumes/TROLLHUNTER/python Lab/Basic-Programs-in-python/file handling in python/test.txt",'r')
# for a in f:
#     print(a)
# f.close()

# f1 = open("/Volumes/TROLLHUNTER/python Lab/Basic-Programs-in-python/file handling in python/testwrite.txt",'w')
# f1.write("pokemon world23\n")
# f1.writelines("ash ketchum is from palettown\n")
# f1.writelines("ash ketchum is from palettown\n")
# f1.writelines("ash ketchum is from palettown\n")
# f1.close
# f1 = open("/Volumes/TROLLHUNTER/python Lab/Basic-Programs-in-python/file handling in python/testwrite.txt",'r')
# for a in f1:
#     print(a)

f2 = open("/Volumes/TROLLHUNTER/python Lab/Basic-Programs-in-python/file handling in python/testwrite.txt",'a')
f2.write("the is the new line")
f2.close()
f2 = open("/Volumes/TROLLHUNTER/python Lab/Basic-Programs-in-python/file handling in python/testwrite.txt",'r')
for a in f2:
    print(a.split(' '))
j = f2.tell()
print(j)
a = f2.seek(7)
j = f2.tell()
print(j)