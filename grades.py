####  Carefully read instructions this template and only change where you are instructed to
### - Rename this template from grade_book_template.py to YOUR_STUDENT_NUMBER.py e.g 202408110.py
### - The Gradebook app keeps records of students' grades for subjects Maths, SST, English, and Science
### - The app must MAINTAIN ITS PREVIOUS STATE in case of power failure or reopening the script (Data added previously should not be lost when any of those events occur)

# Student Information (Edit the following lines)
STUDENT_NAME = "Replace this with Your Full Name"
STUDENT_NUMBER = "Replace this with Your Student Number"
REGISTRATION_NUMBER = "Replace this with Your Registration Number"


class Student:
    def __init__(self, admin_no, name):
        """Initialize a student with admin number, name and optionally marks."""
        self.admin_no =admin_no
        self.name=name
        self.marks={}

    def set_marks(self, subject, marks):
        """Set marks for a specific subject. Possible subjects are Maths, SST, English, and Science. This function should return True on success and False of some error occurs. Implement logic here."""
        for subject in ['Maths',"English","SST","Science"] and 0<=marks<=100:
            self.marks[subject]=marks
            return True
        return False

    def get_marks(self, subject):
        """Return student's mark for the specific subject. The returned mark should be between an Integer between 0 and 100 or none if not available """
        return self.marks.get(subject,None)

    def edit_marks(self, subject, new_marks):
        """Edit marks for a specific subject. This function should return True on success and False of some error occurs. Implement logic here."""
        for subject in self.marks and 0<=new_marks<=100:
            self.marks[subject]=new_marks
            return True
        return False

class Gradebook:
    def __init__(self, filename='previous_data.json'):
        """Initialize an empty gradebook. Load existing data if available.
        - A Gradebook should consist of Students
        """
        self.students={}
        self.filename=filename

    def add_student(self, student):
        """Add a student to the gradebook. This method should return True on success or False on failure due to some reason. Implement logic here."""
        if student.admin_no not in self.students:
            self.students[student.admin_no]=student
            return True
        return False 

    def get_student(self, admin_no):
        """This should return a Student using admin_no or None if the student is not found. Implement logic here."""
        return self.students.get(admin_no,None)
    def delete_student(self, admin_no):
        """Delete a student from the gradebook using their admin number. This should return True on Success and False if admin_no is not found. Implement logic here."""
        if admin_no in self.students:
            del self.students[admin_no]
            return True
        return False


    def view_statistics(self):
        """Display statistics about the grades. Implement logic here.
         - This method must return a dictionary where key is a statistic and value is its value. see the return dictionary below
        """
        grade_stats = {
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
        return grade_stats

    def view_student_grades(self, admin_no):
        """View grades of a specific student. Should return the following dictionary for the student. Implement logic here."""
        student_grades = {
            'Maths': 'Replace this with the mark of Maths',
            'English': 'Replace this with the mark of English',
            'Science': 'Replace this with the mark of Science',
            'SST': 'Replace this with the mark of SST'
        }
        return student_grades

    # set_marks(self, subject, marks),get_marks(self, subject),add_student(self, student),get_student(self, admin_no),view_statistics(self),view_student_grades(self, admin_no),print_gradebook(self)
    def print_gradebook(self):
        """Should return the following dictionary containing details of the gradebook. DONT CHANGE THE DICTIONARY KEYS. Implement logic here."""
        gradebook_details = {
            'total_students': 'Replace with total students in the gradebook',
            'student_details': {'Replace with student admin':'Replace with student name', #this should be for all students
                                }
        }

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
            admin_no = "Add code to get it from user"
            name = "Add code to get it from user"
            student = Student(admin_no,name)
            gradebook.add_student(student)
        elif choice == '2':
            admin_no = "Add code to get it from user"
            gradebook.delete_student(admin_no)
        elif choice == '3':
            gradebook.view_statistics()
        elif choice == '4':
            admin_no = "Add code to get it from user"
            gradebook.view_student_grades(admin_no)
        elif choice == '5':
            admin_no = "Add code to get it from user"
            student = gradebook.get_student(admin_no)
            subject = 'get from user'
            marks = 'get from user'
            student.edit_marks(subject,marks)
        elif choice == '6':
            gradebook.print_gradebook()
        elif choice == 'm':
            print_menu()
        elif choice == 'c':
            print("\033c", end="")  # Clear screen
        elif choice == 'q':
            #Implement logic here to save the current state of the application and gracefully quit.

            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()