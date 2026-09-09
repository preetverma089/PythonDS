# serialization is a process to convert pydantic model into easily understandable, storable process 

# Pydantic models -> Python Dict, JSON strings XML knowns as serilaization

from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street:str
    city:str
    zip_code:str


class User(BaseModel):
    id:int
    name:str
    email:str
    is_active:bool = True
    created_at: datetime
    address:Address
    tags:List[str] = []
    
    model_config = ConfigDict(
        json_encoders={datetime:lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}
    )


user = User(
    id=1,
    name = "Preet",
    email = "h@preeet.ai",
    created_at=datetime(2026,3,15, 14,30),
    address=Address(
        street="Something",
        city = "CKD",
        zip_code = "1273006"
    ),
    is_active=True,
    tags=["Premium","Subscriber"]
)

python_Dict = user.model_dump() # it converts everything into dict for readable and usable data
print(user)
print("=" * 30)
print(python_Dict)
print("=" * 30)
json_str = user.model_dump_json() # it converts model into json
print(json_str)



# Read docs for pydantic: https://pydantic.dev/docs/validation/latest/get-started/