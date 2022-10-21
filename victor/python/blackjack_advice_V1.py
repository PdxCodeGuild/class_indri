num_cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
face_cards = ["A", "J", "Q", "K"]


def advisor(card):
    if card in num_cards:
        card_value = num_cards.index(card) + 1
        return card_value 
    elif card == "A":
        card_value = 1
        return card_value 
    elif card in face_cards:
        card_value = 10
        return card_value 


card1 = advisor(input("What is your first card? ").upper())
card2 = advisor(input("What's your second card? ").upper())
card3 = advisor(input("What's your third card? ").upper())

hand = card1 + card2 + card3

if hand == 21:
    print(hand, "Blackjack!")
elif hand > 21:
    print(hand, "Already Busted")
elif hand < 17:
    print(hand, "Hit")
elif hand >= 17:
     print(hand, "Stay")
