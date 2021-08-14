n=int(input("Enter the number"))

sum_1=0

while (n>0):
    digit=n%10
    sum_1=sum_1+digit
    n=n//10
print("The sum of digits is",sum_1)
