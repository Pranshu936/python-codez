num=int(input("enter any number"))
temp=num
absnum=abs(num)
if(num>=0):
    rev=num%10
    num=num//10
    while(num>0):
        r=num % 10
        num=num // 10
        rev=rev*10+r
    print(rev)
else:
    rev=absnum%10
    absnum=absnum//10
    while(absnum>0):
        r=absnum % 10
        absnum=absnum // 10
        rev=rev*10+r
    print(rev-2*rev)

if(temp==rev):
    print("Palindrome")
else:
    print("not palindrome")


