from django.shortcuts import render
import os
from django.http import HttpResponse
import base64
import json
import requests
def credential(request):
    client_id = "mRoJuiWEnweAzd4bSie8ZBjS3TPTIonYqAvIlhne"
    secret = "pbkdf2_sha256$600000$qBvcKwRNNwCRX0gM6ShAUf$ofjhCMsZzCjCUt3DNRfvIUNymgGEHbHDqmIyITrKfZQ="
    credential = "{0}:{1}".format(client_id, secret)
    CREDENTIAL=base64.b64encode(credential.encode("utf-8"))
    headers={
      "Authorization: Basic ${CREDENTIAL}"
      "Cache-Control: no-cache"
      "Content-Type: application/x-www-form-urlencoded"
    }
    token_url = "http://127.0.0.1:8000/o/token/"
    data=json.dumps({
    "grant_type=client_credentials",
    })
    response =requests.request("POST",token_url,headers=headers,data=data)
    print(type(response))
    #print(response.json())
    #access_token = response.json()["access_token"]

def twit_post(request):
      url = "https://api.twitter.com/2/tweets"
      payload = json.dumps({
        "text": "hi."
        })
      headers = {
        'Authorization': 'OAuth oauth_consumer_key="5JUG4JTLl8LVxOje0sj9KHd5E",oauth_token="1465344450763243520-J7Nul9W9F7m9QKueTtgMy79Ct2kONE",oauth_signature_method="HMAC-SHA1",oauth_timestamp="1694775693",oauth_nonce="JqTADDsDo77",oauth_version="1.0",oauth_signature="xgU79q2qAuD7gY7Y0MGEs7eY1cQ%3D"',
        'Content-Type': 'application/json',
        'Cookie': 'ct0=d1742fa4caa6c445bf95a7717d5cbad3; guest_id=v1%3A169477469610506790; guest_id_ads=v1%3A169477469610506790; guest_id_marketing=v1%3A169477469610506790; personalization_id="v1_f3Z3q4TQVZjDe3v5/UIKsw=="'
        }
      response = requests.request("POST", url, headers=headers, data=payload)

      print(response.text)

      return HttpResponse("Tweet posted successfully")
def post(request):
  '''client_id = "Sbbbck6lB5CjOFwvpDrlNYSgBaAj2ujEldXnpUYD"
  secret = "pbkdf2_sha256$600000$v0nHkcf0px6EpJXX7V4h2a$Bl1/uixQNDgiS86YbnGjWjmjAUkV0vZPVsM0ZmRUOnU="
  credential = "{0}:{1}".format(client_id, secret)
  CREDENTIAL=base64.b64encode(credential.encode("utf-8"))
  print(CREDENTIAL)
  headers= {
    'Authorization': 'BasicU2JiYmNrNmxCNUNqT0Z3dnBEcmxOWVNnQmFBajJ1akVsZFhucFVZRDpwYmtkZjJfc2hhMjU2JDYwMDAwMCR2MG5Ia2NmMHB4NkVwSlhYN1Y0aDJhJEJsMS91aXhRTkRnaVM4NllibkdqV2ptakFVa1YwdlpQVnNNMFptUlVPblU9',
    'Cache-Control': 'no-cache',
    'Content-Type': 'application/x-www-form-urlencoded',
    }

  data = {
    'grant_type':'client_credentials',
  }

  response = requests.post('http://127.0.0.1:8000/o/token/', headers=headers, data=data)
  return HttpResponse(response)'''
def acc(request):
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    }

  data = 'grant_type=client_credentials&client_id=<Sbbbck6lB5CjOFwvpDrlNYSgBaAj2ujEldXnpUYD>client_secret=<pbkdf2_sha256' + os.getenv('600000', '') + os.getenv('v0nHkcf0px6EpJXX7V4h2a', '') + os.getenv('Bl1', '') + '/uixQNDgiS86YbnGjWjmjAUkV0vZPVsM0ZmRUOnU=>'

  response = requests.post('http://127.0.0.1:8000/o/token/', headers=headers, data=data)
  return HttpResponse(response)
