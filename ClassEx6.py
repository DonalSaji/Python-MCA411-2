class Account: 
	pass
a1=Account()
a2=Account()
a1.name="DOnal"
a1.balance=10000

a2.surname="saji"
a2.value=100010
a2.balance=1200

'''print(id(Account))

print(a2)
print(a1.balance)
print(a2.surname)
'''


class Patient:
	def __init__(self,patient_id,name,age,diagnosis):
		self.patient_id=patient_id
		self.name=name
		self.age=age
		self.diagnosis=diagnosis

	def display(self):
		print(self.patient_id)
		print(self.name)
		print(self.age)
		print(self.diagnosis)
	def is_senior():
		return self.age>=60
		


class Student:
#cal total and avg, student details , display pass or fail
	
	def __init__(self,name,reg,m1,m2,m3):
		self.name=name
		self.reg=reg
		self.m1=m1
		self.m2=m2
		self.m3=m3

	def display(self):
		print(self.name)
		print(self.reg)
		print(self.m1)
		print(self.m2)
		print(self.m3)

	def cal(self):
		print("total : ", self.m1+self.m2+self.m3)
		print("avg : ", (self.m1+self.m2+self.m3)/3)


	def is_pass(self):
		return (self.m1+self.m2+self.m3)/3>=40


print("Christ university")
p1=Student("Donal",23456,89,89,87)

p1.display()
p1.cal()
print("Student result: ",p1.is_pass())



class Patient:

 def display(self):
  print("Patient details")

p1=Patient()
p1.display()

class Patient:
 hospital_name="ABC HOSPITAL"

 @classmethod
 def display_hospital(cls):
  print(cls.hospital_name)
Patient.display_hospital()



class Patient:
 @staticmethod
 def hospital_timings():
  print("Hospital Timing:9AM - 5PM")

Patient.hospital_timings()

#single inheritance
class Patient:
 def show_patient(self):
  print("Patient_Id:P101")
  print("Name:Ananya")

class Inpatient(Patient):
 def show_room(self):
  print("Room Number:205")

patient=Inpatient()
patient.show_room()

#multiple inheritance
class Patient:
 def patient_details(self):
  print("Patient Name:Ananya")

class Billing:
 def billing_details(self):
  print("Consulatation fee:500")

class HospitalRecord(Patient,Billing):
 def record_details(self):
  print("Hospital Record Generated")

record=HospitalRecord()

record.patient_details()
record.billing_details()
record.record_details()


