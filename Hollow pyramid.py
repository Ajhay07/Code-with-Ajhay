r=int(input("Enter the rows:"))
for i in range(1,r):
    for j in range(1,r-i):
        print(" ", end='') 
    
    for j in range(2*i+1):
        if j==0 or j==2*i or i==r-1:
            print("*",end='')
        else:
            print(" ", end='')
    print()         
