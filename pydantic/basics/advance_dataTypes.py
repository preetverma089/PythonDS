# Typing is core module in python
# Data types hm dono se define kr skte h pydantic se ya typing se hm mix modules se bna skte h 

from pydantic import BaseModel
from typing import List, Dict,Optional

class Cart(BaseModel):
    user_id: int
    items: List[str]
    quantities:Dict[str, int]


class BlogPost(BaseModel):
    title:str
    content:str
    image_url: Optional[str] = None


cart_data={
    "user_id":123,
    "items":["Laptop","keyboard"],
    "quantities":{"laptop":1, "mouse":2, "keyboard":3}
}
 
cart = Cart(**cart_data)