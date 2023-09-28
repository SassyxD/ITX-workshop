from fastapi import APIRouter
from ..dtos.createroom import CreateRoom
 


all_room = []
router = APIRouter()

@router.get('/sassyxd/{NumID}')
async def getInfo(NumID: int):
    id = int(NumID)
    return 'Nongmaynarak' + str(id+100)

@router.post('/createroom')
async def createroom(create_room: CreateRoom):
    print(create_room)
    # all_room.append({
    #     'room_id':207 + len(all_room),
    #     'member' :'Grey'
    # })
    return create_room  

@router.delete('/remove/{NumID}')
async def deleteroom(NumID):
    all_room.pop(int(NumID))
    return all_room

@router.put('/edit_owner/{NumID}')
async def updateroom(index):
    all_room[int(index)]['member']
        



