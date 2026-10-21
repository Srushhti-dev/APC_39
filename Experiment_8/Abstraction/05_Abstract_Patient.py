from abc import ABC, abstractmethod

class Patient(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def treatment(self):
        pass


class InPatient(Patient):
    def calculate_bill(self):
        return 5000

    def treatment(self):
        print("In-patient receives hospital treatment.")


class OutPatient(Patient):
    def calculate_bill(self):
        return 1000

    def treatment(self):
        print("Out-patient receives consultation.")


class EmergencyPatient(Patient):
    def calculate_bill(self):
        return 10000

    def treatment(self):
        print("Emergency patient receives immediate treatment.")


for patient in [InPatient(), OutPatient(), EmergencyPatient()]:
    patient.treatment()
    print("Bill:", patient.calculate_bill())
