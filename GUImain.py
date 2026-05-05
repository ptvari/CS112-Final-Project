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

#gr
def get_selected_course():
    return courses[selected_course.get()]

#grabs the assignment that the user inputs and adds it to the list
def add_assignment_gui():
    course = get_selected_course()

    name = entryName.get()
    score = int(entryScore.get())
    points = int(entryPoints.get())

    course.add_assignment(name, score, points)

tk.Button(root, text="Add Assignment", command=add_assignment_gui).pack()


root.mainloop()