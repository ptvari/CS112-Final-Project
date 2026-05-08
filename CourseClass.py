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

        output = f"Assignments for {self.course_name}:\n"
        output += "----------------------------------\n"

        total_earned = 0
        total_possible = 0

        for assignment in self.assignments:
            name = assignment["name"]
            score = assignment["score"]
            points = assignment["points"]

            total_earned += score
            total_possible += points

            output += f"{name} | {score} / {points}\n"

        output += "----------------------------------\n"
        output += f"Total Points Earned: {total_earned}\n"
        output += f"Total Points Possible: {total_possible}\n"

        grade = self.calc_grade()


        return output

    def display_course_grade(self):
        grade=self.calc_grade()
        return f"Overall Grade for {self.course_name}: {grade:.2f}%"

    def save_data(self):
        filename = f"{self.course_name}.txt"

        with open(filename, "w") as file:
            for assignment in self.assignments:
                name = assignment["name"]
                score = assignment["score"]
                points = assignment["points"]

                file.write(f"{name},{score},{points}\n")

    def load_data(self):
        filename = f"{self.course_name}.txt"
        self.assignments = []
        try:
            with open(filename, "r") as file:
                for line in file:
                    name, score, points = line.strip().split(",")

                    assignment = {
                        "name": name,
                        "score": int(score),
                        "points": int(points)
                    }

                    self.assignments.append(assignment)

        except FileNotFoundError:
            return "No saved data found."