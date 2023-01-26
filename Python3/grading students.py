#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def roundUp5(x, base=5):
    rounded = base * round(x/base)
    if rounded > x:
        return rounded

    return x


def gradingStudents(grades):
    newGrades = []
    for grade in grades:
        if grade < 38:
            newGrades.append(grade)
        else:
            print(roundUp5(grade) - grade)
            if((roundUp5(grade) - grade) < 3):
                newGrades.append(roundUp5(grade))
            else:
                newGrades.append(grade)

    return newGrades


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
