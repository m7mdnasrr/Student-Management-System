import ast


def login():
    try:
        with open("users.txt", "r") as f:
            data = f.read()
            users = ast.literal_eval(data) if data else {}
    except FileNotFoundError:
        users = {}

    print("LOGIN SYSTEM")
    choice = int(input("1. Login  2. Register\nEnter choice: "))
    match choice:
        case 1:
            username = input("Enter username: ")
            password = input("Enter password: ")
            if username in users and users[username] == password:
                print("Login successful!")
                return True
            else:
                print("Invalid username or password")
                return False

        case 2:
            username = input("Choose a username: ")
            password = input("Choose a password: ")
            users[username] = password
            with open("users.txt", "w") as f:
                f.write(str(users))
            print("User registered successfully")
            return login() 


def students_per_course(Student):
    course_count = {}
    for info in Student.values():
        for course in info["courses"]:
            course_count[course] = course_count.get(course, 0) + 1

    print("\nNumber of students in each course:")
    for course, count in course_count.items():
        print(f"{course}: {count}")



if not login():
    exit()

print("Welcome to the Student Management System")

try:
    with open("students.txt", "r") as f:
        data = f.read()
        Student = ast.literal_eval(data) if data else {}
except FileNotFoundError:
    Student = {}

while True:
    num = int(input(
        "\nEnter your choice:\n"
        " 1. Add Student\n"
        " 2. View Students\n"
        " 3. Search Student\n"
        " 4. Update Student\n"
        " 5. Delete Student\n"
        " 6. Students per Course\n"
        " 7. Save & Exit\n "
    ))

    match num:
        case 1:
            ID = int(input("Enter ID: "))
            name = input("Enter name: ")
            age = input("Enter age: ")
            courses = input("Enter courses separated by comma (,): ").split(",")
            Student[ID] = {
                "name": name,
                "age": age,
                "courses": [c.strip() for c in courses]
            }
            print("Student added successfully")

        case 2:
            for student_id, student_info in Student.items():
                print(f"\nStudent ID: {student_id}")
                print(f"Name: {student_info['name']}")
                print(f"Age: {student_info['age']}")
                print(f"Courses: {', '.join(student_info['courses'])}")

        case 3:
            ID = int(input("Enter ID: "))
            if ID in Student:
                print(f"Student ID: {ID}")
                print(f"Name: {Student[ID]['name']}")
                print(f"Age: {Student[ID]['age']}")
                print(f"Courses: {', '.join(Student[ID]['courses'])}")
            else:
                print("ID not found")

        case 4:
            ID = int(input("Enter ID: "))
            if ID in Student:
                print(f"Courses: {Student[ID]['courses']}")
                action = input("Add or remove a course? (a/r): ").lower()
                course = input("Enter course: ").strip()
                if action == 'a':
                    if course not in Student[ID]['courses']:
                        Student[ID]['courses'].append(course)
                elif action == 'r':
                    if course in Student[ID]['courses']:
                        Student[ID]['courses'].remove(course)
                    else:
                        print("Course not found")
                print(f"Updated courses: {Student[ID]['courses']}")
            else:
                print("ID not found")

        case 5:
            ID = int(input("Enter ID: "))
            if ID in Student:
                del Student[ID]
                print("Student deleted successfully")
            else:
                print("ID not found")

        case 6:
            students_per_course(Student)

        case 7:
            with open("students.txt", "w") as f:
                f.write(str(Student))
            print("Data saved to students.txt")
            break

        case _:
            print("Invalid choice. Please try again.")
