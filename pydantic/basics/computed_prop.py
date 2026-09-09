from pydantic import BaseModel, computed_field, Field

class Product(BaseModel):
    price:float
    quantity:int

    @computed_field # calculations or computed krne k lie use krte h 
    @property # makes accesible like attribute
    def total_price(self) -> float:
        return self.price * self.quantity
    


class Booking(BaseModel):
    user_id:int
    room_id:int
    nights:int = Field(..., ge = 1)
    rate_per_night:float


    @computed_field
    @property
    def total_amount(self)->float:
        return self.nights * self.rate_per_night

# booking = Booking(
#     user_id=123,
#     room_id=45,
#     nights=3,
#     rate_per_night=100
# )

# booking_dict = {
#     "user_id":123,
#     "room_id":344,
#     "nights":4,
#     'rate_per_night':500
# }
# booking = Booking(**booking_dict)
# print(booking.total_amount) # ye hme return krke dega price kuu ki computed and property bnaya h to calculation krke property dega
# print(booking.model_dump()) # ye hme dega complete model jo hmne bnaaya h vo 

