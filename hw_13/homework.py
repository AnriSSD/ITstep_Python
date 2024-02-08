def display_student_info(data):
    # Display the list of student IDs
    student_ids = [student["id"] for student in data["students"]]
    print("Student IDs:", ", ".join(str(id) for id in student_ids))

    # Ask the user to select a student ID
    selected_id = int(input("Enter the student ID: "))

    # Find the student with the selected ID
    selected_student = next(
        (student for student in data["students"] if student["id"] == selected_id), None
    )

    # If the student is found, display their information
    if selected_student:
        print("Student information:")
        print(
            f"ID: {selected_student['id']}, Name: {selected_student['name'].capitalize()}, Age: {selected_student['age']}"
        )

        # Display the grades for each subject
        for subject in data["subjects"]:
            grade = subject["grades"].get(str(selected_id))
            if grade is not None:
                print(f"Subject: {subject['name']}, Grade: {grade.upper()}")
            else:
                print(f"Subject: {subject['name']}, Grade: Not Available")
    else:
        print("Student not found")


# Test the function with the provided data
my_dict = {
    "students": [
        {"id": 20, "name": "giorgi", "age": 25},
        {"id": 25, "name": "giorgi", "age": 23},
        {"id": 100, "name": "nika", "age": 22},
        {"id": 56, "name": "nika", "age": 25},
        {"id": 1232, "name": "dato", "age": 22},
        {"id": 846723, "name": "archili", "age": 32},
    ],
    "subjects": [
        {
            "id": 1,
            "name": "Math",
            "grades": {
                "20": "B",
                "25": "A",
                "100": "A",
                "56": "B ",
                "1232": "C",
                "846723": "A",
            },
        },
        {
            "id": 2,
            "name": "Physics",
            "grades": {
                "20": "A",
                "25": "B",
                "100": "A",
                "56": "B ",
                "1232": "C",
                "846723": "B",
            },
        },
        {
            "id": 3,
            "name": "English",
            "grades": {
                "20": "A",
                "25": "A",
                "100": "A",
                "56": "A ",
                "1232": "B",
                "846723": "A",
            },
        },
        {
            "id": 4,
            "name": "Chemistry",
            "grades": {
                "20": "B",
                "25": "B",
                "100": "A",
                "56": "B ",
                "1232": "A",
                "846723": "A",
            },
        },
        {
            "id": 5,
            "name": "History",
            "grades": {
                "20": "C",
                "25": "B",
                "100": "A",
                "56": "B ",
                "1232": "A",
                "846723": "A",
            },
        },
    ],
}

display_student_info(my_dict)
