x=int(input("Enter x:"))
n=int(input("Enter n:"))
s=0
for a in range(n+1):
    if a % 2 == 0:
        s = s+ x ** a
    else:
        s = s -  x ** a

print("The sum of the series:", s)
