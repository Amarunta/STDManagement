# Dictionary to store student records
student_records = {}
# counter used to name every unique student record
id_counter = -1


def add_student(name, age, grade, subjects):
    """
    Add a new student record.
    Args:
    - id_number (int): The identification number of the student. This argument is automatically configured by the id_counter.
    - name (str): The name of the student.
    - age (int): The age of the student.
    - grade (float): The grade of the student.
    - subjects (list of str): The subjects the student is enrolled in.
    """
    global id_counter
    id_counter += 1
    # Code to add a new student record
    id_number = id_counter
    student = {
        "id": id_number,
        "name": name,
        "age": age,
        "grade": grade,
        "subjects": subjects
    }
    student_records.update({id_number: student})


def update_student(id_num):
    """
    Update an existing student record.
    Args:
    - id_num (int): The identification number of the student whose record is to be updated.
    """
    # Check if the student exists
    # Prompt the user to update fields and keep current values if fields are empty
    # Code to update the student's record

    if id_num in student_records:
        while True:
            print(student_records[id_num])
            command = input("Which field would you like to update? ")
            if command == "name":
                student_records[id_num]["name"] = input()
            elif command == "age":
                student_records[id_num]["age"] = int(input())
            elif command == "grade":
                student_records[id_num]["grade"] = float(input())
            elif command == "subjects":
                student_records[id_num]["subjects"] = input().split(", ")
            elif command == "id":
                print("You can't change the ID-number. Try something else.")
                continue
            elif command == "Done":
                main()
            else:
                print("This field does not exist. Try again.")
                continue
            print("Type \"Done\" once you've finished updating your record.")
    else:
        command = input("This student record does not exist. Would you like to add a new record? (y/n) ")
        if command == "y":
            # Prompt for student details
            name = input("Enter student's name: ")
            age = int(input("Enter student's age: "))
            grade = float(input("Enter student's grade: "))
            subjects = input("Enter student's subjects (comma-separated): ").split(',')
            # Call the add_student function
            add_student(name, age, grade, subjects)
        elif command == "n":
            main()


def delete_student(id_num):
    """
    Delete a student record based on the student's identification number.
    Args:
    - id_num (int): The identification number of the student is needed in order to delete the record.
    """
    # Check if the student exists
    # Code to delete the student's record
    if id_num in student_records:
        print(student_records[id_num])
        print("Are you sure you would like to delete this record? You cannot undo this action. (Yes/No)")
        command = input()
        if command == "Yes":
            del student_records[id_num]
        elif command == "No":
            main()
        else:
            print("Try again.")
    else:
        print("The student record you're looking for doesn't exist.")


def search_student(id_num):
    """
    Search for a student by identification number and return their record.
    Args:
    - id_num (int): The identification number of the student to search for.
    """
    # Check if the student exists
    # Code to return the student's record
    if id_num in student_records:
        print(student_records[id_num])


def list_all_students():
    """
    List all student records.
    """
    # Check if there are any student records
    # Code to list all students

    if not student_records:
        print("There are no student records. Would you like to return to the main menu?")
        choice = input("Yes/No: ")
        if choice == "Yes":
            main()
        elif choice == "No":
            exit()
    else:
        for key, value in student_records.items():
            print(f"{key}: {value}")


def main():
    """
    Main function to provide user interaction.
    """
    while True:
        # Display menu options
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. List All Students")
        print("6. Exit")

        # Prompt user for their choice
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for student details
            name = input("Enter student's name: ")
            age = int(input("Enter student's age: "))
            grade = float(input("Enter student's grade: "))
            subjects = input("Enter student's subjects (comma-separated): ").split(',')
            # Call the add_student function
            add_student(name, age, grade, subjects)
        elif choice == '2':
            # Prompt for student identification number to update
            id_number = int(input("Enter student's ID to update: "))
            # Call the update_student function
            update_student(id_number)
        elif choice == '3':
            # Prompt for student identification number to delete
            id_number = int(input("Enter student's identification number to delete: "))
            # Call the delete_student function
            delete_student(id_number)
        elif choice == '4':
            # Prompt for student identification number to search
            id_number = int(input("Enter student's identification number to search: "))
            # Call the search_student function
            search_student(id_number)
        elif choice == '5':
            # Call the list_all_students function
            list_all_students()
        elif choice == '6':
            # Exit the program
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
