s=input("Enter a string:")
list_of_words=s.split()
word_length=0
longest_word=''

for word in list_of_words:
    length=len(word)
    if length>word_length:
        word_length=length
        longest_word=word
print(f"The longest word is {longest_word}, which consists of {word_length},charecters")
