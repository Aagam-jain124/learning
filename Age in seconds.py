print("welcome to age into seconds calculator")
age = int(input("Please enter your age: "))
months = age * 12
days = months * 30
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

# Printing each item on a new line
print("Years:", age)
print("Months:", months)
print("Days ≈", days)
print("Hours ≈", hours)
print("Minutes ≈", minutes)
print("Seconds ≈", seconds)
