####  Carefully read instructions this template and only change where you are instructed to
### - Rename this template from grade_book_template.py to YOUR_STUDENT_NUMBER.py e.g 202408110.py
### - The Gradebook app keeps records of students' grades for subjects Maths, SST, English, and Science
### - The app must MAINTAIN ITS PREVIOUS STATE in case of power failure or reopening the script (Data added previously should not be lost when any of those events occur)

# Student Information (Edit the following lines)
import os
STUDENT_NAME = "NANSEREKO HOUSNAH"
STUDENT_NUMBER = "2400709631"
REGISTRATION_NUMBER = "24/U/09631/EVE"


class Student:
    def __init__(self, admin_no, name):
        """Initialize a student with admin number, name and optionally marks."""
        self.admin_no= admin_no
        self.name= name
        self.marks = {}
        

    def set_marks(self, subject, marks):
        """Set marks for a specific subject. Possible subjects are Maths, SST, English, and Science. 
        This function should return True on success and False of some error occurs. Implement logic here."""
        if subject in ["Maths","SST","English","Science"] and 0<=marks <=100:
            self.marks[subject]=marks
            return True
        return False


    def get_marks(self, subject):
        """Return student's mark for the specific subject. The returned mark should be between an Integer between 0 and 100 or none if not available """
        return self.marks.get(subject,None)

    def edit_marks(self, subject, new_marks):
        """Edit marks for a specific subject. This function should return True on success and False of some error occurs. Implement logic here."""
        if subject in self.marks and 0<=new_marks<=100:
            self.marks[subject]= new_marks
            return True
        return False
from statistics import mean ,mode
import os
import json
class Gradebook:
    def __init__(self, filename='previous_data.json'):
        """Initialize an empty gradebook. Load existing data if available.
        - A Gradebook should consist of Students
        """
        self.filename= filename
        self.students ={}
        self.load_data()
    def load_data(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as file:
                    data = json.load(file)
                    for admin_no , info in data.items():
                        student = Student(admin_no,info["name"])
                        student.marks = info['marks']
                self.students[admin_no]=student
        except FileNotFoundError:
            pass
    def save_data(self):
        data ={admin_no:{'name':student.name,'marks':student.marks} for admin_no,student in self.students.items()}
        with open(self.filename, 'w') as file:
                json.dump(data, file,indent=4)

    def add_student(self, student):
        """Add a student to the gradebook. This method should return True on success or False on failure due to some reason. Implement logic here."""
        if student.admin_no not in self.students:
            self.students[student.admin_no] = student
            self.save_data()
            return True
        return False


    def get_student(self, admin_no):
        """This should return a Student using admin_no or None if the student is not found. Implement logic here."""
        return self.students.get(admin_no, None)

    def delete_student(self, admin_no):
        """Delete a student from the gradebook using their admin number. This should return True on Success and False if admin_no is not found. Implement logic here."""
        if admin_no in self.students:
            del self.students[admin_no]
            self.save_data()
            return True
        return False


    def view_statistics(self):
        """Display statistics about the grades. Implement logic here.
         - This method must return a dictionary where key is a statistic and value is its value. see the return dictionary below
        """
        subjects = ['Maths', "Science","English","SST"]
        grade_stats = {}
        for subject in subjects:
            marks = [student.get_marks(subject) for student in self.students.values() if student.get_marks(subject) is not None]
            if marks:
                grade_stats[f'Average_{subject}'] = mean(marks)
                grade_stats[f'Max_{subject}'] = max(marks)
                grade_stats[f'Min_{subject}'] = min(marks)
                try:
                    grade_stats[f"Mode_{subject}"]= mode(marks)
                    grade_stats[f"Mode-frequeny_{subject}"]= marks.count(mode(marks))
                except:
                    grade_stats[f'Mode_{subject}']= None
                    grade_stats[f'Mode-freq_{subject}']= 0
            print("-------------------")
        return grade_stats
        # More Statistical keys to add to the dictionary
        # Min_Subject e.g Min_Maths whose value should be the lowest mark in the subject e.g math
        # Mode_Subject whose value should be the mode mark for the subject
        # Mode_Freq_Subject whose value should be the modal frequency for the subject
        #NOTE: DO NOT DEVIATE FROM THE NAMING CONVENTIONS OF THE KEYS
    

    def view_student_grades(self, admin_no):
        """View grades of a specific student. Should return the following dictionary for the student. Implement logic here."""
        student = self.get_student(admin_no)
        if student:
            return {subject: student.get_marks(subject) for subject in ["Maths", "SST","English","Science"]}
        return {}
       
    # set_marks(self, subject, marks),get_marks(self, subject),add_student(self, student),get_student(self, admin_no),view_statistics(self),view_student_grades(self, admin_no),print_gradebook(self)
    def print_gradebook(self):
        """Should return the following dictionary containing details of the gradebook. DONT CHANGE THE DICTIONARY KEYS. Implement logic here."""
        gradebook_details = {
            'total_students': len(self.students),
            'student_details': {}
        }
        for admin_no,student in self.students.items():
            student_marks ={"Maths":student.get_marks("Maths"),
            "Science":student.get_marks("Science"),
            "English":student.get_marks("English"),
            "SST":student.get_marks("SST")}
            gradebook_details['student_details'][admin_no]={
                'name':student.name,
                "marks":student_marks
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
            admin_no = input("Enter the admin no of the student: ")
            name = input("Enter the student name: ")
            student = Student(admin_no,name)
            for subject in ["Maths",'English', "SST","Science"]:
                while True:
                    try:
                        marks = int(input(f"Enter marks for {subject}(0-100): "))
                        if 0<=marks<=100:
                            student.set_marks(subject,marks)
                            break
                        else:
                            print("Please eneter a value between 0 and 100")
                    except ValueError:
                        print("Invalid input. Please enter a value between 0 and 100.")
            if gradebook.add_student(student):
                print(f"{name} added successfully")
            else:
                print(f"{admin_no} already exists")
            gradebook.add_student(student)
        elif choice == '2':
            admin_no = input("Enter the admin no of the student to be deleted: ")
            if gradebook.delete_student(admin_no):
                print(f"student with {admin_no} deleted successfully.")
            else:
                print(f"Student with {admin_no} not found.")

        elif choice == '3':
            stats=gradebook.view_statistics()
            print("Grade Statistics:")
            for stat,value in  stats.items():
                print(f"{stat}: {value}")
        elif choice == '4':
            admin_no = input("Enter the the admin no of the student to be viewed: ")
            student_grades=gradebook.view_student_grades(admin_no)
            if student_grades:
                print(f"Grades for {name}: ")
                for subject,grade in student_grades.items():
                    print(f"{subject} :{ grade}")
            else:
                print(f"Student with {admin_no} not found.")
        elif choice == '5':
            admin_no = input("Enter the admin number of the student whose marks you want to edit: ")
            student = gradebook.get_student(admin_no)
            if student:
                subject = input("Enter the subject whose marks you want to edit: ")
                new_marks =input("Enter the new marks (0-100): ")
                try:
                    new_marks= int(new_marks)
                    if 0<=new_marks<=100:
                        if student.edit_marks(subject,new_marks):
                            print(f"Marks for {subject} updated successfully.")
                        else:
                            print(f"failed to update the marks. Please check subhject and try again!")
                    else:
                        print("Please enyer a mark between 0 and 100.")
                    
                except ValueError:
                    print("Invalid input. Please enter a number.")
            else:
                print(f"Student with {admin_no} not found.")
            
        elif choice == '6':
            grade_book_details=gradebook.print_gradebook()
            print("Gradebook details: ")
            print(f"Total Students: {grade_book_details['total_students']}")
            for admin_no, student_info in grade_book_details['student_details'].items():
                print(f"Admin Number: {admin_no}, Name:{student_info['name']}")
                print("Marks: ")
                for subject,marks in student_info['marks'].items():
                    print(f"{subject}: {marks if marks is not None else 'No marks entered'}")
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