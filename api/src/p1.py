from fastapi import FastAPI
from .dtos.createroom import CreateRoom

app = FastAPI()
all_room = []

@app.post('/createroom')
async def createroom(create_room: CreateRoom):
    print(create_room)
    return create_room  

@app.get('/sassyxd/{NumID}')
async def getInfo(NumID: int):
    id = int(NumID)
    return 'Nongmaynarak' + str(id+100)

@app.delete('/remove/{NumID}')
async def deleteroom(NumID):
    all_room.pop(int(NumID))
    return all_room

@app.put('/edit_owner/{NumID}')
async def updateroom(index):
    all_room[int(index)]['member']
        

@app.on_event("startup")
async def startup():
    print('start')

@app.on_event("shutdown")
async def shutdown():
    print("shutdown")


from fastapi import FastAPI

app = FastAPI()
all_room = [] 
