import random
from datetime import datetime, timedelta

# List of participant names
participants = [
    "AAGAM JAIN", "AARAV JAIN", "AARYAN BHARADWAJ", "ADITYA KESTWAL", "ADITYA MEHTA", 
    "ADYA SHARMA", "ANSH BAJPAI", "ANSHIKA PAL", "ANSUIYA", "ANUJ MISHRA", 
    "ARSH KHAN", "ATHARV GUPTA", "ATHARV SHARMA", "BHAVYA PAL", "BHAVYA SINGH", 
    "CHAHAT KAPOOR", "DAKSH", "DHANVI GUPTA", "DRISHTI", "GYAN ANAND", 
    "JAI GABA", "JISHAN SALMANI", "KARTIK GUPTA", "KUSH JAISWAL", "MILI DAS", 
    "MOHD. NAOMAN", "NAISHA SINGH", "NAMAN KANT", "POOJA MANOCHA", "PRADYOT", 
    "PRISHA GAUTAM", "PRISHA GUPTA", "RIA MENDIRATTA", "ROMIT SHARMA", "SAANVI KATPALIA", 
    "SAKSHI GUPTA", "SAMARTH RASTOGI", "SAMARTH SINGHAL", "SNEHAL VERMA", "TEJAAS RANA", 
    "TEJAS PAL", "VANSH KASHYAP", "VEDANT CHANDEL", "YASHVI ARORA", "ZIYA PARVEEN"
]

# Function to generate a random marriage record
def generate_marriage(marriage_id):
    husband = random.choice(participants)
    wife = random.choice(participants)
    # Ensure husband and wife are not the same person
    while wife == husband:
        wife = random.choice(participants)
    marriage_date = datetime(2000, 1, 1) + timedelta(days=random.randint(0, 9125))  # Random date from 2000 to 2025
    husband_age = random.randint(18, 100)
    wife_age = random.randint(18, 100)
    years_until_divorce = random.choice([0] + [random.randint(1, 50) for _ in range(4)])  # 20% chance of no divorce
    return f"({marriage_id}, '{husband}', '{wife}', '{marriage_date.strftime('%Y-%m-%d')}', {husband_age}, {wife_age}, {years_until_divorce})"

# Generate 100,000 marriage records
marriages = []
for i in range(1, 100001):
    marriages.append(generate_marriage(i))

# Combine all records into an SQL insert statement
insert_statement = (
    "INSERT INTO marriages (id, husband, wife, marriage_date, husband_age, wife_age, years_until_divorce) VALUES \n"
    + ",\n".join(marriages) + ";"
)

# Write the SQL query to a file
with open("marriages_insert.sql", "w") as file:
    file.write(insert_statement)

# Print a portion of the SQL statement (first 5 records) as an example
print("\n".join(insert_statement.splitlines()[:15]))
