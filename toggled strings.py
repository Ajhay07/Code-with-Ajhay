s=input("Enter a string:")
s1=""
for ch in s:
    if ch.islower():
        s1=s1+ch.upper()
    elif  ch.isupper():
        s1=s1+ch.lower()
    else:
        s1=s1+ch
print("The Original string:",s)
print("The Toppled string:",s1)
