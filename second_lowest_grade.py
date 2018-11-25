def second_lowest_grade(marks):
    marks = list(set(marks))
    marks.sort()
    return marks[1]
def student_name(ls,marks):
    names = []
    for i in range(0, len(ls)):
       if ls[i][1] == second_lowest_grade(marks):
           names.append(ls[i][0])
    names.sort()
    return names 
def main():
    n = int(input("enter no of students"))
    ls = []
    marks = []
    for i in range(0, n):
       name = input()
       score = float(input())
       ls.append([name,score])
       marks.append(score)
    print(student_name(ls,marks))
    return None
main()
