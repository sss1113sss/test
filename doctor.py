from patient import Patient

class Doctor(Patient):
    def __init__(self, ismi, familyasi, ssn, id, speciality) -> None:
        self._id = id
        self._speciality = speciality
        self._count = 0
        self._patient_list: list[Patient] = []
        super().__init__(ismi, familyasi, ssn)

    @property
    def id(self):
        return self._id
    
    @property
    def speciality(self):
        return self._speciality
    
    def addpatient(self, patient,count):
        self._patient_list.append(patient)
        print('doctorga patient biriktirildi')
        count+=1

    def getpatients(self):
        return self._patient_list
    
    def __str__(self) -> str:
        return super().__str__()
    def idledoctors(self):
        if self._count==0:
            return sorted(self._ismi),self._familyasi
    def busydoctors(self):
        return   sorted(self._ismi),self._familyasi     
    def doctorsbynumpatient(self):
        return sorted(self._count,reverse=True),self._familyasi,self._ismi    
    def countpatientperspecal(self):
        return sorted(self._count,reverse=True) ,self._speciality