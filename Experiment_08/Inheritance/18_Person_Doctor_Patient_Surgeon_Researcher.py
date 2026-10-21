class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Doctor(Person):
    def doctor_work(self):
        print(self.name, "treats patients.")


class Patient(Person):
    def patient_work(self):
        print(self.name, "is receiving treatment.")


class Surgeon(Doctor, Patient):
    def surgery(self):
        print(self.name, "performs surgery.")


class MedicalResearcher(Doctor, Patient):
    def research(self):
        print(self.name, "conducts medical research.")


surgeon = Surgeon("Dr. Amit", 40)
surgeon.doctor_work()
surgeon.patient_work()
surgeon.surgery()

print()

researcher = MedicalResearcher("Dr. Priya", 38)
researcher.doctor_work()
researcher.patient_work()
researcher.research()
