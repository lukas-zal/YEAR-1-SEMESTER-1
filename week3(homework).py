import random
numbers = [random.randint(1, 100) for _ in range(20)]
even_amount = 0
for num in numbers:
    if num % 2 == 0:
        even_amount += 1
print("Random Numbers:", numbers)
print("Number of even numbers:", even_amount)
