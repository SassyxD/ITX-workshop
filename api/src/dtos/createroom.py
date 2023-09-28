#data transfer object
from pydantic import BaseModel

class CreateRoom(BaseModel):
    room_id: int
    status: bool
    user: str