from pydantic import BaseModel

# Foundations and steps
# import BaseModel
# Type Annotyations means giving attribute with type
# ALways use scatter symbols ** for all further objects
# model init(Always unpack the dict)
# Automatic Validation from pydantic
# pydantic try krta h phle convert krne ki uske type me agar nhi kr pata to error deta h 
class User(BaseModel):
    id:int
    name:str
    is_active:bool


# input_Data = {'id':101, 'name':"Preet", 'is_active':True}

# **: ye usen krte h unpack krne ke lie basically spread operator agar hm ye use nhi krenge direct dalenge
# to kya hoga hr object k lie ni bnyega ye isiliye hm ye use krte h

# user = User(**input_Data)
# print(user)

# Examples:
# input_Data = {'id':101, 'name':"Preet", 'is_active':45}
# user = User(**input_Data)
# print(user) // give me validation error pydantic_core._pydantic_core.ValidationError: 1 validation error for User

# Example_2 : Try krta h convert krne ki 
# input_Data = {'id':101, 'name':"Preet", 'is_active':"True"}
# user = User(**input_Data)
# print(user)

