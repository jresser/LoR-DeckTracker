import json
import requests
import time
from os import system, name
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

hasPrinted = False
gotDeck = False
playerDeckCode = str()

def printMessage(printedMessage):
  if not printedMessage:
    print('Error: Make sure LoR is running with port 21337 enabled!')


playerDeck = {}
playerDeckCode = ""
knownIDs = []

def printDeck(playerName):
  # for windows 
  if name == 'nt': 
    _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
  else: 
    _ = system('clear')

  print('Player Name: ' + playerName)
  print('code: ' + playerDeckCode + '\n')
  cardCosts = {}
  for cardCode in playerDeck:
    cardCosts[cardCode] = cardSet[cardCode]['cost']

  for card in sorted(cardCosts.items(), key=lambda item: item[1]):
    cardName = cardSet[card[0]]['name']
    print(cardName + ": " + str(playerDeck[card[0]]))

def handleData(data):
  global playerDeckCode
  global playerDeck
  if data['GameState'] == 'InProgress':
    req = requests.get('http://127.0.0.1:21337/static-decklist')
    deckJson = req.json()
    deckCode = deckJson['DeckCode']
    # get player deck 
    if (not playerDeck) or (playerDeckCode != deckCode):
      playerDeckCode = deckCode
      deck = LoRDeck.from_deckcode(deckCode)
      for cardStr in deck:
        card = CardCodeAndCount.from_card_string(cardStr)
        playerDeck[card.card_code] = card.count

    rectangles = data['Rectangles']
    for rect in rectangles:
      if not rect['LocalPlayer']:
        continue

      if rect['CardID'] in knownIDs:
        continue
      knownIDs.append(rect['CardID'])

      cardCode = rect['CardCode']
      if cardCode not in playerDeck:
        continue

      if playerDeck[cardCode] < 1:
        continue

      playerDeck[cardCode] -= 1

    playerName = data['PlayerName']
    printDeck(playerName)

  else:
    # for windows 
    if name == 'nt': 
      _ = system('cls') 
    
    # for mac and linux(here, os.name is 'posix') 
    else: 
      _ = system('clear')

    print('Start a game to see your deck!')
    
    playerDeck = {}
    playerDeckCode = ""


while True:
  try:
    req = requests.get('http://127.0.0.1:21337/positional-rectangles')
    if req.status_code == 200: 
      clientData = req.json()
      handleData(clientData)
      time.sleep(2)
      continue

    printMessage(hasPrinted)
    hasPrinted = True
    try: 
      time.sleep(2)
    except KeyboardInterrupt:
      quit()
  except:
    printMessage(hasPrinted)
    hasPrinted = True
    try: 
      time.sleep(2)
    except KeyboardInterrupt:
      quit()
