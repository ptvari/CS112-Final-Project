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