import json
import httpx
from datetime import datetime, timedelta
from models import History
from fastapi import APIRouter, Body, HTTPException
from pydantic import BaseModel
from random import randint
from typing import Union
from models import Catalog


router = APIRouter()
secrets: Union[None, dict] = None
apiUrl = 'https://test.ecom.raiffeisen.ru/'
# apiUrl = 'https://e-commerce.raiffeisen.ru/'


@router.on_event('startup')
def startup():
    global secrets
    with open('secrets.json', 'r', encoding='utf8') as file:
        secrets = json.load(file)


class Transaction(BaseModel):
    sum: int
    info: str


class Wrapper(BaseModel):
    code: str
    qrId: str
    payload: str
    qrUrl: str


@router.post('/', response_model=Wrapper)
async def get_qr(transaction: Transaction = Body(...)):
    current_time = datetime.now()
    reg_res = httpx.post(
        apiUrl + 'api/sbp/v1/qr/register',
        json={
            # "account": 40700000000000000000,
            "additionalInfo": "Доп информация",
            "amount": 1,
            "createDate": current_time.strftime('%Y-%m-%dT%H:%M:%S+03:00'),
            "qrExpirationDate": (current_time + timedelta(minutes=5)).strftime('%Y-%m-%dT%H:%M:%S+03:00'),
            "currency": "RUB",
            "order": randint(0, 99999999999),
            "paymentDetails": "Оплата товаров",
            "qrType": "QRDynamic",
            "sbpMerchantId": secrets['MerchantId']
        }
    )
    return Wrapper(**reg_res.json())
