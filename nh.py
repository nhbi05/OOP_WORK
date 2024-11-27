import json

class Student:
    def __init__(self, admin_no, name):
        self.admin_no = admin_no
        self.name = name
        self.marks = {}
    def set_marks(self, subject, marks):
        if subject in ["MATHS", "SST", "ENGLISH","SCIENCE"]:
            if 0<=marks<=100:
                self.marks[subject] = marks
                return True
        return False
    def get_marks(self, subject):
        return self.marks.get(subject, None)
        """Return student's mark for the specific subject. The returned mark should be between an Integer between 0 and 100 or none if not available """

    def edit_marks(self, subject, new_marks):
        if self.set_marks(subject, new_marks):
            return True
        return False
        """Edit marks for a specific subject. This function should return True on success and False if some error occurs. Implement logic here."""
       
class Gradebook:
    def __init__(self, filename='previous_data.json'):
        self.filename = filename
        self.students = {}
        self.load_data()
        """Initialize an empty gradebook. Load existing data if available.
        - A Gradebook should consist of Students
        """
    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                for admin_no, info in data.items():
                    student = Student(admin_no, info['name'])
                    student.marks = info['marks']
                    self.students[admin_no] = student
        except FileNotFoundError:
            pass
    def save_data(self):
        data = {admin_no: {'name': student.name, 'marks': student.marks} for admin_no, student in self.students.items()}
        with open(self.filename, 'w') as file:
            json.dump(data, file)
           
    def add_student(self, student):
        if student.admin_no not in self.students:
            self.students[student.admin_no] = student
            self.save_data()
            return True
        return False
        """Add a student to the gradebook. This method should return True on success or False on failure due to some reason. Implement logic here."""

    def get_student(self, admin_no):
        return self.students.get(admin_no, None)
        """This should return a Student using admin_no or None if the student is not found. Implement logic here."""

    def delete_student(self, admin_no):
        if admin_no in self.students:
            del self.students[admin_no]
            self.save_data()
            return True
        return False
        """Delete a student from the gradebook using their admin number. This should return True on Success and False if admin_no is not found. Implement logic here."""

    def view_statistics(self):
        """Display statistics about the grades. Implement logic here.
         - This method must return a dictionary where key is a statistic and value is its value. see the return dictionary below
        """
        '''grade_stats = {
            'Average_Maths': 'Replace this with the average mark of Maths',
            'Average_English': 'Replace this with the average mark of English',
            'Average_Science': 'Replace this with the average mark of Science',
            'Average_SST': 'Replace this with the average mark of SST',
            'Max_Maths': 'Replace this with the highest mark in Maths',
            'Max_English': 'Replace this with the highest mark in English',
            'Max_Science': 'Replace this with the highest mark in Science',
            'Max_SST': 'Replace this with the highest mark in SST',
            #... add more statisics here using the same convention (see below)

        }
        # More Statistical keys to add to the dictionary
        # Min_Subject e.g Min_Maths whose value should be the lowest mark in the subject e.g math
        # Mode_Subject whose value should be the mode mark for the subject
        # Mode_Freq_Subject whose value should be the modal frequency for the subject
        #NOTE: DO NOT DEVIATE FROM THE NAMING CONVENTIONS OF THE KEYS
        return grade_stats'''
        subjects = ["MATHS", "SST", "ENGLISH","SCIENCE"]
        grade_stats ={}

        for subject in subjects:
            marks = [student.get_marks(subject) for student in self.students.values() if student.get_marks(subject) is not None]
            if marks:
                grade_stats[f'Average_{subject}'] = sum(marks)/len(marks)
                grade_stats[f'Max_{subject}'] = max(marks)
                grade_stats[f'Min_{subject}'] = min(marks)
                mode = max(set(marks), key=marks.count)
                grade_stats[f'Mode_{subject}'] = mode
                grade_stats[f'Mode_freq_{subject}'] = marks.count(mode)

        return grade_stats
   
    def view_student_grades(self, admin_no):
        student = self.student.get(admin_no,None)
        if student:
            """View grades of a specific student. Should return the following dictionary for the student. Implement logic here."""
            student_grades = {
                'Maths': student.get_marks("MATHS"),
                'English': student.get_marks("ENGLISH"),
                'Science': student.get_marks("SCIENCE"),
                'SST': student.get_marks("SST")
            }
            return student_grades
        return None
    def edit_student_grades(self, admin_no, subject, marks):
        student = self.students.get(admin_no, None)
        if student:
            if student.edit_marks(subject, marks):
                self.save_data()
                return True
        return False

    # set_marks(self, subject, marks),get_marks(self, subject),add_student(self, student),get_student(self, admin_no),view_statistics(self),view_student_grades(self, admin_no),print_gradebook(self)
    def print_gradebook(self):
        """Should return the following dictionary containing details of the gradebook. DONT CHANGE THE DICTIONARY KEYS. Implement logic here."""
        gradebook_details = {
            'total_students': len(self.students),
            'student_details': {admin_no: student.name for admin_no, student in self.students.items()}
        }
        return gradebook_details

def print_menu():
    """Print the menu for user interaction. Do not change this"""
    print("--------------------Menu--------------------")
    print("1 - Add student")
    print("2 - Delete student, given an admin_no")
    print("3 - View statistics about the grades")
    print("4 - View student grades")
    print("5 - Edit student grades")
    print("6 - Print Gradebook")
    print("m - Print menu")
    print("c - Clear Screen")
    print("q - Quit system\n")

def main():
    """Main function to run the gradebook application."""
    gradebook = Gradebook()
    while True:
        print_menu()
        choice = input("Select an option: ").strip().lower()
        #Be sure to validate any values entered by the user and act accordingly
        if choice == '1':
            admin_no = input("Enter the Admin number.: ")
            name = input("Enter name of student.: ")
            while True:
                try:
                    SST = int(input("Enter the sst mark of the student: "))
                    MATH = int(input("Enter the math mark of the student: "))
                    SCIENCE = int(input("Enter the science mark of the student: "))
                    ENGLISH = int(input("Enter the english mark of the student: "))
                    marks = {'SST': SST, 'MATH': MATH, 'SCIENCE': SCIENCE, 'ENGLISH': ENGLISH}
                    if any(mark < 0 or mark > 100 for mark in marks.values()):
                        raise ValueError("Marks should be between 0 and 100. ")
                    break
                except ValueError as e:
                    print(f"{e} is an invalid input. Please enter a valid mark.")

            student = Student(admin_no,name)
            for subject, mark in marks.items():
                student.set_marks(subject, mark)
           
            if gradebook.add_student(student):
                print(f"{name} ({admin_no}) added to class. ")
            else:
                print(f"Student with admin number ({admin_no}) already exists. ")

        elif choice == '2':
            admin_no = input("Enter the admin number to delete.: ")
            if gradebook.delete_student(admin_no):
                print(f"{admin_no} deleted.")
            else:
                print(f"{admin_no} not found. ")

        elif choice == '3':
            stats = gradebook.view_statistics()
            for t, v in stats.items():
                print((f"{t}:{v}"))

        elif choice == '4':
            admin_no = input("Enter admin number.: ")
            grades = gradebook.view_student_grades(admin_no)
            if grades:
                for subject, mark in grades.items():
                    print(f"{subject}: {mark}")
                else:
                    print(f"{admin_no} not found.")

        elif choice == '5':
            admin_no =  input("Enter admin number.: ")
            student = gradebook.get_student(admin_no)
            if student:
                subject =  input("Enter subject name: ").upper()
                while True:
                    try:
                        marks =  int(input("Enter subject mark: "))
                        if 0 <= marks <= 100:
                            break
                        else:
                            print("Marks should be between 0 and 100.")
                    except ValueError:
                        print("Please enter numeric values for marks.")

                if student.edit_marks(subject,marks):
                    gradebook.save_data()
                    print(f"Marks for {admin_no} successfully changed.")
                else:
                    print(f"Failed to update marks for {admin_no}.")
            else:
                print(f"{admin_no} not found.")

        elif choice == '6':
            gradebook_details = gradebook.print_gradebook()
            print(gradebook_details)
        elif choice == 'm':
            print_menu()
        elif choice == 'c':
            print("\033c", end="")  # Clear screen
        elif choice == 'q':
            gradebook.save_data()
            #Implement logic here to save the current state of the application and gracefully quit.

            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()