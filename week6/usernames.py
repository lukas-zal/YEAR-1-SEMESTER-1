students = ['John Doe', 'Mary Smith', 'Andrew Green', 'Lisa Tomas', 'Mike Smith', 'Alex Green']
usernames = []
username_count = {}

for student in students:
    name = student.split()[0][0].lower() # edo den gnoriza pos mporeis na kaneis split kai na epileklseis sugkekrimena me parentheseis kai boithithika apo chatgpt
    surname = student.split()[1].lower()
    username = name + surname

    if username in username_count:
        username_count[username] += 1
    else:
        username_count[username] = 0
    usernames.append(username)      

print(usernames)
