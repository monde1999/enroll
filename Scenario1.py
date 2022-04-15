import unittest
from Database import Database, Student
from Enroll import Enroll
class Scenario1(unittest.TestCase):
    def setUp(self):
        self.DB = Database()
        self.student = Student(first_name='Mark', last_name='Simbajon')
        self.enroll = Enroll(self.student)
        self.enroll.set_complete_prerequisite_courses(True)
        self.enroll.set_submit_documents(True)
        self.enroll.set_has_passed_entrance_exam(True)
        self.enroll.set_pay_fee(True)
        self.enroll.enroll(self.DB)
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

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
