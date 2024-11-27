import json
import os

# Student Information (Edit the following lines)
STUDENT_NAME = "my_name"
STUDENT_NUMBER = "my_std_no"
REGISTRATION_NUMBER = "my_reg_no"

class Student:
    def __init__(self, admin_no, name):
        """Initialize a student with admin number and name."""
        self.admin_no = admin_no
        self.name = name
        self.marks = {"Maths": None, "Science": None, "English": None, "SST": None}

    def set_marks(self, subject, marks):
        """Set marks for a specific subject."""
        if subject in self.marks:
            self.marks[subject] = marks
        else:
            print("Invalid subject!")

    def get_marks(self, subject):
        """Get student's mark for a specific subject."""
        return self.marks[subject]

    def edit_marks(self, subject, new_marks):
        """Edit marks for a specific subject."""
        if subject in self.marks:
            self.marks[subject] = new_marks
        else:
            print("Subject not found")

    def to_dict(self):
        """Convert Student object to dictionary for JSON serialization."""
        return {
            "admin_no": self.admin_no,
            "name": self.name,
            "marks": self.marks
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Student object from a dictionary."""
        student = cls(data['admin_no'], data['name'])
        student.marks = data['marks']
        return student

class Gradebook:
    def __init__(self, filename='gradebook.json'):
        """Initialize an empty gradebook and load existing data."""
        self.students = {}
        self.filename = filename
        self.load_gradebook()

    def add_student(self, student):
        """Add a student to the gradebook."""
        try:
            if student.admin_no in self.students:
                return False
            self.students[student.admin_no] = student
            self.save_gradebook()  # Save after adding a student
            return True
        except:
            return False

    def get_student(self, admin_no):
        """Add a student to the gradebook."""
        try:
            student = self.students[admin_no]
            return student
        except:
            return False


    def delete_student(self, admin_no):
        """Delete a student from the gradebook using their admin number."""
        if admin_no in self.students:
            del self.students[admin_no]
            self.save_gradebook()  # Save after deleting a student
            return True
        else:
            False

    def view_statistics(self):
        """Display statistics about the grades."""
        subjects = ['Maths','English','Science','SST']
        stats = ['Average','Max','Min','Mode','Mode_Freq']
        grade_stats = {}
        for stat in stats:
            for subject in subjects:
                grade_stats[f"{stat}_{subject}"] = 'NA'
        if self.students:
            total_students = len(self.students)
            total_marks = {subject: 0 for subject in subjects}
            for student in self.students.values():
                for subject, marks in student.marks.items():
                    try:
                        student_mark = int(marks)
                        total_marks[subject] += student_mark
                    except:
                        pass
            for subject, total in total_marks.items():
                average = total / total_students if total_students > 0 else 0
                grade_stats[f"Average_{subject}"] = float(f"{average:.2f}")
        return grade_stats

    def view_student_grades(self, admin_no):
        """View grades of a specific student by their admin number."""
        results = {}
        if admin_no in self.students:
            student = self.students[admin_no]
            # print(f"Grades for {student.name} (Admin No: {admin_no}):")
            for subject, marks in student.marks.items():
                results[subject] = {marks if marks is not None else 'N/A'}
        return results

    def print_gradebook(self):
        """Print the complete gradebook."""
        gradebook_details = {
            'total_students': 0,
            'student_details': {}
        }
        if self.students:
            gradebook_details['total_students'] = len(self.students)
            for admin_no, student_details in self.students.items():
                gradebook_details['student_details'] = {
                    admin_no:student_details.name
                }
        return gradebook_details

    def save_gradebook(self):
        """Save the gradebook to a JSON file."""
        with open(self.filename, 'w') as f:
            json.dump({admin_no: student.to_dict() for admin_no, student in self.students.items()}, f)

    def load_gradebook(self):
        """Load the gradebook from a JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                for student_data in data.values():
                    student = Student.from_dict(student_data)
                    self.students[student.admin_no] = student

def print_menu():
    print("--------------------Menu--------------------")
    print("1 - Add student with marks")
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
