"""
This is the GUI portion of the project that displays the
grade course tracker
"""

#first importing the basics and my class from my other file
import tkinter as tk
from CourseClass import Course as cc



#used to take the courses that I want to display on gui
#create different instances with their own data
math_course = cc("Math")
science_course = cc("Science")
english_course = cc("English")

#connects the instance with the dropdown menu
#to be able to return the correct data
courses = {
    "Math": math_course,
    "Science": science_course,
    "English": english_course
}

#main root and root window
root= tk.Tk()
root.title("Course Tracker")
root.geometry("300x500")
root.grid_columnconfigure(0, weight=0)
root.grid_columnconfigure(1, weight=0)

#the option/combo box to display different courses and their data
#that the user wants to pick
selected_course = tk.StringVar()
selected_course.set("Math")
course_menu = tk.OptionMenu(root, selected_course, "Math", "Science", "English")
course_menu.grid(row=0, column=1, padx=5, pady=5)

#entry boxes for the name of assignment, score of it and points
entryName = tk.Entry(root)
entryScore = tk.Entry(root)
entryPoints = tk.Entry(root)

entryName.grid(row=1, column=1, padx=5, pady=5)
entryScore.grid(row=2, column=1, padx=5, pady=5)
entryPoints.grid(row=3, column=1, padx=5, pady=5)

#labels and their positions
labelCourse= tk.Label(root,text="Course")
labelCourse.grid(row=0, column=0, padx=5, pady=5, sticky="w")
labelName= tk.Label(root, text="Assignment Name")
labelName.grid(row=1, column=0, padx=5, pady=5, sticky="w")
labelScore= tk.Label(root, text="Score Earned")
labelScore.grid(row=2, column=0, padx=5, pady=5, sticky="w")
labelPoint=tk.Label(root, text="Points Possible")
labelPoint.grid(row=3, column=0, padx=5, pady=5, sticky="w")

#grab the selected course assignments from option box
def get_selected_course():
    return courses[selected_course.get()]

#grabs the assignment that the user inputs and adds it to the list
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


output_label = tk.Label(
    root,
    text="",
    justify="left",
    anchor="w",
    font=("Courier New", 10)
)

output_label.grid(row=8, column=0, columnspan=2, padx=10, pady=10, sticky="w")


def show_assignments():
    course = get_selected_course()
    result = course.display_course_assignments()
    output_label.config(text=result)


def show_grade():
    course = get_selected_course()

    current_text = output_label.cget("text")

    grade_text = course.display_course_grade()

    output_label.config(text=current_text + "\n" + grade_text)

def clear_fields():
    entryName.delete(0, tk.END)
    entryScore.delete(0, tk.END)
    entryPoints.delete(0, tk.END)

def save_data_gui():
    course = get_selected_course()
    course.save_data()

def load_data_gui():
    course = get_selected_course()
    message = course.load_data()

    if message:
        output_label.config(text=message)


#the buttons and their layouts
tk.Button(root, text="Add Assignment", command=add_assignment_gui).grid(row=4, column=0, pady=5)

tk.Button(root, text="Show Assignments", command=show_assignments).grid(row=4, column=1, pady=5)

tk.Button(root, text="Show Grade", command=show_grade).grid(row=5, column=0, pady=5)

tk.Button(root, text="Clear Fields", command=clear_fields).grid(row=5, column=1, pady=5)

tk.Button(root, text="Load", command=load_data_gui).grid(row=6, column=0, pady=5)

tk.Button(root, text="Save", command=save_data_gui).grid(row=6, column=1, pady=5)

tk.Button(root, text="Quit", command=root.quit).grid(row=7, column=0, columnspan=2, pady=10)


root.mainloop()