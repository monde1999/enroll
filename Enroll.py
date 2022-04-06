from Database import Student
from Database import Database

###########-SIMULATION-###########
# return True if simulation is executed
class Console:
    def prompt(self, msg):
        return True
class Printer:
    def print_receipt(self):
        return True

console = Console()
printer = Printer()
##################################

class Enroll:
    # Conditions
    has_submitted_required_documents:bool = False
    has_completed_prerequisite_senior_high_courses:bool = False
    has_passed_entrance_exam:bool = False
    has_paid_fee:bool = False

    student:Student = None
    enrollment_status:str = None
    # prompt:str = None
    prompt:bool = False
    receipt:bool = False

    def __init__(self,student):
        self.student = student
    
    def set_submit_documents(self, submitted:bool):
        self.has_submitted_required_documents = submitted
    
    def set_pay_fee(self, paid:bool):
        self.has_paid_fee = paid
    
    def set_complete_prerequisite_courses(self, completed:bool):
        self.has_completed_prerequisite_senior_high_courses = completed
    
    def set_has_passed_entrance_exam(self, has_passed:bool):
        self.has_passed_entrance_exam = has_passed

    def __add_to_db(self, db:Database, status:str):
        self.student.status = status
        db.add(self.student)
    
    def enroll(self,database:Database):
        # res = (self.enrollment_status,self.prompt)
        
        if self.has_completed_prerequisite_senior_high_courses and self.has_submitted_required_documents \
            and self.has_passed_entrance_exam and self.has_paid_fee:
                #enrollment
                self.receipt = printer.print_receipt()
                self.enrollment_status = 'Enrolled'
                self.__add_to_db(database,self.enrollment_status)
                
        elif self.has_completed_prerequisite_senior_high_courses and self.has_submitted_required_documents \
            and self.has_passed_entrance_exam and not self.has_paid_fee:
                #enrollment
                # self.prompt = "Some requirements are not met. Enrollment cannot proceed."
                self.prompt = console.prompt()
                self.enrollment_status = 'Pending'
                self.__add_to_db(database,self.enrollment_status)
        
        elif self.has_completed_prerequisite_senior_high_courses and self.has_submitted_required_documents \
            and not self.has_passed_entrance_exam and self.has_paid_fee:
                #enrollment
                # self.prompt = "Some requirements are not met. Enrollment cannot proceed."
                self.prompt = console.prompt()
                self.enrollment_status = 'Rejected'
                
        elif self.has_completed_prerequisite_senior_high_courses and self.has_submitted_required_documents \
            and not self.has_passed_entrance_exam and not self.has_paid_fee:
                #enrollment
                # self.prompt = "Some requirements are not met. Enrollment cannot proceed."
                self.prompt = console.prompt()
                self.enrollment_status = 'Rejected'
        
        elif self.has_completed_prerequisite_senior_high_courses and not self.has_submitted_required_documents \
            and self.has_passed_entrance_exam and self.has_paid_fee:
                #enrollment
                # self.prompt = "Some requirements are not met. Enrollment cannot proceed."
                self.prompt = console.prompt()
                self.enrollment_status = 'Pending'
                self.__add_to_db(database,self.enrollment_status)
        
        # return res