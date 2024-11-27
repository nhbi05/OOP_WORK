class Student:
    def __init__(self,admin_no,name):
        self.admin_no=admin_no
        self.name=name
        self.marks={}
    
    def set_marks(self,subject,mark):
        if subject in self.marks:
            self.marks[subject]=mark
            return True
        return False
    def view_marks(self,subject):
        return self.marks[subject]
    
    def edit_marks(self,subject,new_marks):
        if subject in self.marks:
            self.marks[subject]=new_marks
            return True
        return False
