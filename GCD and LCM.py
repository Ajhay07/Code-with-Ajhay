m=int(input("Enter the first number:"))
n=int(input("Enter the second number:"))
if n>m:
    m,n=n,m
for a in range(1,n+1):
    if m%a==0 and n%a==0:
        gcd=a
print("Greatest Common Divisor:",gcd)
lcm=(m*n)/gcd
print("Least Common Multiple:",lcm)
