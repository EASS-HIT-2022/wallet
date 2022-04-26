import time
from fastapi import FastAPI
from enum import Enum, IntEnum
from pydantic import BaseModel

#Clock request
class RequestClock(BaseModel):
    id: int
    zone: str

# client-pay&pray
class NusachEnum(str, Enum):
    MZ= 'mizrach'
    SP = 'sfard'
    EZ= 'ashkenaz'


class RequestClient(BaseModel):
    id1: int
    balance1: float
    nusach1: NusachEnum=NusachEnum.MZ #default-changeable
    location1: str

    id2: int
    balance2: float
    nusach2: NusachEnum=NusachEnum.SP #default-changeable
    location2: str

    amount: float

app = FastAPI()

@app.get("/")
async def get_root():
    print(get_root)
    return {"Hello World": "demo-backend"}

@app.post("/v1/clock")
async def clock(req: RequestClock):
    return {"clock":time.asctime(),"req.zone":req.zone}

@app.post("/v1/pay")
def pay(req:RequestClient):
    if req.balance1 > req.amount :
        print("your request to charity approved:","-",req.amount)
        req.balance1=req.balance1-req.amount
        req.balance2=req.balance2+req.amount
    return {
    'id_from': req.id1,'balance_from': req.balance1,
    'id_to': req.id2,'balance_to': req.balance2,
    'amount':req.amount}


  

  

