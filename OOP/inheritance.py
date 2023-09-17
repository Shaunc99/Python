class Person:
    def __init__(self, firstname, lastname):
        self.firstName = firstname
        self.lastName = lastname
    def printName(self):
        print(self.firstName, f" {self.lastName}")


class Student(Person):
    def __init__(self,firstname,lastname, graduationYear, schoolName):
        super().__init__(firstname, lastname)
       
        self.graduationYear = graduationYear
        self.schoolName = schoolName

class Doctor(Person):
    def __init__(self,firstname,lastname, speciality, university):
        super().__init__(firstname, lastname)
       
        self.speciality = speciality
        self.university = university


studentObj = Student("Shayan","Qureshi",2004, "ST Paul's")

print(studentObj.printName())