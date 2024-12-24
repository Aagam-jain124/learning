file_path = "output.txt"

while True:
    info = []

    name = input("name: ")
    info.append("name - " + name)

    claes = input("class: ")
    info.append("class - " + claes)

    pcode = input("pin code: ")
    info.append("pin code - " + pcode)

    percent = input("overall percentage: ")
    info.append("overall percentage - " + percent)

    # Open the file in append mode ('a') to add each set of information without overwriting
    with open(file_path, 'a') as file:
        # Write each item in the 'info' list to the file
        for item in info:
            file.write(item + "\n")
        # Add an extra newline character to separate entries
        file.write("\n")

    print("Set of information saved to", file_path)

    another_entry = input("Do you want to enter another set of information? (y/n): ").lower()
    if another_entry != 'y':
        break
