import pandas as pd
import numpy as np
from .exceptions import IllegalSize

class students:
    def __init__(self, file_name: str) -> None:
        self.students = pd.read_csv(file_name, index_col=0)
        if (list(self.students.columns) != ["course", "score"]):
            raise IllegalSize("number or names of columns unexpected")
        masks_nan = self.students.isna()
        if masks_nan.any().any():
            raise IllegalSize("number of items unexpected")

    @staticmethod
    def to_letter_grade(p) -> str:
        if p >= 90:
            return 'A'
        elif p >= 80:
            return 'B'
        elif p >= 70:
            return 'C'
        elif p >= 60:
            return 'D'
        else:
            return 'F'
        
    def add_letter_grade(self):
        self.students['letter_grade'] = self.students.score.map(students.to_letter_grade)

