
""""
import unittest
from borrower import Borrower
from loan import Loan

class TestScenario1(unittest.TestCase):
  def setUp(self) -> None:
    loanAmount = 100000
    borrower = Borrower(
      depositAmount=loanAmount, nationality='Filipino', age=18,
      employment='employed', monthlyIncome=30000, accountNumber='0123456'
    )
    self.loan = Loan(loanAmount=loanAmount, borrower=borrower)
    return super().setUp()
  def tearDown(self) -> None:
    # delete all the temporary data created in setUp() method
    return super().tearDown()
  def test_nationality(self):
    c1 = self.loan.checkNationality()
    self.assertEqual(c1, True)
  def test_age(self):
    c2 = self.loan.checkAge()
    self.assertEqual(c2, True)
  def test_employment(self):
    c3 = self.loan.checkEmployment()
    self.assertEqual(c3, True)
  def test_monthly_income(self):
    c4 = self.loan.checkMonthlyIncome()
    self.assertEqual(c4, True)
  def test_loan_amount(self):
    c5 = self.loan.checkLoanAmount()
    self.assertEqual(c5, True)
  def test_submit_bank_account(self):
    a1 = self.loan.submitBankAccount()
    self.assertEqual(a1, True)
  def test_grant(self):
    a2 = self.loan.grant()
    self.assertEqual(a2, True)
  def test_deposit(self):
    a3 = self.loan.deposit()
    self.assertEqual(a3, True)
if __name__ == '__main__':
    unittest.main()
"""


import unittest
from Database import Database, Student
from Enroll import Enroll
class Scenario1(unittest.TestCase):
    def setUp(self) -> None:
        self.DB = Database()
        self.student = Student(first_name='Mark', last_name='Simbajon')
        self.enroll = Enroll(self.student)

        self.enroll.set_complete_prerequisite_courses(True)
        self.enroll.set_submit_documents(True)
        self.enroll.set_has_passed_entrance_exam(True)
        self.enroll.set_pay_fee(True)
        self.enroll.enroll(self.DB)

        return super().setUp()

    def test_set_completed_prerequisite_courses(self):
        c1 = self.enroll.has_completed_prerequisite_senior_high_courses
        self.assertEqual(c1, True)

    def test_set_submit_documents(self):
        c2 = self.enroll.has_submitted_required_documents
        self.assertEqual(c2, True)

    def test_set_has_passed_entrance_exam(self):
        c3 = self.enroll.has_passed_entrance_exam
        self.assertEqual(c3, True)

    def test_set_pay_fee(self):
        c4 = self.enroll.has_paid_fee
        self.assertEqual(c4, True)
    
    def test_receipt(self):
        a1 = self.enroll.receipt
        self.assertEqual(a1,True)
    
    def test_db(self):
        student:Student = self.DB.retrieve__fn(self.student.first_name)
        a2 = (student is not None)
        self.assertEqual(a2,True)
            
    def test_prompt(self):
        a3 = self.enroll.prompt
        self.assertEqual(a3, False)
    
    def test_record(self):
        student:Student = self.DB.retrieve__fn(self.student.first_name)
        a4 = student.status=='Enrolled'
        self.assertEqual(a4,True)
    
    def test_reject(self):
        a5 = self.enroll.enrollment_status
        self.assertEqual(a5,'Enrolled')

if __name__ == '__main__':
    unittest.main()

##unsaon pag sulod? murag naa sa ubos... 
