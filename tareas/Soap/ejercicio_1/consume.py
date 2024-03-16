#Del ejemplo del cliente SOAP consumir el endpoint de NumberToDollars
from zeep import Client

client = Client(
  "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"
)
#NumberToDollars
result = client.service.NumberToDollars(5.0)
print(result)