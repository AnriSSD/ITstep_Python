import csv
import os


def add_student_to_csv(file_path, student_data):
    file_exists = os.path.isfile(file_path)
    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["id", "name", "age", "grade", "subject_name", "marks"])
        writer.writerow(student_data)


def read_students_from_csv(file_path, student_id=None):
    students = []
    with open(file_path, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if student_id is None or int(row["id"]) == student_id:
                students.append(dict(row))
    return students


def update_student_score(file_path, student_id, subject_name, new_marks):
    updated_rows = []
    with open(file_path, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if int(row["id"]) == student_id and row["subject_name"] == subject_name:
                row["marks"] = new_marks
            updated_rows.append(row)

    with open(file_path, "w", newline="") as file:
        writer = csv.DictWriter(
            file, fieldnames=["id", "name", "age", "grade", "subject_name", "marks"]
        )
        writer.writeheader()
        writer.writerows(updated_rows)


# Example:

# Add new students
students_data = [
    [2, "Jane Smith", 21, "B", "Math", 85],
    [3, "Alice Johnson", 19, "A", "Physics", 92],
]
for student_data in students_data:
    add_student_to_csv("students.csv", student_data)

# Read all students
all_students = read_students_from_csv("students.csv")
print("All Students:")
print(all_students)

# Read a specific student
specific_student_id = 1
specific_student = read_students_from_csv(
    "students.csv", student_id=specific_student_id
)
print(f"\nStudent with ID {specific_student_id}:")
print(specific_student)

# Update a students score
update_student_score("students.csv", 1, "Math", 95)
updated_specific_student = read_students_from_csv("students.csv", student_id=1)
print(f"\nUpdated Student with ID {specific_student_id}:")
print(updated_specific_student)
