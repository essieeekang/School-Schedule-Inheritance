from .student import Student


# add MiddleSchoolStudent here
class MiddleSchoolStudent(Student):
    def __init__(self, name, grade, classes, gets_transportation=False):
        super().__init__(name, grade, classes)
        self.gets_transportation = gets_transportation

    def summary(self):
        student_summary = super().summary()
        transportation_summary = self.transportation_message()

        return student_summary + "\n" + transportation_summary

    def transportation_message(self):
        has_message = "has" if self.gets_transportation else "doesn't have"

        return f"{self.name} {has_message} transportation"
