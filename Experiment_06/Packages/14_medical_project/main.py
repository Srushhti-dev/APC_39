from Patient.patient import create_patient
from Patient.registration import register_patient
from Doctor.doctor import create_doctor
from Doctor.schedule import show_schedule
from Billing.bill import calculate_bill
from Billing.payment import make_payment
from MedicalRecords.records import add_record
from MedicalRecords.history import display_record

p=create_patient(101,"Amit",20)
register_patient(p)
d=create_doctor(1,"Dr. Sharma","Cardiology")
show_schedule(d)
r=add_record(101,"Regular Checkup")
display_record(r)
bill=calculate_bill(500,1000)
print("Total Bill:",bill)
make_payment(bill)
