# self Refrencing Model or Recursive Models
# jse comment model h uske andar comment model kuu ki comment ka model same h chahe reply ku na kr rha ho

from pydantic import BaseModel
from typing import List, Optional

class Comment(BaseModel):
    id:int
    content:str
    replies:Optional[List['Comment']] = None


Comment.model_rebuild() # isko use krne se phle hmare model me vo same model use ho rha ho nhi to memory degradtion very high hogi

# ye h nested and nested model or self refrencing model
comment = Comment(
    id=1,
    content='first comment',
    replies=[
        Comment(id=2, content="reply 1"),
        Comment(id=3, content="reply 2", replies=[
            Comment(id=4, content='Nested Reply')
        ]),
        Comment(id=4, content="reply 3"),
    ]

)
print(comment)
