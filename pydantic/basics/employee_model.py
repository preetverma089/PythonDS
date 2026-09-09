# Field in pydantic
from typing import Optional
from pydantic import BaseModel, Field
import re
# basically field ka use krte h hm hmari attribute pe validations lgana jst like zod, express validator in js
# some keys in field: gt, gte, lt, lte, min.length, max.length, regex, description(PLaceholder)
class Employee(BaseModel):
    id:int
    name:str = Field(
        ..., # means required field or manadatory Field
        min_length=3,
        max_length=50,
        description="Employee Name",
        examples="Preet Verma"
    ),
    department:Optional[str] = "General"
    salary:float = Field(
        ...,
        ge=10000,
        le=100000
    )
# regexr: website for regex
class User(BaseModel):
    email:str = Field(
        ...,
        regex = r''
    )
    phone:str = Field(
        ...,
        regex = r''
    )
    age:int = Field(
        ...,
        ge=0,
        le=150,
        description="age in years"
    )
    discount:float = Field(
        ...,
        ge= 0,
        le = 100,
        description="discount Percentage"
    )