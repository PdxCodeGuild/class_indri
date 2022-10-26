print("\nBlackjack Advice")
print("===============================================")
print("""
\nAvailable card Input: 
-----------------------
A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K
""")

card_dict = {'A': 1, '2': 2, '3' :3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10 , 'J': 10, 'Q': 10, 'K': 10}


card_input_1 = input("What's your first card? ").upper()
card_input_2 = input("What's your second card? ").upper()
card_input_3 = input("What's your third card? ").upper()
 
if card_input_1 in card_dict:
    pair_1 = card_dict[card_input_1]
if card_input_2 in card_dict:
    pair_2 = card_dict[card_input_2]
if card_input_3 in card_dict:
    pair_3 = card_dict[card_input_3]   


while True:
    try:
        pair_1 = card_dict[card_input_1]
        pair_2 = card_dict[card_input_2]
        pair_3 = card_dict[card_input_3]
    except KeyError:
        print("one or more input not defined")
        break
    result = pair_1 + pair_2 + pair_3
    if result < 17:
        print(f'{result} Hit') 
    if result >= 17 and result < 21:
        print(f'{result} Stay')
    if result == 21:
        print(f'{result} Blackjack')
    if result > 21:
        print(f'{result} Already Busted')
    break
else:
    print("Input error!")




 



