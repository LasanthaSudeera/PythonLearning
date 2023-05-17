class Docter:
    def __init__(self, name, speciality):
            self.name = name
            self.speciality = speciality
            self.patients = []

    def getPatients(self):
          return self.patients
    
    def addPatient(self, patient):
          self.patients.append(patient)

    def printPatients(self):
          for i in range(len(self.patients)):
                print("Name: {} Age: {}".format(self.patients[i].name, self.patients[i].age))
        
class Patient:
      def __init__(self, name, age):
            self.name = name
            self.age = age


# Docter
doc = Docter("John Doe", "MMBS")

# Patients
p1 = Patient("Jane Doe", 19)
p2 = Patient("Jene Doe", 45)

doc.addPatient(p1)
doc.addPatient(p2)

print("Doc details: ", doc.name)
print("Patients: ")
doc.printPatients()