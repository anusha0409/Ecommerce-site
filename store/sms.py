import os
from twilio.rest import Client
import math,random


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure

def gen_otp():
    digits= "0123456789"
    OTP=""
    for i in range(6):
        OTP+= digits[math.floor(random.random()*10)]
    return OTP




def send_sms(body_,from__, to_):
    account_sid = 'AC95f177e36ef0c9e96dd113ccf275293b'
    auth_token = '5e91cdc06c825aff50d63b940fa4552f'
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body=body_,
                     from_= from__,
                     to=to_
                 )
