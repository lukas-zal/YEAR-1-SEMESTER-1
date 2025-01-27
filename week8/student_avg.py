from student_dict import students

for i in range(10,16):
    key = i
    if key in students:
        grades = students[key]['grades']
        avg = sum(grades) / len(grades)

        if avg < 40:
            print(f"Student Name: {students[key]['name']}")
            print(f"Student's Grade Average is: {avg:.2f}") # edo to {avg:.2f} den gnoriza pos allios mporo na to kano print

      


