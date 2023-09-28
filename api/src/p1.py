from fastapi import FastAPI
from .dtos.createroom import CreateRoom
from routes.room import router

app = FastAPI()
all_room = []

        

@app.on_event("startup")
async def startup():
    print('start')

@app.on_event("shutdown")
async def shutdown():
    print("shutdown")


 
