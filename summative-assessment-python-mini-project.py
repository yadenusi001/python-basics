
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


# List to store student data as tuples
student_records = []

while True:
    # Input student name
    raw_name = input("Enter student name: ").strip()
    
    # Format name properly (capitalize first letters)
    formatted_name = ' '.join([word.capitalize() for word in raw_name.split()])
    
    # Input student score with validation
    while True:
        try:
            raw_score = input("Enter score (0-100): ").strip()
            numeric_score = float(raw_score)
            if 0 <= numeric_score <= 100:
                break
            else:
                print("❌ Score must be between 0 and 100.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")
    
    # Get letter grade
    letter = calculate_grade(numeric_score)
    
    # Add student record to list
    student_records.append((formatted_name, numeric_score, letter))
    
    # Ask user if they want to add another student
    another = input("Add another student? (yes/no): ").strip().lower()
    if another != 'yes':
        break

# After data entry is complete, display summary and save
display_summary(student_records)
save_records(student_records)
print("\n✅ Student data saved to grades.txt")