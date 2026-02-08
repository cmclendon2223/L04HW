# convert letter grade to int, 0 for F, 3 for D-, 4 for D, 5 for D+, 6 for C, and so on
def gradeToNumber(grade):
    letter = grade[0].upper()
    signBonus = 1
    value = 0
    if '-' in grade: signBonus = 0
    elif '+' in grade: signBonus = 2
    if grade[0] == "A": value = 12
    elif grade[0] == "B": value = 9
    elif grade[0] == "C": value = 6
    elif grade[0] == "D": value = 3
    elif grade[0] == "F": value = 0

    return signBonus + value

# undo the the letter to int conversion made above, F to 0, 3 to D-, and so on
def numberToGrade(n):
    letter = ""
    value = n // 3
    if value == 4: letter = "A"
    elif value == 3: letter = "B"
    elif value == 2: letter = "C"
    elif value == 1: letter = "D"
    elif value == 0: letter = "F"

    sign = "-"
    signValue = n % 3
    if signValue == 1: sign = ""
    elif signValue == 2: sign = "+" 
    return letter + sign

# convert user input into an array of uppercase strings
def processLine(line):
    return line.upper().split("$ ")

# make sure a string array is valid to use in the program
def isValidGradeArray(grades):
    if len(grades) != 4:
        return False
    for grade in grades:
        if len(grade) > 2 or len(grade) < 1:
            return False
        if grade[0] not in "ABCDF":
            return False
        if len(grade) == 2:
            if grade[1] not in " -+":
                return False
    return True
