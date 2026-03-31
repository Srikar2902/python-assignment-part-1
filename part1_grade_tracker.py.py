# ==========================================================
# Task 1: Cleaning Up the Messy Student Data
# ==========================================================
# Justification: Real-world data is often messy. I'm using .strip() to fix 
# accidental spaces and .title() to make sure names look professional.
# I'm also converting strings to integers so we can actually do math with them.

raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

cleaned_students = []

print("--- Task 1: Student Profile Cards ---")
for student in raw_students:
    # Fix the name formatting
    name = student["name"].strip().title()
    
    # Convert roll number to a number type
    roll = int(student["roll"])
    
    # Split the marks string and turn each piece into an integer
    marks = [int(m) for m in student["marks_str"].split(", ")]
    
    # Basic validation: check if name only contains letters
    is_valid = "✓ Valid name" if name.replace(" ", "").isalpha() else "✗ Invalid name"
    
    # Displaying the profile card with f-strings for clean alignment
    print("=" * 32)
    print(f"Student : {name}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")
    print("=" * 32)
    print(f"Status  : {is_valid}\n")
    
    cleaned_students.append((name, marks))

# Requirement: Show Roll 103 in different cases
print(f"Checking Roll 103... Upper: {'Priya Nair'.upper()} | Lower: {'Priya Nair'.lower()}\n")


# ==========================================================
# Task 2: Individual Marks Analysis
# ==========================================================
# Justification: Using a loop here allows us to categorize every subject 
# based on the grading scale. I used an if-elif ladder for the logic.

student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

print("--- Task 2: Ayesha's Subject Analysis ---")
for i in range(len(subjects)):
    m = marks[i]
    if m >= 90: grade = "A+"
    elif m >= 80: grade = "A"
    elif m >= 70: grade = "B"
    elif m >= 60: grade = "C"
    else: grade = "F"
    print(f"{subjects[i]:<10}: {m} ({grade})")

# Basic math for stats
avg_ayesha = sum(marks) / len(marks)
print(f"\nTotal Marks: {sum(marks)} | Average: {avg_ayesha:.2f}")

# Finding the best and worst subjects using index matching
print(f"Top Subject: {subjects[marks.index(max(marks))]} ({max(marks)})")
print(f"Lowest Subject: {subjects[marks.index(min(marks))]} ({min(marks)})")

# Interactive section: While loop for manual entries
print("\n--- Manual Entry Mode ---")
added = 0
while True:
    sub_input = input("Enter a new subject (or type 'done'): ").strip().lower()
    if sub_input == 'done':
        break
    
    # Justification: Added a try-except block to catch non-number errors 
    # so the program doesn't crash if the user makes a typo.
    try:
        m_val = int(input(f"Enter marks for {sub_input}: "))
        if 0 <= m_val <= 100:
            marks.append(m_val)
            added += 1
        else:
            print("Error: Marks must be between 0 and 100.")
    except ValueError:
        print("Error: Please enter a whole number.")

print(f"Update: {added} subjects added. New Class Average: {sum(marks)/len(marks):.2f}\n")


# ==========================================================
# Task 3: Class Performance Summary
# ==========================================================
# Justification: For the table, I used padding (:<18) to ensure 
# the columns stay straight regardless of name length.

class_data = [
    ("Ayesha Sharma", [88, 72, 95, 60, 78]),
    ("Rohit Verma",   [55, 68, 49, 72, 61]),
    ("Priya Nair",    [91, 85, 88, 94, 79]),
    ("Karan Mehta",   [40, 55, 38, 62, 50]),
    ("Sneha Pillai",  [75, 80, 70, 68, 85]),
]

print(f"{'Name':<18} | {'Average':<7} | {'Status'}")
print("-" * 40)

pass_count, fail_count = 0, 0
all_avgs = []
topper_name, topper_score = "", 0

for name, m_list in class_data:
    avg = sum(m_list) / len(m_list)
    status = "Pass" if avg >= 60 else "Fail"
    
    if status == "Pass": pass_count += 1
    else: fail_count += 1
    
    all_avgs.append(avg)
    if avg > topper_score:
        topper_score, topper_name = avg, name
        
    print(f"{name:<18} |  {avg:>5.2f}  | {status}")

print("-" * 40)
print(f"Summary: {pass_count} Passed, {fail_count} Failed.")
print(f"Topper: {topper_name} with {topper_score:.2f}")
print(f"Overall Class Average: {sum(all_avgs)/len(all_avgs):.2f}\n")


# ==========================================================
# Task 4: Essay String Manipulation
# ==========================================================
# Justification: String methods like .replace() and .split() make 
# text processing very efficient in Python.

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# Step 1: Clean the whitespace first
clean_essay = essay.strip()

print("--- Task 4: Essay Analysis ---")
print(f"Title Case version: {clean_essay.title()}")
print(f"Frequency of 'python': {clean_essay.lower().count('python')}")
print(f"Rebranded version: {clean_essay.replace('python', 'Python 🐍')}")

# Splitting and numbering sentences
sentence_list = clean_essay.split(". ")
print(f"Sentence List: {sentence_list}")

for num, text in enumerate(sentence_list, 1):
    # Ensure every sentence ends with a period for the final print
    final_text = text if text.endswith(".") else text + "."
    print(f"{num}. {final_text.strip().capitalize()}")