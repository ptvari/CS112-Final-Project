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
root.geometry("400x400")

#the option/combo box to display different courses and their data
#that the user wants to pick
selected_course = tk.StringVar()
selected_course.set("Math")
course_menu = tk.OptionMenu(root, selected_course, "Math", "Science", "English")
course_menu.pack()

#entry boxes for the name of assignment, score of it and points
entryName = tk.Entry(root)
entryScore = tk.Entry(root)
entryPoints = tk.Entry(root)

entryName.pack()
entryScore.pack()
entryPoints.pack()

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

tk.Button(root, text="Add Assignment", command=add_assignment_gui).pack()


output_label = tk.Label(root, text="", justify="left", anchor="w")
output_label.pack()


def show_assignments():
    course = get_selected_course()
    result = course.display_course_assignments()
    output_label.config(text=result)

tk.Button(root, text="Show Assignments", command=show_assignments).pack()

def show_grade():
    course = get_selected_course()
    result = course.display_course_grade()
    output_label.config(text=result)

tk.Button(root, text="Show Grade", command=show_grade).pack()

def clear_fields():
    entryName.delete(0, tk.END)
    entryScore.delete(0, tk.END)
    entryPoints.delete(0, tk.END)

tk.Button(root, text="Clear Fields", command=clear_fields).pack()

def save_data_gui():
    course = get_selected_course()
    course.save_data()

tk.Button(root, text="Save", command=save_data_gui).pack()
def load_data_gui():
    course = get_selected_course()
    message = course.load_data()

    if message:
        output_label.config(text=message)

tk.Button(root, text="Load", command=load_data_gui).pack()

tk.Button(root, text="Quit", command=root.quit).pack()



root.mainloop()