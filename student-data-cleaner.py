student = [
    "AWeshahA",
    "AOmarA",
    "AAzzamA",
    10,
    "ASaraA",
    "AMohammedA",
    20,
    "AAmalA"
]

# List to store the cleaned student names
new_list = []


# Return None for unwanted integer values
def clean_student(a):
    if isinstance(a, int):
        return None
    return a


# Clean the original list and store valid values
for i in student:
    cleaned = clean_student(i)

    if cleaned is None:
        continue

    new_list.append(cleaned)


print(new_list)


# Remove the first and last character from each name
map_stu = list(map(lambda i: i[1:-1], new_list))
print(map_stu)


# Keep names with more than 5 characters
filter_stu = list(filter(lambda i: len(i) > 5, map_stu))
print(filter_stu)
