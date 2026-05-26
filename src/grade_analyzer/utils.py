import pandas as pd
from .students import Students

def get_mean_students(students: pd.DataFrame) -> pd.Series:
    return students.groupby(level=0)['score'].mean()

def get_mean_course(students: pd.DataFrame) -> pd.Series:
    return students.groupby('course')['score'].mean()

def get_max_mean(students_scores: pd.Series) -> str:
    return str(students_scores.idxmax())

def get_letter_grades(stu: Students) -> pd.Series:
    stu.add_letter_grade()
    return stu.students.groupby('letter_grade').score.agg(len)