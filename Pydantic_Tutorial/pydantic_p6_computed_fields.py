from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    height: float
    married: bool = False
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height ** 2), 2)
        return bmi

def insert_patient(patient: Patient):

     print(patient.name)
     print(patient.email)
     print(patient.age)
     print(patient.weight)
     print(patient.height)
     print(patient.married)
     print(patient.allergies)
     print(patient.contact_details)
     print('inserted')

def update_patient_data(patient: Patient):

     print(patient.name)
     print(patient.email)
     print(patient.age)
     print(patient.weight)
     print(patient.height)
     print(patient.married)
     print(patient.allergies)
     print(patient.contact_details)
     print('BMI', patient.bmi)
     print('updated')
    
patient_info = { 'name': 'Akhil', 'email': 'akhil@icici.com', 'age': '61', 'weight': 70,'height': 1.75,'married': False, 'allergies': ['penicillin', 'aspirin', 'ibuprofen', 'acetaminophen', 'antihistamines'], 'contact_details': { 'phone': '1234567890', 'emergency': '1234567890'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)