#WAP to read a string and display the number of words starts with 'A' or 'a'
s=input("Enter a string:")
list_of_words=s.split()
number_of_words=0
for word in list_of_words:
    if word.startswith(('a','A'))==True:
        number_of_words+=1
print(f"There are {number_of_words} words starting with 'A' or 'a'")
        
        
