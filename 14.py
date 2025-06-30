# 14. Check if Digits Are in Increasing Order
#     Example: 1234 Yes, 132 No


num = input("Enter a number =>")
is_increasing = True

for i in range(len(num) - 1):
    if num[i] >= num[i + 1]:
        is_increasing = False
        break

if is_increasing:
    print("Yes (Digits are in increasing order)")
else:
    print("No (Digits are not in increasing order)")
