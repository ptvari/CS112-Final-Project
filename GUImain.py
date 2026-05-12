"""
This is the GUI portion of the project that displays the
grade course tracker with a Windows XP style theme.
"""

# importing tkinter and the Course class
import tkinter as tk
from CourseClass import Course as cc
# ==========================================
# COURSE OBJECTS
# creates separate course instances
# ==========================================

math_course = cc("Math")
science_course = cc("Science")
english_course = cc("English")

courses = {
    "Math": math_course,
    "Science": science_course,
    "English": english_course
}


# ==========================================
# MAIN WINDOW
# creates the main GUI window
# ==========================================

root = tk.Tk()
root.title("Course Tracker")
root.geometry("500x600")
root.configure(bg="#d4d0c8")


# ==========================================
# TITLE BAR
# fake Windows XP style title section
# ==========================================

title_frame = tk.Frame(root, bg="#0a246a", height=40)
title_frame.pack(fill="x")

title_label = tk.Label(root, text="Course Grade Tracker", bg="#0a246a", fg="white", font=("Tahoma", 14, "bold"))
title_label.place(x=10, y=7)


# ==========================================
# MAIN FRAME
# holds all GUI widgets together
# ==========================================

main_frame = tk.Frame(root, bg="#d4d0c8", bd=2, relief="groove")
main_frame.pack(padx=15, pady=20, fill="both", expand=True)


# ==========================================
# COURSE DROPDOWN
# lets the user select a course
# ==========================================

selected_course = tk.StringVar()
selected_course.set("Math")

labelCourse = tk.Label(main_frame, text="Course:", bg="#d4d0c8", font=("Tahoma", 10))
labelCourse.grid(row=0, column=0, padx=10, pady=10, sticky="e")

course_menu = tk.OptionMenu(main_frame, selected_course, "Math", "Science", "English")
course_menu.config(font=("Tahoma", 9), bg="#d4d0c8", width=20)
course_menu.grid(row=0, column=1, padx=10, pady=10)


# ==========================================
# ENTRY BOXES
# allows the user to input assignment data
# ==========================================

labelName = tk.Label(main_frame, text="Assignment Name:", bg="#d4d0c8", font=("Tahoma", 10))
labelName.grid(row=1, column=0, padx=10, pady=10, sticky="e")

entryName = tk.Entry(main_frame, width=25, relief="sunken", bd=2, font=("Tahoma", 10))
entryName.grid(row=1, column=1, padx=10, pady=10)

labelScore = tk.Label(main_frame, text="Score Earned:", bg="#d4d0c8", font=("Tahoma", 10))
labelScore.grid(row=2, column=0, padx=10, pady=10, sticky="e")

entryScore = tk.Entry(main_frame, width=25, relief="sunken", bd=2, font=("Tahoma", 10))
entryScore.grid(row=2, column=1, padx=10, pady=10)

labelPoint = tk.Label(main_frame, text="Points Possible:", bg="#d4d0c8", font=("Tahoma", 10))
labelPoint.grid(row=3, column=0, padx=10, pady=10, sticky="e")

entryPoints = tk.Entry(main_frame, width=25, relief="sunken", bd=2, font=("Tahoma", 10))
entryPoints.grid(row=3, column=1, padx=10, pady=10)
# ==========================================
# FUNCTIONS
# handles button actions and GUI updates
# ==========================================

def get_selected_course():
    return courses[selected_course.get()]
def add_assignment_gui():

    course = get_selected_course()
    name = entryName.get()

    try:
        score = int(entryScore.get())
        points = int(entryPoints.get())

    except ValueError:
        output_label.config(text="Please enter valid numbers.")
        return

    course.add_assignment(name, score, points)

    output_label.config(text=f"Assignment '{name}' added.")
def show_assignments():

    course = get_selected_course()

    result = course.display_course_assignments()

    output_label.config(text=result)
def show_grade():

    course = get_selected_course()

    assignments = course.display_course_assignments()

    grade = course.display_course_grade()

    output_label.config(text=assignments + "\n\n----------------------\n" + grade)
def clear_fields():

    entryName.delete(0, tk.END)
    entryScore.delete(0, tk.END)
    entryPoints.delete(0, tk.END)

    output_label.config(text="Fields cleared.")
def save_data_gui():

    course = get_selected_course()

    course.save_data()

    output_label.config(text="Data saved successfully.")
def load_data_gui():

    course = get_selected_course()

    message = course.load_data()

    if message:
        output_label.config(text=message)

# ==========================================
# BUTTON SECTION
# contains all interactive buttons
# ==========================================

button_style = {"font": ("Tahoma", 9), "bg": "#d4d0c8", "relief": "raised", "bd": 2, "width": 18}

tk.Button(main_frame, text="Add Assignment", command=add_assignment_gui, **button_style).grid(row=4, column=0, padx=5, pady=5)

tk.Button(main_frame, text="Show Assignments", command=show_assignments, **button_style).grid(row=4, column=1, padx=5, pady=5)

tk.Button(main_frame, text="Show Grade", command=show_grade, **button_style).grid(row=5, column=0, padx=5, pady=5)

tk.Button(main_frame, text="Clear Fields", command=clear_fields, **button_style).grid(row=5, column=1, padx=5, pady=5)

tk.Button(main_frame, text="Load", command=load_data_gui, **button_style).grid(row=6, column=0, padx=5, pady=5)

tk.Button(main_frame, text="Save", command=save_data_gui, **button_style).grid(row=6, column=1, padx=5, pady=5)
# ==========================================
# OUTPUT SECTION
# displays assignments and grades
# ==========================================
output_frame = tk.Frame(main_frame, bg="white", bd=2, relief="sunken")
output_frame.grid(row=7, column=0, columnspan=2, padx=15, pady=20)

output_label = tk.Label(output_frame, text="Welcome to Course Tracker", justify="left", anchor="nw", bg="white", fg="black", font=("Courier New", 10), width=50, height=14, padx=10, pady=10)
output_label.pack()
# ==========================================
# EXIT BUTTON
# closes the application
# ==========================================
exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Tahoma", 9), bg="#d4d0c8", relief="raised", bd=2, width=15)
exit_button.pack(pady=10)
# ==========================================
# MAIN LOOP
# keeps the GUI running
# ==========================================

root.mainloop()