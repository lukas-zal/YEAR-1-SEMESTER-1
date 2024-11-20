def additional():
    a = int(input("Enter start point (a): "))
    b = int(input("Enter end point (b): "))
    c = int(input("Enter step (c): "))
    if a > b and c > 0:
        c = -c  
    for num in range(a, b + 1 if c > 0 else b - 1, c):
        print(num, end=", ")
additional()
