import math

PROGRAM_TITLE = "FINAL GRADE CALCULATOR"

#Create a headline of what the calculator will be used
def display_title():
    print("==================================================")
    print("            " + PROGRAM_TITLE)
    print("==================================================")

#Given by the user's score, check if the inputted variable is out of range or showcasing a non-numeric symbol/letter.
def get_valid_score(assessment_name, max_score):
    while True:
        try:
            user_input = input("Enter " + assessment_name + " (0-" + str(max_score) + "): ").strip()
            score = int(user_input)
            
            if score >= 0 and score <= max_score:
                return score
            else:
                print("Error: Score out of range! Try again.")
        except ValueError:
            print("Error: Please enter a valid whole number!")

#Compute the average of the Tests, including the FAs, LT/PT, and PP.
def compute_grade(fa1, fa2, fa3, fa4, fa5, lt, pt, pp):
    # Calculate individual percentages for each Machine Problem (FA)
    fa1_pct = (fa1 / 30) * 100
    fa2_pct = (fa2 / 30) * 100
    fa3_pct = (fa3 / 25) * 100
    fa4_pct = (fa4 / 30) * 100
    fa5_pct = (fa5 / 20) * 100
    
    # Average the individual percentages out of 100%
    fa_percent = (fa1_pct + fa2_pct + fa3_pct + fa4_pct + fa5_pct) / 5
    
    lt_percent = (lt / 50) * 100
    pt_percent = (pt / 60) * 100
    pp_percent = (pp / 100) * 100
    
    # Component weights applied strictly to individual component averages
    raw_grade = (fa_percent * 0.30) + (lt_percent * 0.30) + (pt_percent * 0.30) + (pp_percent * 0.10)
    final_grade = math.ceil(raw_grade)
    
    return fa_percent, lt_percent, pt_percent, pp_percent, raw_grade, final_grade


def get_rating(grade):
    if grade >= 96:
        return "EXCELLENT"
    elif grade >= 84:
        return "VERY GOOD"
    elif grade >= 72:
        return "GOOD"
    elif grade >= 60:
        return "SATISFACTORY"
    elif grade >= 50:
        return "FAIR"
    elif grade >= 40:
        return "FAILED ON CONDITION"
    else:
        return "FAILED"


def print_report(name, student_id, fa1, fa2, fa3, fa4, fa5, lt, pt, pp, raw_grade, rating):
    print("\n==================================================")
    print("            " + PROGRAM_TITLE)
    print("==================================================")
    print("Student Name: " + name)
    print("Student ID:   " + student_id)
    print("")
    print("Machine Problem 1: " + str(fa1) + "/30")
    print("Machine Problem 2: " + str(fa2) + "/30")
    print("Machine Problem 3: " + str(fa3) + "/25")
    print("Machine Problem 4: " + str(fa4) + "/30")
    print("Machine Problem 5: " + str(fa5) + "/20")
    print("Long Test 1: " + str(lt) + "/50")
    print("Long Test 2 / Practical Test: " + str(pt) + "/60")
    print("Initial Project Proposal: " + str(pp) + "/100")
    print("")
    print("Final Weighted Average: " + f"{raw_grade:.2f}%")
    print("Adjectival Rating: " + rating)
    print("==================================================")


# --- MAIN PROGRAM EXECUTION ---

display_title()

#Ask the user to input his/her student's name
name = input("Enter Student Name: ").strip()
while name == "":
    print("Error: Name cannot be blank!")
    name = input("Enter Student Name: ").strip()

#Ask the user to input the student's identity document (ID)
student_id = input("Enter Student ID (e.g., G8-1025): ").strip().upper()
while not (student_id.startswith("G8-") and len(student_id) == 7 and student_id[3:].isdigit()):
    print("Error: ID must follow pattern G8-#### (e.g., G8-1025).")
    student_id = input("Enter Student ID (e.g., G8-1025): ").strip().upper()

print("\n--- ENTER ASSESSMENT SCORES ---")

#Ask the user to input the given values of scores based on the student's performance and scores that is not exceeded to the maximum no. of items in the test
fa1 = get_valid_score("Machine Problem 1", 30)
fa2 = get_valid_score("Machine Problem 2", 30)
fa3 = get_valid_score("Machine Problem 3", 25)
fa4 = get_valid_score("Machine Problem 4", 30)
fa5 = get_valid_score("Machine Problem 5", 20)

lt = get_valid_score("Long Test 1", 50)
pt = get_valid_score("Long Test 2 / Practical Test", 60)
pp = get_valid_score("Initial Project Proposal", 100)

fa_pct, lt_pct, pt_pct, pp_pct, raw_grade, final_grade = compute_grade(fa1, fa2, fa3, fa4, fa5, lt, pt, pp)

rating = get_rating(final_grade)

print_report(name, student_id, fa1, fa2, fa3, fa4, fa5, lt, pt, pp, raw_grade, rating)
