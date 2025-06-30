# 11. Print Number Pyramid with Powers
#     Input: 3
#     Output:
#     1
#     1 2
#     1 2 3


n = int(input("Enter a number =>"))

for i in range(1, n + 1):
    for i in range(1, i + 1):

        # Number Pyramid 
        print(i, end=' ')

        # Number Pyramid with Powers
        print(i**i, end=' ')
    print()
