import random
 
LC_letters = "abcdefghijklmnopqrstuvwxyz"
UC_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "!@#$%^&*()" 


random_LC = random.choice(LC_letters) 
random_UC = random.choice(UC_letters) 
random_number = random.choice(numbers) 
random_symbol = random.choice(symbols)

password = [random_LC, random_UC, random_number, random_symbol]
for i in range(6):
    password.append(random.choice(LC_letters + UC_letters + numbers + symbols))
random.shuffle(password)

for char in password: 
    print(char, end="")
