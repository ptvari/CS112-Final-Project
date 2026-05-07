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
root.geometry("500x400")

#the option/combo box to display different courses and their data
#that the user wants to pick
selected_course = tk.StringVar()
selected_course.set("Math")
course_menu = tk.OptionMenu(root, selected_course, "Math", "Science", "English")
course_menu.grid(column=8)

#entry boxes for the name of assignment, score of it and points
entryName = tk.Entry(root)
entryScore = tk.Entry(root)
entryPoints = tk.Entry(root)

entryName.grid(column=8)
entryScore.grid(column=8)
entryPoints.grid(column=8)

labelCourse= tk.Label(root,text="Course")
labelCourse.grid(row=0)
labelName= tk.Label(root, text="Assignment Name")
labelName.grid(row=1)
labelScore= tk.Label(root, text="Score Earned")
labelScore.grid(row=2)
labelPoint=tk.Label(root, text="Points Possible")
labelPoint.grid(row=3)

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

tk.Button(root, text="Add Assignment", command=add_assignment_gui).grid(row=5)


output_label = tk.Label(root, text="", justify="left", anchor="w")
output_label.grid(row=9)


def show_assignments():
    course = get_selected_course()
    result = course.display_course_assignments()
    output_label = tk.Label(root, text="", justify="left", anchor="w", wraplength=350)
    output_label.grid(row=9)
    print(result)

tk.Button(root, text="Show Assignments", command=show_assignments).grid(row=5,column=8)

def show_grade():
    course = get_selected_course()
    result = course.display_course_grade()
    output_label.config(text=result)

tk.Button(root, text="Show Grade", command=show_grade).grid(row=6)

def clear_fields():
    entryName.delete(0, tk.END)
    entryScore.delete(0, tk.END)
    entryPoints.delete(0, tk.END)

tk.Button(root, text="Clear Fields", command=clear_fields).grid(row=6,column=8)

def save_data_gui():
    course = get_selected_course()
    course.save_data()

tk.Button(root, text="Save", command=save_data_gui).grid(row=6,column=11)
def load_data_gui():
    course = get_selected_course()
    message = course.load_data()

    if message:
        output_label.config(text=message)

tk.Button(root, text="Load", command=load_data_gui).grid(row=6,column=10)

tk.Button(root, text="Quit", command=root.quit).grid()



root.mainloop()