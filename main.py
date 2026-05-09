OPEN_WEATHER_API = "open weather api"
MAIL = "email id"
PASSWORD = "pass"
NUMBER = "phone number"
EMAIL = "to email"

account_sid = "account_sid"
auth_token = "auth_token"
MESSAGING_SERVICE_SID = "your_sid"

import requests
import smtplib
from twilio.rest import Client
response = requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast?lat=17.668268&lon=75.924339&cnt=4&appid={OPEN_WEATHER_API}")
response.raise_for_status()
data = response.json()

will_rain = False
for n in range(0, 4):
    condition_code = data["list"][n]["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("yes")
    #MAIL:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MAIL, password=PASSWORD)
        connection.sendmail(from_addr=MAIL, to_addrs=EMAIL, msg="Subject:ALERT\n\nRAIN ALERT!!")
    
    #SMS:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    messaging_service_sid=MESSAGING_SERVICE_SID,
    body="RAIN ALERT!!",
    to=f"+91{NUMBER}"
    )

    #WHATSAPP:
    message = client.messages.create(
    from_='whatsapp:+14155238886',
    body="RAIN ALERT!!!",
    to=f"whatsapp:+91{NUMBER}"
    )

    print(message.sid)
        
else:
    print("no")
