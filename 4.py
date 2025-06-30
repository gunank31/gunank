# 4. Count the Number of Even Digits and Odd Digits
#    Input: 456123
#    Output: Even: 3, Odd: 3

number = input("Enter a number =>")
even_count = 0
odd_count = 0

for digit in number:
    if digit.isdigit():
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

print(f"Even =>{even_count}, Odd =>{odd_count}")
