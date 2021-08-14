num=int(input("Enter the number:"))
x=num
s=0
while (x>0):
    digit=x%10
    s=s+digit**3
    x=x//10

if num==s:
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")
