a=eval(input("Enter the series of numbers:"))

even_num=0
odd_num=0

for num in a:
    if num%2==0:
        even_num=even_num+1
    else:
        odd_num=odd_num+1

print("There are",even_num,"even numbers and",odd_num,"odd number") 
