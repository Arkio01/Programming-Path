def main():
    students_dict = {}
    try:
        with open ('grades.txt', 'r') as f:
            for line in f:
                student_name, grades = line.removesuffix("\n").split(", ")
                grade_list = grades.split("|")
                for grade in grade_list:
                    if not grade.isnumeric():
                        grade_list.remove(grade)
                students_dict[student_name] = [int(item) for item in grade_list]
    except FileNotFoundError:
        print("File not found")
        
    while True:
        
        print("\n")
        
        user_choice = get_option()
        
        # Control panel
        if user_choice == 1:
            output = add_student(students_dict)
            if not output == None:
                student, grades = output
                students_dict[student] = grades
            
        elif user_choice == 2:
            output = add_grade(students_dict)
            if not output == None:
                student_name, new_grade = output
                for student in students_dict:
                    if student == student_name:
                        students_dict[student].append(new_grade)
                        
        elif user_choice == 3:
            view_all_students(students_dict)
            
        elif user_choice == 4:
            view_single_student(students_dict)
            
        elif user_choice == 5:
            show_student_avg(students_dict)
            
        elif user_choice == 6:
            show_class_avg(students_dict)
            
        elif user_choice == 7:
            show_best_students(students_dict)
            
        elif user_choice == 8:
            save_to_file(students_dict)
            break
            

    
# Gets user choice
def get_option():
    while True:
        print("\n")
        print("1. Add new student")       
        print("2. Add a grade to an existing student")       
        print("3. View all students and their grades")       
        print("4. View a single student’s grades")       
        print("5. Show the average grade of a student")       
        print("6. Show the class average")       
        print("7. Show the top-performing student(s)")       
        print("8. Save & exit")       
            
        user_input = int(input("Choose an option: "))
        
        if not user_input in range(1, 9):
            print("Not a valid option")
            continue
        else:
            return user_input
        

# Prompts the user for data and adds a new student to the dictionary after reviewing it 
def add_student(students):
    new_student = {}
    
    student_name = input("Student name: ").lower().strip()
    
    existing_students = []
    for student in students:
        existing_students.append(student)

    if student_name in existing_students:
        print(f"{student_name} already exists.")
        return
    else:
        grades = []
        while True:
            grade = input("Student grade (or 'done' to finish operation): ").lower().strip()
        
            if not grade.isnumeric():
                if grade == "done":
                    if len(grades) == 0:
                        print("No valid grade specified. Student won't be added")
                        return
                    else:
                        print("Student added succesfully")
                        return student_name, grades
                else:
                    print(f"{grade} is not a valid grade. it won't be added")
                    continue
            elif grade.isnumeric():
                if not int(grade) in range(0, 101):
                    print(f"{grade} is not a valid grade. it won't be added")
                else:
                    grades.append(int(grade))
                    print(f"{grade} inserted.")
                    print("")
            
        
# Prompts the user for a name and then a grade, which it reviews and then adds to an existent student of the dictionary
def add_grade(students):
    while True:
        student_name = input("Student (or 'exit' to terminate operation): ").lower().strip()
        if student_name == "exit":
            print("No update was made.")
            return
        elif not student_name in students:
            print(f"{student_name} not in database")
            continue
        else:
            while True:
                new_grade = input("New grade (or 'exit' to terminate operation): ").lower().strip()
                if not new_grade.isnumeric():
                    if new_grade == "exit":
                        print("No update was made.")
                        return
                    else:
                        print(f"{new_grade} is not a valid grade. it won't be added")
                        continue
                elif new_grade.isnumeric():
                    if not int(new_grade) in range(0, 101):
                        print(f"{new_grade} is not a valid grade. it won't be added")
                        continue
                    else:
                        return student_name, int(new_grade)
            
            

# Prints a list of all students ands their grades
def view_all_students(students):
    for student in students:
        print(f"{student.title()}: {students[student]}")

# Prompts the user for a name and prints that student's info is available
def view_single_student(students):
    student_name = input("Student (or 'exit' to terminate operation): ").lower().strip()
    if student_name == "exit":
        print("No update was made.")
        return
    elif student_name in students:
        for student in students:
            if student == student_name:
                print(f"{student.title()}: {students[student]}")
            else:
                continue
    else:
        print(f"{student_name.title()} not in database.")
        return
    
# Prompts the user for a name and prints the sudent's average grade
def show_student_avg(students):
    student_name = input("Student (or 'exit' to terminate operation): ").lower().strip()
    if student_name == "exit":
        print("No update was made.")
        return
    elif student_name in students:
        for student in students:
            if student == student_name:
                print(f"{student.title()} average grade: {float(sum(students[student])) / float(len(students[student]))}")
            else:
                continue
    else:
        print(f"{student_name.title()} not in database.")
        return

# Prints the overall average
def show_class_avg(students):
    grade_list = []
    for student in students:
        for grade in students[student]:
            grade_list.append(grade)
    
    print(f"{float(sum(grade_list)) / float(len(grade_list))}")

# Prints the info of the students with the highest average
def show_best_students(students):
    class_averages = []
    for student in students:
        class_averages.append(float(sum(students[student])) / float(len(students[student])))
    
    highest_average = max(class_averages)
    best_students_list = []
    for student in students:
        if float(sum(students[student])) / float(len(students[student])) == highest_average:
            best_students_list.append(student)
        else:
            continue
    if len(best_students_list) == 1:
        print(f"Best student: {best_students_list[0].title()} ({highest_average})")
    else:
        print(f"Best students: {', '.join(best_students_list).title()} ({highest_average})")
        


# Saves dictionary to external file
def save_to_file(students):
    with open ("grades.txt", 'w') as f:
        for student in students:
            string_grades = []
            for grade in students[student]:
                string_grades.append(str(grade))
            f.write(f"{student}, {'|'.join(string_grades)}\n")
            
    print("File updated.")
    return







        
if __name__ =="__main__":
    main()