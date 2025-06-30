# 12. Print All Prime Numbers from 1 to N
#     Input: 10
#     Output: 2 3 5 7


n = int(input("Enter a number =>"))

for num in range(2, n + 1):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')
