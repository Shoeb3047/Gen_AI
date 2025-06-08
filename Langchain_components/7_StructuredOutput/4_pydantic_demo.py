from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name: str = 'nitish'  # Basic field with default value
    age: Optional[int] = None # Optional field, can be None
    email: EmailStr   # In build validator for email
    cgpa: float = Field(gt=0, lt=10, default=5, description='A decimal value representing the cgpa of the student') 


# new_student = {'age':'32', 'email':'abc@gmail.com'}

new_student = {"age":'32', 'email':'xyz@gmail.com','cpga': 12}          
student = Student(**new_student)

print("-*-" * 50)  
print(student, type(student))

print("-*-" * 50)  
# Converting to dictionary
# This will convert the pydantic model to a dictionary
student_dict = student.model_dump()
print(student_dict, type(student_dict))


print("-*-" * 50)  
# Converting to JSON
# This will convert the pydantic model to a JSON string
student_json = student.model_dump_json()
print(student_json, type(student_json))

print("-*-" * 50)  