def card_conv(card):
    """"
    takes card input and turns it into a int 
    """
    if card == "j":
        card = 10
    elif card == "k":
        card = 10
    elif card == "q":
        card = 10
    elif card == "a":
        card = 1
    elif card == "0":
        card = 0
    elif card == "1":
        card = 1
    elif card == "2":
        card = 2
    elif card == "3":
        card = 3
    elif card == "4":
        card = 4
    elif card== "5":
        card = 5
    elif card== "6":
        card = 6
    elif card == "7":
        card = 7
    elif card == "8":         
        card = 8
    elif card == "9":
        card = 9
    elif card == "10":
        card = 10
    else:
        print("invalid input accepted inputs are # 1-10 and j,q,k,a")
    return card

def blackjack_advice():
    """"
    asks what cards you have adds them together then gives advice on what to do.
    """
    card1 = input("whats your first card? ")
    card1 = card_conv(card1)
    card2 = input("whats your second card? ")
    card2 = card_conv(card2)
    card3 = input("whats your third card? ")
    card3 = card_conv(card3)
    cardtotal=card1+card2+card3
    if cardtotal > 21 :
        print(f"{cardtotal} already bust")
    elif cardtotal == 21 :
        print(f"{cardtotal} blackjack") 
    elif cardtotal < 17 :
        print(f"{cardtotal} hit")
    elif cardtotal >= 17:
        print(f"{cardtotal} stay")

blackjack_advice()