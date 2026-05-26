import pandas as pd
from .utils import get_mean_students, get_mean_course, get_max_mean, get_letter_grades
from .students import Students as st


class Report:
    def __init__(self, students: st):
        self.names = students.students.index.unique()
        self.num_records = len(students.students)
        self.students_mean_scores = get_mean_students(students.students)
        self.courses_mean_scores = get_mean_course(students.students)
        self.best_student = get_max_mean(self.students_mean_scores)
        self.distribution = get_letter_grades(students)
    
    def write_report(self, file_name: str):
        with open(file_name, "w", encoding="UTF-8") as file:
            file.writelines(["Grade Analysis Report\n", 
                             "\n", 
                             "Total record: ", str(self.num_records), "\n",
                             "students: ", str(list(self.names)), "\n",
                             "Average score by student: ", "\n",
                             self.students_mean_scores.to_string(), "\n", 
                             "\n",
                             "Average score by course: \n",
                             self.courses_mean_scores.to_string(), "\n",
                             "Top student: \n",
                             self.best_student, " with average score ", 
                             str(self.students_mean_scores[self.best_student]), "\n",
                             "\n",
                             "Grade distribution: \n",
                             self.distribution.to_string()])