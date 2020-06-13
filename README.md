# LoR-DeckTracker
Simple command line deck tracker for [Legends of Runeterra](https://playruneterra.com/)

## How to Run:
First, ensure you have the dependencies installed by running
```
pip install requests
pip install lor-deckcodes
```
Then, run the tracker with
```
python deck_tracker.py
```
## Known Issues:
There is currently no known way in the LoR API to detect a difference between cards created by other cards and cards originating in the player's deck. This means that cards like Used Cask Salesman, Jaull Hunters, and Yordle Grifter may cause issues if you have the created cards in your deck.

This will be fixed with either an update to the LoR API, or hard-coding all of these interactions, which is a long-term goal.

## Upcoming Features (To-do List)
- Add support for tracking wins/losses with a deck, and saving user data
- Track opponent deck
- Guess opponent's deck by pulling data from [Mobalytics](https://lor.mobalytics.gg/)
- Add a GUI
