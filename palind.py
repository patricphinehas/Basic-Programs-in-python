def strev(a):
    s = a[::-1]
    print(s)
    pali(a,s)

def pali(a,s):
    if(a==s):
        print("the given sequence is palindrome")
    else:
        print("the given string is not a plaindrome")

# the main function
a = str(input('enter the text for reversal palindrome check'))
print(a)
strev(a)