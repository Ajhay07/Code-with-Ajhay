print("1.Triangle")
print("2.Square")
print("3.Rectangle")
print("4.Circle")
n=input("Enter the choice 1/2/3/4:")
if n=='1':
    a=float(input("Enter the 1st side:"))
    b=float(input("Enter the 2nd side:"))
    c=float(input("Enter the 3rd side:"))
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print("The Area of the triangle with sides", a, b, c, "is", round(area, 2))
elif n=='2':
    d=float(input("Enter the side:"))
    a2=d**2
    print("The Area of the Square with side",d,"is",a2)
elif n=='3':
    l=float(input("Enter the length:"))
    b=float(input("Enter the breadth:"))
    a3=l*b
    print("The Area of the Rectangle with length",l,"breadth",b,"is",a3)
elif n=='4':
    r=float(input("Enter the radius:"))
    a4=3.14*(r**2)
    print("The Area of the Circle with radius",r,"is",round(a4,2))
else:
    print("Invalid Input!!!")
