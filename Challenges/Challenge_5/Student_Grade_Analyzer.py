def main():
    student_dictionary = get_student_dictionary()
    
    print("\n")
    
    print(f"Class average: {get_average(student_dictionary)}")
    
    highest_student, highest_grade, lowest_student, lowest_grade = get_highest_lowest(student_dictionary)
    
    print(f"Highest: {highest_student} ({highest_grade})")
    print(f"Lowest: {lowest_student} ({lowest_grade})")
    
    
# Prompts the user for a name and a grade then adds them as a pair to the dict
def get_student_dictionary():
    student_dictionary = {}
    while True:
        student_name = input("Enter student name (or 'done' to stop): ").lower().title()
        if student_name == "Done":
            break
        else:
            student_grade = int(input("Enter grade: "))
            student_dictionary.update({student_name: student_grade})
            print(f"{student_name} added to the data-base.")
            continue
    return student_dictionary

# Calculates the average of the dictionary's keys
def get_average(dictionary):
    grades = []
    for student in dictionary:
        grades.append(dictionary.get(student))
    summed_grades = sum(grades)
    return float(summed_grades) / float(len(grades))

# Returns the highest and lowest names and grades
def get_highest_lowest(dictionary):
    grades = []
    for student in dictionary:
        grades.append(dictionary.get(student))
    highest_grade = max(grades)
    lowest_grade = min(grades)
    for student in dictionary:
        if dictionary.get(student) == highest_grade:
            highest_student = student
        elif dictionary.get(student) == lowest_grade:
            lowest_student = student
    return highest_student, highest_grade, lowest_student, lowest_grade

    
if __name__ =="__main__":
    main()
    
    