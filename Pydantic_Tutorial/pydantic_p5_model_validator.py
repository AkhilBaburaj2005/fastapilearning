from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool = False
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return model

def insert_patient(patient: Patient):

     print(patient.name)
     print(patient.email)
     print(patient.age)
     print(patient.weight)
     print(patient.married)
     print(patient.allergies)
     print(patient.contact_details)
     print('inserted')

def update_patient_data(patient: Patient):

     print(patient.name)
     print(patient.email)
     print(patient.age)
     print(patient.weight)
     print(patient.married)
     print(patient.allergies)
     print(patient.contact_details)
     print('updated')
    
patient_info = { 'name': 'Akhil', 'email': 'akhil@icici.com', 'age': '61', 'weight': 70,'married': False, 'allergies': ['penicillin', 'aspirin', 'ibuprofen', 'acetaminophen', 'antihistamines'], 'contact_details': { 'phone': '1234567890', 'emergency': '1234567890'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)