import pandas as pd
from .students import students

def getMeanStudents(students: pd.DataFrame) -> pd.Series:
    return students.groupby(level=0)['score'].mean()

def getMeanCourse(students: pd.DataFrame) -> pd.Series:
    return students.groupby('course')['score'].mean()

def getMaxMean(students_scores: pd.Series) -> str:
    return str(students_scores.idxmax())

def getLetterGrades(stu: students) -> pd.Series:
    stu.add_letter_grade()
    return stu.students.groupby('letter_grade').score.agg(len)