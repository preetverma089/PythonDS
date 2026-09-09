from pydantic import BaseModel

class Product(BaseModel):
    id:int
    name:str
    price:float
    in_stock:bool = True


# Always use type Annotation and specific Type
# set sensible default

Product_one = Product(id=1, name="Laptop", price=99.99, in_stock=True)
Product_two = Product(id = 2, name='Mouse', price=56.99)
# Product_three = Product(name="keyboard") give error