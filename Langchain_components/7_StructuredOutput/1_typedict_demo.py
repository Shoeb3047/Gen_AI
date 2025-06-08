from typing import TypedDict


class Person(TypedDict):
    name:str
    age: int
    

new_person = Person(name='John Doe', age=30) 

new_person2 = Person(name=10,age='30')  # This will not raise a type error

print(new_person)
print(new_person2)  # This will not  raise a type error, as its hints does not fail.
