marks = {
    "Tia": 100,
    "Divyansh": 56,
    "Akash": 23,
    0: "Tia"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Tia": 99, "Renuka": 100})
# print(marks)

print(marks.get("Tia2")) # Prints None
print(marks["Tia2"]) # Returns an error