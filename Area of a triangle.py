a=float(input("Enter the 1st side:"))
b=float(input("Enter the 2nd side:"))
c=float(input("Enter the 3rd side:"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("The Area of the triangle with sides",a,b,c,"is",round(area,2))