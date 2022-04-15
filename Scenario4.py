import unittest
from Database import Database, Student, Enrollment
from Enroll import Enroll
class Scenario4(unittest.TestCase):
    def setUp(self):
        self.DB = Database()
        self.student = Student(first_name='Mark', last_name='Simbajon')
        self.enroll = Enroll(self.student)
        self.enroll.set_complete_prerequisite_courses(True)
        self.enroll.set_submit_documents(True)
        self.enroll.set_took_placement_entrance_exam(False)
        self.enroll.set_pay_fee(False)
        self.enroll.enroll(self.DB)
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_set_completed_prerequisite_courses(self):
        c1 = self.enroll.has_completed_prerequisite_senior_high_courses==True
        self.assertEqual(c1, True)

    def test_set_submit_documents(self):
        c2 = self.enroll.has_submitted_required_documents==True
        self.assertEqual(c2, True)

    def test_set_has_took_placement_exam(self):
        c3 = self.enroll.has_took_placement_exam == False
        self.assertEqual(c3, True)

    def test_set_pay_fee(self):
        c4 = self.enroll.has_paid_fee == False
        self.assertEqual(c4, True)
    
    def test_prompted_enrolled(self):
        a1 = self.enroll.prompted_success==False
        self.assertEqual(a1, True)

    def test_status(self):
        student:Student = self.DB.retrieve_student__pk(self.enroll.returned_pk)
        a2 = student.status == ''
        self.assertEqual(a2, True)

    def test_prompted_warning(self):
        a3 = self.enroll.prompted_warning == True
        self.assertEqual(a3, True)

    def test_pending(self):
        enrollment:Enrollment = self.DB.retrieve_enrollment__pk(self.enroll.returned_pk)
        a4 = enrollment.pending == True
        self.assertEqual(a4, True)

    def test_closed(self):
        enrollment:Enrollment = self.DB.retrieve_enrollment__pk(self.enroll.returned_pk)
        a5 = enrollment.closed == False
        self.assertEqual(a5, True)

if __name__ == '__main__':
    unittest.main()
