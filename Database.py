class Student:
    def __init__(self, first_name:str='', last_name:str='', status:str=''):
        self.first_name = first_name
        self.last_name = last_name
        self.status = status

    def __repr__(self):
        return "Student['%s','%s','%s']" % (self.first_name,self.last_name,self.status)

class Enrollment:
    def __init__(self, student_pk:int):
        self.student_pk = student_pk
        self.pending = True
        self.closed = False

class Database:
    __data_student  = {}
    __data_enrolment = {}
    
    __count = 0

    def add_student(self, student:Student) -> None:
        pk = self.__generate_pk()
        self.__data_student[pk] = student
        self.__count += 1
        return pk
    
    def add_enrollment(self, student_pk:int) ->None:
        self.__data_enrolment[student_pk] = Enrollment(student_pk)
    
    def retrieve_enrollment__pk(self, pk:int)->Enrollment:
        return self.__data_enrolment.get(pk, None)

    def retrieve_enrollment__student(self,student:Student)->Enrollment:
        res = None
        if student == None: return None
        for k, v in self.__data_enrolment.items():
            if v.student.first_name==student.first_name and v.student.last_name==student.last_name:
                res = v
                break
        return res

    def retrieve_student__pk(self,pk:int) -> Student:
        if pk in self.__data_student: return self.__data_student[pk]
        else: return None

    def retrieve_student__name(self, fn:str, ln:str) -> Student:
        res = None
        for k, v in self.__data_student.items():
            if v.first_name==fn and v.last_name==ln:
                # res.append(v)
                res = v
                break
        return res

    def __generate_pk(self) -> int:
        pk =self.__count
        while pk in self.__data_student:
            pk += 1
        return pk
