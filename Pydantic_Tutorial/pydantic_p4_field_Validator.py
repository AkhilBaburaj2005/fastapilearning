from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str 
    email: EmailStr
    age: int
    weight: float
    married: bool = False
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domains = ['hdfc.com', 'icici.com']
        # abc@gmail.com
        domain_name =value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Invalid domain name')
        return value

    @field_validator('name')
    @classmethod
    def name_validator(cls, value):
        return value.upper()

    @field_validator('age', mode='after')
    @classmethod
    def age_validator(cls, value):
        if 0 < value < 100:
             return value
        raise ValueError('Invalid age')
    
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
    
patient_info = { 'name': 'Akhil', 'email': 'akhil@icici.com', 'age': '30', 'weight': 70,'married': False, 'allergies': ['penicillin', 'aspirin', 'ibuprofen', 'acetaminophen', 'antihistamines'], 'contact_details': { 'phone': '1234567890'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)