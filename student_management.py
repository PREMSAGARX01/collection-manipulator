# Student Management System
# Uses list, tuple, set, dictionary, type casting and del

students = []
all_subjects = set()


def rebuild_subjects():
    global all_subjects
    all_subjects = set()
    for student in students:
        all_subjects.update(student["subjects"])


def add_student():
    print("\n--- Add Student ---")

    sid = input("Enter student id: ")

    for student in students:
        if student["details"][0] == sid:
            print("This student id already exists.")
            return

    name = input("Enter name: ")

    while True:
        try:
            age = int(input("Enter age: "))
            break
        except ValueError:
            print("Age must be a number.")

    grade = input("Enter grade: ")
    dob = input("Enter date of birth: ")

    subjects_input = input("Enter subjects (comma separated): ")
    subjects = [s.strip() for s in subjects_input.split(",") if s.strip() != ""]

    details = (sid, dob)

    student = {
        "details": details,
        "name": name,
        "age": age,
        "grade": grade,
        "subjects": subjects
    }

    students.append(student)
    all_subjects.update(subjects)

    print("Student added successfully.")


def show_students():
    print("\n--- All Students ---")

    if len(students) == 0:
        print("No student records found.")
        return

    for student in students:
        sid, dob = student["details"]
        print("ID:", sid)
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Grade:", student["grade"])
        print("DOB:", dob)
        print("Subjects:", ", ".join(student["subjects"]))
        print("--------------------")


def update_student():
    print("\n--- Update Student ---")
    sid = input("Enter student id to update: ")

    for student in students:
        curr_id, dob = student["details"]

        if curr_id == sid:
            print("Press enter to keep the old value.")

            new_name = input("Enter new name: ")
            new_age = input("Enter new age: ")
            new_grade = input("Enter new grade: ")
            new_subjects = input("Enter new subjects (comma separated): ")

            if new_name != "":
                student["name"] = new_name

            if new_age != "":
                try:
                    student["age"] = int(new_age)
                except ValueError:
                    print("Age not changed.")

            if new_grade != "":
                student["grade"] = new_grade

            if new_subjects != "":
                subjects = [s.strip() for s in new_subjects.split(",") if s.strip() != ""]
                student["subjects"] = subjects

            rebuild_subjects()
            print("Student updated successfully.")
            return

    print("Student not found.")


def delete_student():
    print("\n--- Delete Student ---")
    sid = input("Enter student id to delete: ")

    for i in range(len(students)):
        curr_id, dob = students[i]["details"]

        if curr_id == sid:
            del students[i]
            rebuild_subjects()
            print("Student deleted successfully.")
            return

    print("Student not found.")


def show_subjects():
    print("\n--- Subjects ---")

    if len(all_subjects) == 0:
        print("No subjects found.")
        return

    for subject in sorted(all_subjects):
        print(subject)


while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Show Subjects")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        show_subjects()
    elif choice == "6":
        print("Exiting program.")
        break
    else:
        print("Invalid choice.")
