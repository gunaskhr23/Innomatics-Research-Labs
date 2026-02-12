# Assignment Tasks Solution
 
# 1. User Login Check

# stored credentials
username = "admin"
password = "1234"

# taking input from user
entered_username = input("Enter username: ").strip()
entered_password = input("Enter password: ").strip()

# checking login
if entered_username == username and entered_password == password:
    print("Login Successful")
else:
    print("Invalid Credentials")

# 2. Pass / Fail Analyzer

marks = [45, 78, 90, 33, 60]

pass_count = 0
fail_count = 0

# checking each student's marks
for mark in marks:
    if mark >= 50:
        pass_count += 1
    else:
        fail_count += 1

print("\nPass / Fail Report")
print("Total Passed Students:", pass_count)
print("Total Failed Students:", fail_count)

# 3. Simple Data Cleaner

names = [" Alice ", "bob", " CHARLIE "]

cleaned_names = []

# cleaning names
for name in names:
    clean = name.strip().lower()
    cleaned_names.append(clean)

print("\nCleaned Names List:")
print(cleaned_names)

# 4. Message Length Analyzer

messages = ["Hi", "Welcome to the platform", "OK"]

print("\nMessage Length Analysis")

for message in messages:
    length = len(message)

    print("Message:", message)
    print("Length:", length)

    # check long messages
    if length > 10:
        print("This message is longer than 10 characters.")

    print()

# 5. Error Message Detector

logs = ["INFO", "ERROR", "WARNING", "ERROR"]

error_count = 0

# counting errors
for log in logs:
    if log == "ERROR":
        error_count += 1

print("Total ERROR messages:", error_count)
