# 6. Find the Largest Digit in a Number
#    Input: 98342
#    Output: 9


number = input("Enter a number =>")

max_digit = 0
for digit in number:
    if digit.isdigit():
        if int(digit) > max_digit:
            max_digit = int(digit)

print("Largest digit =>", max_digit)
