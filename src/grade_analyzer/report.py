import pandas as pd
from .utils import *
from .students import students as st


class report:
    def __init__(self, students: st):
        self.names = students.students.index.unique()
        self.num_records = len(students.students)
        self.students_mean_scores = getMeanStudents(students.students)
        self.courses_mean_scores = getMeanCourse(students.students)
        self.best_student = getMaxMean(self.students_mean_scores)
        self.distribution = getLetterGrades(students)
    
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