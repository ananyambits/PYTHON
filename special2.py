start = int(input("Enter the starting range: "))
end = int(input("Enter the ending range: "))


for num in range(start, end + 1):
    if 1000 <= num <= 9999:
        root = int(num ** 0.5)

        if root * root == num:
           

            if all(int(digit) % 2 == 0 for digit in str(num)):
                print(num)

