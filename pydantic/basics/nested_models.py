# Nested Models: ek pydantic model ke andar dusra pydantic model

from typing import List, Optional
from pydantic import BaseModel

# also known as Hiearchical Data Structures

class Address(BaseModel):
    street:str
    city:str
    postal_code:str


class User(BaseModel):
    id:int
    name:str
    address:Address


address = Address(
    street='123',
    city='ckd',
    postal_code='127306'
)

user = User(
    id =101,
    name = "Preet",
    address=address,
)

user_data = {
    'id':1,
    'name':"Prince",
    'address':{
        'street':'321 something',
        'city':'Rohtak',
        'postal_code':'30003'
    }
}

user = User(**user_data)
print(user)