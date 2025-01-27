file = open('users.csv')
lines = file.readlines()

usernames = {}

for i in range(1, len(lines)):  
    line = lines[i]
    elements = line.split(',')

    if len(elements) > 1:
        username = elements[0].strip()  
        pin = elements[1].strip()  

        usernames[username] = pin

while True:
    u = input("Give username: ")

    if u == 'exit':
        print("Are you sure you want to exit? (Y/N)")
        yesorno = input().lower()

        if yesorno == 'y':
            print("Exiting")
            break
        elif yesorno == 'n':
            print("Please give username: ")
            continue
    elif u in usernames:
        p = input("Give password: ")
        if p == usernames[u]:
            print("Welcome!")   
            break 
        else:
            print("Wrong password...")
            print("Types [EXIT] if you want to quit...")
    else:
        print("Username not found")