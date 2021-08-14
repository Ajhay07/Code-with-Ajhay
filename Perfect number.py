a=int(input("Enter the number:"))

if (a<=0):
    print("Negative numbers and zero are not perfect!")
    exit()

b=0

for x in range(1,a):
    if a%x==0:
        b=b+x

if a==b:
    print(a,"is a perfect number")
else:
    print(a,"is NOT a perfect number")

