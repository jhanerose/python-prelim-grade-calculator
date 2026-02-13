"""
Program Name: Prelim Grade Calculator (Midterm Lab)
Filename: jhane_rose_sadicon_midterm.py
Description: A CLI program to compute a student's Prelim Grade based on Class Standing 
             and Exam components. Includes Loop, Remarks, and File Saving.
             
Subject: BSIT 2206L Integrated Programming and Technologies - Lec and Lab (9316-AY225)
Professor: Homer T. Favenir
"""

# --- Ethical Coding: Standard Metadata ---
__author__ = "Jhane Rose Sadicon"
__email__ = "jhanerose.sadicon@perpetual.edu"
__copyright__ = "Copyright 2026, Computation of Grades in Python"
__credits__ = ["Homer T. Favenir"]
__license__ = "MIT"
__version__ = "1.2.0" # Version updated for new features


def print_program_header():
    """
    Displays the program details, ethical notice, and student info.
    """
    print("=" * 70)
    print(f"SUBJECT: BSIT 2206L - Integrated Programming and Technologies")
    print(f"SECTION: 9316-AY225 | PROFESSOR: Homer T. Favenir")
    print("-" * 70)
    print(f"AUTHOR: {__author__} (BSIT-GD, 2nd Year)")
    print(f"COPYRIGHT: {__copyright__}")
    print(f"LICENSE: {__license__}")
    print("=" * 70)
    print("\n")

def get_valid_float(prompt):
    """
    Ethical Feature: Reliability.
    Ensures the user inputs a valid number.
    """
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("   [Error] Grade cannot be negative. Please try again.")
            else:
                return value
        except ValueError:
            print("   [Error] Invalid input. Please enter a number (e.g., 90 or 85.5).")

def get_weighted_score(score, weight):
    """
    Calculates the weighted portion of a grade.
    """
    return score * weight

def calculate_quizzes():
    """
    Handles the input and calculation for the Quiz component.
    """
    while True:
        try:
            num_quizzes = int(input("Enter Number of Quizzes: "))
            if num_quizzes < 0:
                print("   [Error] Number cannot be negative.")
                continue
            break
        except ValueError:
            print("   [Error] Please enter a whole number.")

    if num_quizzes == 0:
        return 0.0

    total_score = 0
    for i in range(num_quizzes):
        score = get_valid_float(f"Enter Quiz {i+1} : ")
        total_score += score

    average = total_score / num_quizzes
    weighted_score = get_weighted_score(average, 0.50)
    
    print(f"Quizzes Average is (50%): {weighted_score:.1f}")
    return weighted_score

def get_remarks(grade):
    """
    New Feature: Returns a Pass/Fail remark based on the grade.
    """
    if grade >= 75.0:
        return "PASSED"
    else:
        return "FAILED"

def save_to_file(name, grade, remark):
    """
    New Feature: Saves the result to 'class_records.txt'.
    Demonstrates File I/O (Input/Output).
    """
    try:
        # 'a' mode opens the file to Append (add to the end) instead of overwriting
        with open("class_records.txt", "a") as file:
            file.write(f"Student: {name} | Grade: {grade:.1f} | Status: {remark}\n")
        print("   [System] Record successfully saved to class_records.txt")
    except Exception as e:
        print(f"   [Error] Could not save file: {e}")

def main():
    """
    Main execution function with Loop.
    """
    print_program_header()

    while True:
        print("PRELIM GRADES")
        print("*" * 30)
        print("*" * 30)

        # 1. Inputs
        student_name = input("Computing for (Student Name): ")

        # 2. Computations
        attendance = get_valid_float("Enter attendance: ")
        attendance_grade = get_weighted_score(attendance, 0.10)
        print(f"Attendance Grade is (10%): {attendance_grade:.1f}")

        quiz_grade = calculate_quizzes()

        assignment = get_valid_float("Enter Assignment grade: ")
        assignment_grade = get_weighted_score(assignment, 0.10)
        print(f"Assignment Average is (10%): {assignment_grade:.1f}")

        project = get_valid_float("Enter Project grade: ")
        project_grade = get_weighted_score(project, 0.30)
        print(f"Project Average is (30%): {project_grade:.1f}")

        # Class Standing (70%)
        base_class_standing = attendance_grade + quiz_grade + assignment_grade + project_grade
        final_class_standing = base_class_standing * 0.70
        print(f"Class Performance is (70%): {final_class_standing:.1f}")

        # Exam (30%)
        prelim_exam = get_valid_float("Enter Prelim grade: ")
        prelim_exam_component = get_weighted_score(prelim_exam, 0.30)
        print(f"Prelim Average is (30%): {prelim_exam_component:.1f}")

        # Final Grade
        final_grade = final_class_standing + prelim_exam_component
        
        # Determine Remark
        remark = get_remarks(final_grade)

        # 3. Output
        print("\n" + "*" * 30)
        print(f"Total Average is: {final_grade:.1f}")
        print(f"Remark: {remark}")
        print("*" * 30)
        
        # 4. Save to File
        save_to_file(student_name, final_grade, remark)

        # 5. Loop Control (Ask to continue)
        print("\n")
        choice = input("Calculate for another student? (y/n): ").lower()
        if choice != 'y':
            print("Exiting program. Goodbye!")
            break # Breaks the while loop and ends the program
        
        print("\n" + "="*30 + "\n") # Divider for next student

if __name__ == "__main__":
    main()