card_values={
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10
}

def message(first_card: int, second_card: int, third_card: int):
    '''Function needs three int, and takes the value of the three cards from the user and
    lets the user know what they should do in the game
    '''
    hand_value=first_card + second_card+ third_card
    statement=''
    if hand_value>21:
        statement= "Already Busted"
    elif hand_value==21:
        statement="Blackjack!"
    elif hand_value<=17:
        statement= "Hit"
    elif hand_value>=17:
        statement="Stay"
    #I print the out put statement here
    print(f'{hand_value}, {statement}')


#From line 35 to 41 I get the cards from user and get their values for dirct
while True:
    try:
        first_card = input("What's your first card?: ").upper()
        first_card_value=card_values[first_card]
        second_card = input("What's your second card?: ").upper()
        second_card_value=card_values[second_card]
        third_card = input("What's your third card?: ").upper()
        third_card_value=card_values[third_card]
    except KeyError:
        exit=input('Your input was not a card choice. Do you want to continue? (Y or N)').upper()
        if exit == 'N':
            print('Goodbye!')
            break
#I call the function here
    message(first_card_value,second_card_value, third_card_value)
