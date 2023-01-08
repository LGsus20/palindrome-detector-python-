#input the word to see if is a palindrome
str = "racecar"
str_lenght = len(str)
palindrome = False

#for loop checks if the word is a palindrome
for idx, a in enumerate(str):
    #reverse counter
    reverse_str = len(str) - idx -1
    if a == str[reverse_str]:
        palindrome = True
    else:
        palindrome = False
        break

if palindrome: x = "a palindrome"
else: x = "not a palindrome"

print("The word {1} is {0}".format(x, str))
