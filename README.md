#  Prelim Grade Calculator (Python Command Line Program)

Computation of Grades in Python in Partial Fulfillment for the Course Subject **BSIT 2206L - Integrated Programming and Technologies - Lec and Lab (9316-AY225)**. This project demonstrates adherence to **programming ethics**, **robust input validation**, and **data persistence**.

![Language](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
---
**Python Command Line Program** that computes a student’s Prelim Grade using the grading system below

**Grading System:**

**Class Standing (70%)**
* Attendance grade = Attendance × 10%
* Assignment grade = Assignment × 10%
* Quiz grade = (Average of Quizzes) × 50%
* Project grade = Project × 30%

Class Standing Grade = (Attendance grade + Assignment grade + Quiz grade + Project grade) × 70%

**Major Exam (30%)**
Prelim Grade (Exam Component) = Prelim Exam × 30%

**Final Prelim Grade**  
Final Prelim Grade = Class Standing Grade + Prelim Grade (Exam Component)
    

## 🚀 Key Features

This application exceeds standard requirements by implementing advanced reliability and usability features:

### 1. 🛡️ Robust & Ethical Input Handling
* **Crash Prevention:** Implements `try-except` blocks and `while` loops to handle non-numeric inputs gracefully.
* **Data Integrity:** Prevents negative numbers and ensures valid grading logic.

### 2. 🔄 Improved User Experience (UX)
* **Continuous Operation:** Includes a `while` loop mechanism allowing the user to process multiple students in a single session without restarting the script.
* **Visual Feedback:** Provides immediate grading remarks (**PASSED** or **FAILED**) based on the computed average.

### 3. 💾 Data Persistence (File I/O)
* **Automated Logging:** Automatically appends every calculation result to a local `class_records.txt` file, ensuring no data is lost after the program closes.

---

## ⚙️ Technical Implementation (Rubric Alignment)

| Component | Implementation Detail |
| :--- | :--- |
| **Functions** | Modular architecture using `calculate_quizzes()`, `get_valid_float()`, and `save_to_file()` for maintainability. |
| **Computation** | Strict adherence to the `(Class Standing * 70%) + (Exam * 30%)` formula. |
| **Formatting** | Clean, formatted console output with distinct sections for readability. |
| **Ethics** | Source code includes standard metadata (`__author__`, `__license__`) and attribution. |
--- 

## 📋 Prerequisites
* Python 3.6 or higher
* Git (optional, if cloning the repository).

### 1. Installation
**Option A: Clone Repository (Recommended)**
```bash
git clone https://github.com/jhanerose/python-prelim-grade-calculator.git
cd python-prelim-grade-calculator
```
**Option B: Direct Download**
1. Download the jhane_rose_sadicon_midterm.py file.
2. Open your terminal or command prompt.
3. Navigate to the folder where you saved the file:
```bash
cd path/to/your/folder
```
### 2. Running the program
Once you are in the correct directory, run the script using Python:
```bash
python "jhane rose_sadicon_midterm.py"
```
(Note: If ```python``` doesn't work, try using ```python3``` or ```py```)

---

## 📊 Sample User Input Output
```
======================================================================
SUBJECT: BSIT 2206L - Integrated Programming and Technologies
SECTION: 9316-AY225 | PROFESSOR: Homer T. Favenir
----------------------------------------------------------------------
AUTHOR: Jhane Rose Sadicon (BSIT-GD, 2nd Year)
COPYRIGHT: Copyright 2026, Computation of Grades in Python
LICENSE: MIT
======================================================================
PRELIM GRADES
******************************
******************************
Computing for (Student Name): Jhane Rose Sadicon
Enter attendance: 100
Attendance Grade is (10%): 10.0
Enter Number of Quizzes: 3
Enter Quiz 1 : 100
Enter Quiz 2 : 98
Enter Quiz 3 : 100
Quizzes Average is (50%): 49.7
Enter Assignment grade: 100
Assignment Average is (10%): 10.0
Enter Project grade: 100
Project Average is (30%): 30.0
Class Performance is (70%): 69.8
Enter Prelim grade: 100
Prelim Average is (30%): 30.0

******************************
Total Average is: 99.8
Remark: PASSED
******************************
   [System] Record successfully saved to class_records.txt

Calculate for another student? (y/n):
``` 
---

## 📜 License

This project is open-source and available under the **MIT License**.    
Copyright © 2026 Jhane Rose Sadicon.
