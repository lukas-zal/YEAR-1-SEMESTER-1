def diamond(n):
    if n % 2 == 0:
        print("Please enter an odd number.")
        return 
    for i in range(1, n + 1, 2):
        spaces = (n - i) // 2
        print(" " * spaces + "* " * i)
    for i in range(n - 2, 0, -2): 
        spaces = (n - i) // 2
        print(" " * spaces + "* " * i)
input = int(input("Enter the diamond length: "))

diamond(input)
