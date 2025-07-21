
# student tracker project

def calculate_grade(mark):
    """Determines letter grade for given numeric mark."""
    if mark >= 90:
        return 'A'
    elif mark >= 80:
        return 'B'
    elif mark >= 70:
        return 'C'
    elif mark >= 60:
        return 'D'
    else:
        return 'F'

# Function to display summary of all students
def display_summary(records):
    """Prints each student's name, score, and letter grade. """
    print("\nStudent Summary:")
    for record in records:
        name, score, grade = record
        print(f"{name}: {score} -> {grade}")

# Function to save student records into a text file
def save_records(records):
    """Writes all student records to grades.txt file."""
    with open("grades.txt", "w") as file:
        for record in records:
            name, score, grade = record
            file.write(f"{name}: {score} -> {grade}\n")
 
 # Main Project--- Student Tracker

print("Welcome to the Student Grade Tracker!")
 
