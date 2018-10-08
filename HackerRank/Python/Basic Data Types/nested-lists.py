"""
Problem Description:
    Given the names and grades for each student in a Physics class of N students,
    store them in a nested list and print the name(s) of any student(s) having
    the second lowest grade

    Note: If there are multiple students with the same grade, order their names
    alphabetically and print each name on a new line

    Constraints:
        - 2 <= N <= 5
        - There will always be one or more students having the second lowest
        grade

Example
Input:
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Output:
Berry
Harry
"""
import sys

if __name__ == '__main__':

    student_grades = []
    current_min = sys.maxsize
    second_lowest_grade = sys.maxsize

    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_grades.append([name, score])

    for i in range(len(student_grades)):
        if (i < current_min)
