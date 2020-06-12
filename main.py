import json
import requests
import time
from lor_deckcodes import LoRDeck, CardCodeAndCount

with open('./card_data/set1-en_us.json') as f:
  set1 = json.load(f)

with open('./card_data/set2-en_us.json') as f:
  set2 = json.load(f)

cardSet = {}

for card in set1:
  code = card['cardCode']
  cardSet[code] = card
  
for card in set2:
  code = card['cardCode']
  cardSet[code] = card

clientData = {}
hasPrinted = False

def printMessage(printedMessage):
  if not printedMessage:
    print('Make sure LoR is running with port 21337 enabled!')
    try:
      time.sleep(1)
    except KeyboardInterrupt:
      quit()


def handleData(data):
  print("test")

while True:
  try:
    req = requests.get('http://127.0.0.1:21337/positional-rectangles')
    if req.status_code == 200: 
      clientData = req.json()
      handleData(clientData)
      break
    printMessage(hasPrinted)
    hasPrinted = True
  except:
    printMessage(hasPrinted)
    hasPrinted = True

