"""
This portion is for the class function
"""

# creates the Course class
class Course:

    # constructor that sets up the course name and assignment list
    def __init__(self,course_name):

        # stores the course name
        self.course_name=course_name

        # empty list that will hold assignments
        self.assignments=[]


    # adds an assignment into the assignments list
    def add_assignment(self, name, score, points):

        # dictionary holding assignment information
        assignment={
            "name": name,
            "score": score,
            "points": points
        }

        # adds assignment dictionary into the list
        self.assignments.append(assignment)


    # calculates the overall grade percentage
    def calc_grade(self):

        # keeps track of earned points
        total_earned=0

        # keeps track of possible points
        total_possible=0

        # loops through each assignment
        for assignment in self.assignments:

            # adds earned score
            total_earned +=assignment["score"]

            # adds total possible points
            total_possible+=assignment["points"]

        # prevents division by zero
        if total_possible==0:
            return 0

        # returns the final grade percentage
        return (total_earned / total_possible) *100


    # displays all assignments for the course
    def display_course_assignments(self):

        # checks if there are no assignments
        if not self.assignments:
            return "No assignments yet."

        # title text for the output
        output = f"Assignments for {self.course_name}:\n"

        # divider line
        output += "----------------------------------\n"

        # tracks earned points
        total_earned = 0

        # tracks possible points
        total_possible = 0

        # loops through assignments
        for assignment in self.assignments:

            # stores assignment name
            name = assignment["name"]

            # stores assignment score
            score = assignment["score"]

            # stores assignment points possible
            points = assignment["points"]

            # adds earned score
            total_earned += score

            # adds possible points
            total_possible += points

            # adds assignment info into output text
            output += f"{name} | {score} / {points}\n"

        # adds divider line
        output += "----------------------------------\n"

        # shows total earned points
        output += f"Total Points Earned: {total_earned}\n"

        # shows total possible points
        output += f"Total Points Possible: {total_possible}\n"

        # calls the grade calculation function
        grade = self.calc_grade()

        # returns the final output text
        return output


    # displays the final course grade
    def display_course_grade(self):

        # stores calculated grade
        grade=self.calc_grade()

        # returns formatted grade string
        return f"Overall Grade for {self.course_name}: {grade:.2f}%"


    # saves assignment data into a text file
    def save_data(self):

        # creates filename based on course name
        filename = f"{self.course_name}.txt"

        # opens the file in write mode
        with open(filename, "w") as file:

            # loops through assignments
            for assignment in self.assignments:

                # stores assignment name
                name = assignment["name"]

                # stores assignment score
                score = assignment["score"]

                # stores assignment points
                points = assignment["points"]

                # writes assignment data into the file
                file.write(f"{name},{score},{points}\n")


    # loads assignment data from a text file
    def load_data(self):

        # creates filename based on course name
        filename = f"{self.course_name}.txt"

        # clears old assignments before loading
        self.assignments = []

        # tries to open the file
        try:

            # opens the file in read mode
            with open(filename, "r") as file:

                # loops through each line in the file
                for line in file:

                    # separates data using commas
                    name, score, points = line.strip().split(",")

                    # creates assignment dictionary
                    assignment = {
                        "name": name,
                        "score": int(score),
                        "points": int(points)
                    }

                    # adds assignment into list
                    self.assignments.append(assignment)

        # runs if the file does not exist
        except FileNotFoundError:

            # returns error message
            return "No saved data found."