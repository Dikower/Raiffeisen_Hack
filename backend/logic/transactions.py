import json
import httpx
from datetime import datetime, timedelta
from models import History, Catalog
from fastapi import APIRouter, Body, HTTPException
from pydantic import BaseModel, Field
from random import randint
from typing import Union


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
    sum: int = Field(gt=0)
    info: str
    entry_code: str


class Wrapper(BaseModel):
    code: str
    qrId: str
    payload: str
    qrUrl: str


@router.post('/', response_model=Wrapper)
async def get_qr(transaction: Transaction = Body(...)):
    catalog = await Catalog.get_or_none(entry_code=transaction.entry_code)
    if catalog is None:
        raise HTTPException(404, 'Catalog not found')
    await History.create(catalog=catalog, info=transaction.info)

    current_time = datetime.now()
    reg_res = httpx.post(
        apiUrl + 'api/sbp/v1/qr/register',
        json={
            # "account": 40700000000000000000,
            "additionalInfo": "Доп информация",
            "amount": transaction.sum,
            "createDate": current_time.strftime('%Y-%m-%dT%H:%M:%S+03:00'),
            "currency": "RUB",
            "order": randint(0, 99999999999),
            "paymentDetails": "Оплата товаров",
            "qrType": "QRStatic",
            "sbpMerchantId": secrets['MerchantId']
        }
    )
    return Wrapper(**reg_res.json())


@router.get('{qrId}/payment_info')
async def get_info(qrId: str):
    info_res = httpx.get(
        apiUrl + f'api/sbp/v1/qr/{qrId}/payment-info -H "Authorization :Bearer {secrets["key"]}',
    )
    info_res = info_res.json()
    if info_res.get('path'):
        del info_res['path']
    return info_res
