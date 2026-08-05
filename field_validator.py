from pydantic import BaseModel,EmailStr,Field,field_validator
from typing import List, Dict,Annotated

class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]

    @field_validator("email")
    @classmethod
    def email_validator(cls,value):
        valid_domains=["hdfc.com","icici.com"]
        #abc@gmail.com
        domain_name=value.split("@")[-1]

        if domain_name not in valid_domains:
         raise ValueError("Not a valid domain")
        return value


def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print("inserted")
    
patient_info = {
        "name": "ali",
        "age": 30,
        "email":"abc@hdfc.com",
        "weight": 92.5,
        "married": True,
        "allergies": ["pollan", "dust"],
        "contact_details": {
         "phone_no": "12345"
        }
}
    
patient1 = Patient(**patient_info)
    
insert_patient_data(patient1)