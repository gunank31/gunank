# 3. Check for a Special 2-Digit Number
#    Input: 59 5*9 + 5+9 = 45 + 14 = 59 True

def is_special_number(n):
    if 10 <= n <= 99:
        first_digit = n // 10
        second_digit = n % 10
        total = (first_digit * second_digit) + (first_digit + second_digit)
        return total == n
    else:
        return False

num = int(input("Enter a 2-digit number =>"))
if is_special_number(num):
    print("True (It's a special number)")
else:
    print("False (Not a special number)")
