class Student:
    def __init__(self, first_name:str='', last_name:str='', status:str=''):
        self.first_name = first_name
        self.last_name = last_name
        self.enrolled = False
        self.pending = True
        self.closed = False

    def __repr__(self):
        return "Student['%s','%s','%s']" % (self.first_name,self.last_name,self.status)

class Database:
    __data  = {}
    __count = 0

    def add(self, student:Student) -> None:
        pk = self.__generate_pk()
        self.__data[pk] = student
        self.__count += 1

    def retrieve__pk(self,pk:int) -> Student:
        if pk in self.__data: return self.__data[pk]
        else: return None

    def retrieve__name(self, fn:str, ln:str) -> Student:
        res = None
        for k, v in self.__data.items():
            if v.first_name==fn and v.last_name==ln:
                # res.append(v)
                res = v
                break
        return res

    def __generate_pk(self) -> int:
        pk =self.__count
        while pk in self.__data:
            pk += 1
        return pk
