# Constraint Satisfaction Problem (CSP)
# Timetable Scheduling using Backtracking

subjects = ["Maths", "Python", "DBMS", "AI"]
time_slots = ["9:00 AM", "11:00 AM", "2:00 PM"]
# Check constraints
def is_valid(subject, time, assignment):
    if subject == "Maths" and assignment.get("Python") == time:
        return False
    if subject == "Python" and assignment.get("Maths") == time:
        return False
    if subject == "DBMS" and assignment.get("AI") == time:
        return False
    if subject == "AI" and assignment.get("DBMS") == time:
        return False
    return True
def backtracking(assignment):
    if len(assignment) == len(subjects):
        return assignment
    subject = subjects[len(assignment)]
    for time in time_slots:
        if is_valid(subject, time, assignment):
            assignment[subject] = time
            result = backtracking(assignment)
            if result:
                return result
            del assignment[subject]

    return None
solution = backtracking({})
print("===== FINAL TIMETABLE =====")
for subject in subjects:
    print(subject, "->", solution[subject])


    #-----------------SHORT EXPLAINATION------------------

    #This program implements a Constraint Satisfaction Problem (CSP) for creating a timetable. 
    #The subjects Maths, Python, DBMS, and AI are treated as variables, while 9:00 AM, 11:00 AM, and 2:00 PM are their available time slots. 
    #The is_valid() function checks the constraints that Maths and Python cannot have the same time slot, and DBMS and AI cannot have the same time slot.
    #The backtracking() function assigns time slots to each subject and goes back to try another slot whenever a constraint is violated.
    #Finally, the program displays a valid timetable in which all the given constraints are satisfied.


