import json


class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street


class Student:
    row_id = 1

    def __init__(self, name, mark, address):
        self.name = name
        self.mark = mark
        self.address = address
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.mark >= 91:
            return "A"
        elif self.mark >= 81:
            return "B"
        elif self.mark >= 71:
            return "C"
        else:
            return "D"

    def to_dict(self):
        return {
            "row_id": self.row_id,
            "name": self.name,
            "mark": self.mark,
            "address": {"city": self.address.city, "street": self.address.street},
            "grade": self.grade,
        }

    @classmethod
    def from_dict(cls, data):
        address_data = data.pop("address")
        address = Address(city=address_data["city"], street=address_data["street"])
        return cls(address=address, **data)


# Create instances of Address
address1 = Address(city="Tbilisi", street="Saburtalo")
address2 = Address(city="Tbilisi", street="Gldani-7-11-4-93")
address3 = Address(city="Tbilisi", street="Leselidzs str. 25")
address4 = Address(city="Tbilisi", street="Varketili IV 407-5-123")

# Create instances of Student
students = [
    Student(name="Paata", mark=87, address=address1),
    Student(name="Demetre", mark=100, address=address2),
    Student(name="Alexander", mark=100, address=address2),
    Student(name="Teona", mark=92, address=address2),
    Student(name="Nino", mark=99, address=address3),
    Student(name="Andria", mark=87, address=address4),
]

# Save students to a file
with open("students.json", "w") as file:
    json.dump([student.to_dict() for student in students], file, indent=2)

# Read students from file
with open("students.json", "r") as file:
    students_data = json.load(file)

# Update data
students_data[0]["mark"] = 90

# Save updated data to a file
with open("students.json", "w") as file:
    json.dump(students_data, file, indent=2)
