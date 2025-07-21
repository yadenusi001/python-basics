
# student grade tracker

# Define function: calculate_grade(score)
1. If score >= 90: Return 'A'
1. Else if score >= 80: Return 'B'
1. Else if score >= 70: Return 'C'
1. Else if score >= 60: Return 'D'
1. Else: Return 'F'

# Define function: display_summary(records)

1. Print “Student Summary:”
1. For each student record in records:
1. Print student name, score, and letter grade

# Define function: save_records(records)

1. Open file “grades.txt” for writing
1. For each student record in records:
1. Write student name, score, and letter grade to file
1. Close file

# Create empty list 
1. student_records to store all student data

# Student Entry  While Loop
1. Prompt user to enter student name
1. Prompt user to enter student score
1. Validate that score is between 0 and 100
1. If invalid, display error message and prompt again
1. Calculate student grade
1. Add student record to list
1. Ask user if they want to add another student
1. If yes, repeat loop
1. If no, exit loop

# Display All Student Data
Call display_summary(student_records)

# Save Data to File
Call save_records(student_records)

# Final message display
Display message: “Student data saved to grades.txt”

End program