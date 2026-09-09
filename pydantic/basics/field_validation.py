from pydantic import BaseModel, field_validator,model_validator


class User(BaseModel):
    username:str


    @field_validator('username') # decorator, ye specific field pe lgta h 
    def username_length(cls,v): # cls:class validator, v stands for value
        if len(v) < 4:
            raise ValueError("Username must be atleast 4 chracters")
        return v

# Model Validator
class SignUp(BaseModel):
    password:str
    confirm_password:str


    @model_validator(mode='after') # mode means after field validation ye run hoga
    def password_match(cls,values):
        if values.password !=values.confirm_password:
            raise ValueError("password do not match")
        return values