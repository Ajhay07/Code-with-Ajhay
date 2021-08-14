n=int(input("Enter any number:"))
rev=0
m=n
while n>0:
    d=n%10
    rev=rev*10+d
    n//=10
if m==rev:
    print("The given number is a palindrome")
else:
    print("The given number is not a palindrome")
