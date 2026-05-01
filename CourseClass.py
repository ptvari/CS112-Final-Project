"""
This portion is for the class function
"""

class Course:
    def __init__(self,course_name):
        self.course_name=course_name
        self.assignments=[]

    def add_assignment(self, name, score, points):
        assignment={
            "name": name,
            "score": score,
            "points": points
        }
        self.assignments.append(assignment)

    def calc_grade(self):
        total_earned=0
        total_possible=0
        for assignment in self.assignments:
            total_earned +=assignment["score"]
            total_possible+=assignment["points"]
        if total_possible==0:
            return 0
        return (total_earned / total_possible) *100

    def display_course_assignments(self):
        if not self.assignments:
            return "No assignments yet."
        output= f"Assignments for {self.course_name}:\n"
        output += "----------------------------------\n"
        for assignment in self.assignments:
            name=assignment["name"]
            score=assignment["score"]
            points=assignment["points"]
            
            output +=f"{name}|{score}/{points}\n"

    def display_course_grade(self):

    def save_data(self):

    def load_data(self):