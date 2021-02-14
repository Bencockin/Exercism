class School:

    def __init__(self):
        self.reg = {}

    def add_student(self, name, grade):

        self.name = name
        self.grade = grade

        self.reg[self.name] = self.grade

    def roster(self):
        
        grade1 = [key for key , value in sorted(self.reg.items()) if value == 1]
        grade2 = [key for key , value in sorted(self.reg.items()) if value == 2]
        grade3 = [key for key , value in sorted(self.reg.items()) if value == 3]

        result = grade1 + grade2 + grade3
        
        return result

    def grade_(self, grade_number):

        self.grade_number = grade_number

        return [key for key, value in self.reg.items() if value == self.grade_number]