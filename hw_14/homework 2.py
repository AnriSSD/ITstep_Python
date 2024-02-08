import json


def display_file(file_path):
    with open(file_path, "r") as file:
        print(file.read())


def read_file_contents(file_path):
    with open(file_path, "r") as file:
        return file.read()


def write_file_contents(file_path, new_contents):
    with open(file_path, "w") as file:
        json.dump(new_contents, file, indent=2)


def update_file_contents(file_path, new_contents):
    with open(file_path, "w") as file:
        file.write(json.dumps(new_contents))


def add_to_file(file_path, new_data):
    with open(file_path, "r+") as file:
        data = json.load(file)
        if isinstance(data, list):
            data.append(new_data)
            file.seek(0)
            json.dump(data, file, indent=2)
            file.truncate()
        else:
            raise ValueError("File doesn't contain a JSON list")


# Create file
file_path = "chess_players.json"
chess_players = [
    {"id": 19, "name": "Jobava", "country": "Georgia", "rating": 2588, "age": 41},
    {"id": 28, "name": "Caruana", "country": "USA", "rating": 2781, "age": 32},
    {"id": 35, "name": "Giri", "country": "Netherlands", "rating": 2771, "age": 30},
    {"id": 84, "name": "Carlsen", "country": "Norway", "rating": 2864, "age": 34},
    {"id": 118, "name": "Ding", "country": "China", "rating": 2799, "age": 32},
    {"id": 139, "name": "Karjakin", "country": "Russia", "rating": 2747, "age": 35},
    {"id": 258, "name": "Duda", "country": "Poland", "rating": 2731, "age": 31},
    {
        "id": 301,
        "name": "Vachier-Lagrave",
        "country": "France",
        "rating": 2737,
        "age": 34,
    },
    {"id": 403, "name": "Nakamura", "country": "USA", "rating": 2768, "age": 36},
]
write_file_contents(file_path, chess_players)

# Display fi;e
print("Отображение файла после создания:")
display_file(file_path)
print()

# Add new data in file
new_data = {
    "id": 568,
    "name": "Kasparov",
    "country": "Russia",
    "rating": 2705,
    "age": 56,
}
add_to_file(file_path, new_data)
new_data = {"id": 189, "name": "Karpov", "country": "Russia", "rating": 2698, "age": 59}
add_to_file(file_path, new_data)

# Display file after changes
print("Отображение файла после добавления новых данных:")
display_file(file_path)
