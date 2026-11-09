# Name: John
# File Name: student_gpa.py
# Description: This program accepts a student's name and GPA,
# determines if the student qualifies for the Dean's List
# or the Honor Roll, and continues processing records until
# the last name ZZZ is entered.

# Student GPA Program

last_name = input("Enter student's last name (ZZZ to quit): ")

while last_name != "ZZZ":
    first_name = input("Enter student's first name: ")
    gpa = float(input("Enter student's GPA: "))

    if gpa >= 3.5:
        print(first_name, last_name, "has made the Dean's List.")

    if gpa >= 3.25:
        print(first_name, last_name, "has made the Honor Roll.")

    print()

    last_name = input("Enter student's last name (ZZZ to quit): ")

print("Program ended.")
