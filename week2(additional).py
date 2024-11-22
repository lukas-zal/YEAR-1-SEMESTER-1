def additional():
    a = int(input("Enter start point (a): "))
    b = int(input("Enter end point (b): "))
    c = int(input("Enter step (c): "))
    if c == 0:
        print("Step (c) cannot be 0.")
        return
    for num in range(a, b, c):
        print(num)
    num = num + c    
    if num == b:
        print(num)       
additional()
