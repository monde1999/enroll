from Database import Student, Enrollment, Database

###########-SIMULATION-###########
# return True if simulation is executed
class Console:
    def prompt_success(self, msg):
        return True

    def prompt_warning(self, msg):
        return True

console = Console()
##################################

class Enroll:
    def __init__(self,student):
        self.has_submitted_required_documents:bool = False
        self.has_completed_prerequisite_senior_high_courses:bool = False
        self.has_took_placement_exam:bool = False
        self.has_paid_fee:bool = False

        self.student:Student = student
        self.prompted_success = False
        self.prompted_warning = False
        self.status:str = ''
        self.pending:bool = True
        self.closed:bool = False
        self.returned_pk = None
    
    def set_submit_documents(self, submitted:bool):
        self.has_submitted_required_documents = submitted
    
    def set_pay_fee(self, paid:bool):
        self.has_paid_fee = paid
    
    def set_complete_prerequisite_courses(self, completed:bool):
        self.has_completed_prerequisite_senior_high_courses = completed
    
    def set_took_placement_entrance_exam(self, has_passed:bool):
        self.has_took_placement_exam = has_passed

    def __add_to_db(self, db:Database):
        self.student.status = self.status
        self.returned_pk = db.add_student(self.student)
        db.add_enrollment(self.returned_pk)

        enrollment = db.retrieve_enrollment__pk(self.returned_pk)
        enrollment.pending = self.pending
        enrollment.closed = self.closed
    
    def enroll(self,database:Database):
        
        if self.has_completed_prerequisite_senior_high_courses and self.has_submitted_required_documents \
            and self.has_took_placement_exam and self.has_paid_fee:
                self.prompted_success = console.prompt_success("You are now officially enrolled")
                self.status = 'Enrolled'
                self.pending = False
                self.closed = True
                
                # Then, prompt “Enrollment Successful”
                # And modify student status in database as “Enrolled”
                # And close the application.

                
        elif self.has_completed_prerequisite_senior_high_courses and self.has_submitted_required_documents \
            and self.has_took_placement_exam and not self.has_paid_fee:
                self.prompted_warning = console.prompt_warning("Some requirements are not met. Enrollment cannot proceed")
                self.status = ''
                self.pending = True
                self.closed = False
                
                # Then, prompt a message “Some requirements are not met. Enrollment cannot proceed”
                # And record application as pending.

        
        elif self.has_completed_prerequisite_senior_high_courses and self.has_submitted_required_documents \
            and not self.has_took_placement_exam and self.has_paid_fee:
                self.prompted_warning = console.prompt_warning("Some requirements are not met. Enrollment cannot proceed")
                self.status = ''
                self.pending = True
                self.closed = False
                
                # Then, prompt a message “Some requirements are not met. Enrollment cannot proceed”
                # And record applications as pending.
                
        elif self.has_completed_prerequisite_senior_high_courses and self.has_submitted_required_documents \
            and not self.has_took_placement_exam and not self.has_paid_fee:
                self.prompted_warning = console.prompt_warning("Some requirements are not met. Enrollment cannot proceed")
                self.status = ''
                self.pending = True
                self.closed = False
                
                # Then, prompt a message “Some requirements are not met. Enrollment cannot proceed”
                # And record applications as pending.

        
        elif self.has_completed_prerequisite_senior_high_courses and not self.has_submitted_required_documents \
            and self.has_took_placement_exam and self.has_paid_fee:
                self.prompted_warning = console.prompt_warning("Some requirements are not met. Enrollment cannot proceed")
                self.status = ''
                self.pending = True
                self.closed = False
                
                # Then, prompt a message, “Some requirements are not met. Enrollment cannot proceed”
                # And record the application as pending.

        self.__add_to_db(database)
        
        # return res