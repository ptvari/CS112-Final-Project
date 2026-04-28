"""
This portion is for the class function
"""

class Course:
    def __init__(self,course_name,score):
        self.course_name=course_name
        #assignment_name, pts earned, pts_pass
        self.assignments={}
        self.score=score
