word = input("please enter your word. ")
word = str(word)
reverse = word[::-1]
print(reverse)
if word == reverse:
    print("Word is a palindrome")
else:
    print("Word is not a palindrome")