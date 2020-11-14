import httpx
from datetime import datetime

url = 'https://test.ecom.raiffeisen.ru/api/sbp/v1/qr/register'
# url = 'https://e-commerce.raiffeisen.ru/api/sbp/v1/qr/register'

response = httpx.post(
    url,
    json={
        # "account": 40700000000000000000,
        "additionalInfo": "Доп информация",
        "amount": 1,
        "createDate": datetime.now().strftime('%Y-%m-%dT%H:%M:%S+03:00'),
            # "2019-07-22T09:14:38.107227+03:00",
        "currency": "RUB",
        "order": "1-22-333",
        "paymentDetails": "Назначение платежа",
        "qrType": "QRStatic",
        "qrExpirationDate": "2023-07-22T09:14:38.107227+03:00",
        "sbpMerchantId": "MA0000000552"
    }
)

# print(response.text)
print()
