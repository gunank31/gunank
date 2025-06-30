# 9. Palindrome Number Checker
#    Input: 1221
#    Output: Palindrome


number = input("Enter a number =>")

if number == number[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
