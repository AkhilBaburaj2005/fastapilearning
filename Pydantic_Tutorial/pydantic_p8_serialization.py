from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pincode: int

class Patient(BaseModel):

    name:str
    gender: str
    age: int
    address: Address

address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pincode': 122001}

address1 = Address(**address_dict)

patient_dict = {'name': 'nitish', 'gender': 'male', 'age': 35, 'address': address1}

patient1 = Patient(**patient_dict)

temp1 = patient1.model_dump(exclude=['name', 'gender',{'address': 'city'}])

temp2 = patient1.model_dump(exclude_unset=True)
print(temp2)
print(type(temp2))
print(temp1)
print(type(temp1))

temp = patient1.model_dump_json()
print(temp)
print(type(temp))

