from grade_compute import gradeToNumber, processLine, isValidGradeArray, numberToGrade
import math

def main():
    # get grades from user
    userInput = input("What are the grades? ")
    if userInput.lower() == "q":
        return None
    
    # make sure input is valid
    grades = processLine(userInput)
    if not isValidGradeArray(grades):
        print("Not a valid input")
        return None
    
    # start printing report
    print("----------------------------------------")
    print("|         GRADE REPORT SUMMARY          |")
    print("----------------------------------------")
    print("| Grades Entered: ", end="")
    for grade in grades:
        print(grade + (" " if grade == grades[3] else ", "), end="")
    print("\t\t|")

    # find lowest value
    gradeAboveBonuse = False
    lowestGrade = 100
    for grade in grades:
        value = gradeToNumber(grade)
        if value < lowestGrade:
            lowestGrade = value
        if value > 9:
            gradeAboveBonuse = True

    # remove first occurence of lower value
    for grade in grades:
        value = gradeToNumber(grade)
        if value == lowestGrade:
            grades.remove(grade)
            print("| Lowest Grade Dropped:", grade, "\t\t|")
            break
    
    # find GPA
    sum = 0
    for grade in grades:
        sum += gradeToNumber(grade)
    avg = sum / 3
    gpa = avg / 14 * 4

    # apply bonus if valid
    if not gradeAboveBonuse:
        gpa += 0.25
 
    # finish printing report
    print("| Calculated Average:", round(gpa, 2), "\t\t|")
    print("| Final Letter Grade:", numberToGrade(math.floor(gpa / 4 * 14)), "\t\t|")
    print("----------------------------------------")
        


main()