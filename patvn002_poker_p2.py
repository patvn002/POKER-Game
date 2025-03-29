#
# File - patvn002_poker_p1.c
# Author - Vraj Patel
# Email ID - patvn002@mymail.unisa.edu.au
# Assignment Description - 
# This is my own work as defined by the University's
# Academic Misconduct Policy 
#


import dice       # this module lets the user display the player hand as well as dealer hand 
import random     # this module lets the user generate random numbers within a defined range 


def display_details():
  print("File - patvn002_poker_p1.c")
  print("Author - Vraj Patel")
  print("Email ID - patvn002@mymail.unisa.edu.au")
  print("This is my own work as defined by the University's")
  print("Academic Misconduct Policy") 
  print()

display_details()

def roll_die():
    import random
    die = random.randint(1,6)

# the below line determines whether the user wants to play the game or not 
ques = str(input("Do you want to play a game? [y/n]? "))
print()
print()

# this loop will prompt the user to write the correct alphabet and will ask again if the user entered incorrect input 
while ques != 'y' and ques != 'n':
    print("Please enter either 'y' or 'n'." )
    ques = str(input("Do you want to play a game? [y/n]? "))

# this line works when the user inputs "n" before playing a single game    
if ques == "n":
    print("No worries... another time perhaps... :)")


elif ques == "y":    # if the user inputs "y" then the game will begin 
    player_hand=[]
    die_count = [0,0,0,0,0,0,0]
    # the below loop helps in iterating within the list to fill the "player_hand" list with random generated valuse from 1-6
    for i in range(0,5):                               
        player_hand.append(random.randint(1,6))
        die_value = player_hand[i]    
        die_count[die_value] += 1      # it helps in incrementing the die value in the die count 
    print("Player's Hand: ")
    dice.display_hand(player_hand)

    # this helps with the output of full house when there are two pairs of 3 and 2
    pair_count = 0  
    for pair in die_count:
        if pair == 2:
            pair_count +=1

    # this indicated the stars for every rank 
    star = "*"
    str6 = " "
    str5 = " "
    str4 = " "
    str3 = " "
    str2 = " "
    str1 = " "
    str0 = " "
    player_rank = 0

    # this logic is referenced by web search and has a few changes done by me for my above loops 
        
    if 5 in die_count:                                    # Rank 6 : Five of a kind
        player_rank = 6
        str6 = str6 + star
    elif 4 in die_count:                                  # Rank 5 : Four of a kind
        player_rank = 5
        str5 = str5 + star
    elif pair_count == 1 and 3 in die_count:              # Rank 4 : Full House 
        player_rank = 4
        str4 = str4 + star
    elif 3 in die_count:                                  # Rank 3 : Three of a kind
        player_rank = 3
        str3 = str3 + star
    elif pair_count == 2:                                 # Rank 2 : Two Pair
        player_rank = 2
        str2 = str2 + star
    elif pair_count == 1:                                 # Rank 1 : One Pair
        player_rank = 1
        str1 = str1 + star
    # Rank 0 : Nothing Special 
    elif die_count[0] <= 1 and  die_count[1] <= 1 and die_count[2] <= 1 and die_count[3] <= 1 and die_count[4] <= 1 and die_count[5] <= 1 and die_count[6] <= 1 :                                                  
        player_rank = 0
        str0 = str0 + star

    print()

    # this indicates the dealer hand same as the player hand above 
    dealer_hand=[]
    die_count = [0,0,0,0,0,0,0]
    for k in range(0,5):
        dealer_hand.append(random.randint(1,6))
        die_value = dealer_hand[k]
        die_count[die_value] += 1
    print("Dealer's Hand: ")
    dice.display_hand(dealer_hand)    
    pair_count = 0
    for pair in die_count:
        if pair == 2:
            pair_count +=1
    dealer_rank = 0
            
    if 5 in die_count:                                    # Rank 6 : Five of a kind
        dealer_rank = 6
    elif 4 in die_count:                                  # Rank 5 : Four of a kind
        dealer_rank = 5
    elif 3 in die_count:                                  # Rank 3 : Three of a kind
        dealer_rank = 3
    elif pair_count == 2:                                 # Rank 2 : Two Pair
        dealer_rank = 2
    elif pair_count == 1:                                 # Rank 1 : One Pair
        dealer_rank = 1
    elif 3 in die_count and pair_count == 1:              # Rank 4 : Full House 
        dealer_rank = 4
    # Rank 0 : Nothing Special
    elif die_count[0] <= 1 and  die_count[1] <= 1 and die_count[2] <= 1 and die_count[3] <= 1 and die_count[4] <= 1 and die_count[5] <= 1 and die_count[6] <= 1 :                                                     
        dealer_rank = 0
    print()

    if player_rank == 6:                                   # this will display the rank name on the screen for player hand 
        print("-- Player has Five of a kind")
    elif player_rank == 5:
        print("-- Player has Four of a kind")
    elif player_rank == 4:
        print("-- Player has Full House")
    elif player_rank == 3:
        print("-- Player has Three of a kind")
    elif player_rank == 2:
        print("-- Player has Two Pairs")
    elif player_rank == 1:
        print("-- Player has One Pair")
    else:
        print("-- Player has Nothing Special")


    if dealer_rank == 6:                                  # this will display the rank name on the screen for dealer hand  
        print("-- Dealer has Five of a kind")
    elif dealer_rank == 5:
        print("-- Dealer has Four of a kind")
    elif dealer_rank == 4:
        print("-- Dealer has Full House")
    elif dealer_rank == 3:
        print("-- Dealer has Three of a kind")
    elif dealer_rank == 2:
        print("-- Dealer has Two Pairs")
    elif dealer_rank == 1:
        print("-- Dealer has One Pair")
    else:
        print("-- Dealer has Nothing Special")

    print()

    # this allows to know who won,lost or drawn the round of dice poker 
    if player_rank > dealer_rank:
        print("** Player wins! **")
        Games_won +=1
    elif player_rank < dealer_rank:
        print("** Dealer wins! **")
        Games_lost +=1
    else:
        print("** Draw **")
        Games_drawn +=1

    # this is for counting the games played 
    Games_num +=1
    print()
    print()

# this indicates if the game is played more than 1 time and ask the user to play the game again
while Games_num >= 1:
    play_game_again = str(input("Play again [y/n]?"))
    print()
    while play_game_again != 'y' and play_game_again != 'n':
        print("Please enter either 'y' or 'n'." )
        play_game_again = str(input("Play again [y/n]?"))
    
    # same logic and game code as above 
    if play_game_again == 'y':
        player_hand=[]
        die_count = [0,0,0,0,0,0,0]
        for i in range(0,5):
            player_hand.append(random.randint(1,6))
            die_value = player_hand[i]
            die_count[die_value] += 1
        
        print("Player's Hand: ")
        dice.display_hand(player_hand)
        
        pair_count = 0
        for pair in die_count:
            if pair == 2:
                pair_count +=1


        player_rank = 0
            
        if 5 in die_count:                                    # Rank 6 : Five of a kind
            player_rank = 6
            str6 = str6 + star
        elif 4 in die_count:                                  # Rank 5 : Four of a kind
            player_rank = 5
            str5 = str5 + star
        elif 3 in die_count:                                  # Rank 3 : Three of a kind
            player_rank = 3
            str3 = str3 + star
        elif pair_count == 2:                                 # Rank 2 : Two Pair
            player_rank = 2
            str2 = str2 + star
        elif pair_count == 1:                                 # Rank 1 : One Pair
            player_rank = 1
            str1 = str1 + star
        elif pair_count == 1 and 3 in die_count:              # Rank 4 : Full House 
            player_rank = 4
            str4 = str4 + star
        # Rank 0 : Nothing Special
        elif die_count[0] <= 1 and  die_count[1] <= 1 and die_count[2] <= 1 and die_count[3] <= 1 and die_count[4] <= 1 and die_count[5] <= 1 and die_count[6] <= 1 :                                                 
            player_rank = 0
            str0 = str0 + star


        dealer_hand=[]
        die_count = [0,0,0,0,0,0,0]
        for k in range(0,5):
            dealer_hand.append(random.randint(1,6))
            die_value = dealer_hand[k]
            die_count[die_value] += 1
        
        print("Dealer's Hand: ")
        dice.display_hand(dealer_hand)    
        pair_count = 0
        for pair in die_count:
            if pair == 2:
                pair_count +=1
        dealer_rank = 0
                
        if 5 in die_count:                                    # Rank 6 : Five of a kind
            dealer_rank = 6
        elif 4 in die_count:                                  # Rank 5 : Four of a kind
            dealer_rank = 5
        elif 3 in die_count:                                  # Rank 3 : Three of a kind
            dealer_rank = 3
        elif pair_count == 2:                                 # Rank 2 : Two Pair
            dealer_rank = 2
        elif pair_count == 1:                                 # Rank 1 : One Pair
            dealer_rank = 1
        elif 3 in die_count and pair_count == 1:              # Rank 4 : Full House 
            dealer_rank = 4
        # Rank 0 : Nothing Special
        elif die_count[0] <= 1 and  die_count[1] <= 1 and die_count[2] <= 1 and die_count[3] <= 1 and die_count[4] <= 1 and die_count[5] <= 1 and die_count[6] <= 1 :                                                     
            dealer_rank = 0


        if player_rank == 6:
            print("-- Player has Five of a kind")
        elif player_rank == 5:
            print("-- Player has Four of a kind")
        elif player_rank == 4:
            print("-- Player has Full House")
        elif player_rank == 3:
            print("-- Player has Three of a kind")
        elif player_rank == 2:
            print("-- Player has Two Pairs")
        elif player_rank == 1:
            print("-- Player has One Pair")
        else:
            print("-- Player has Nothing Special")


        if dealer_rank == 6:
            print("-- Dealer has Five of a kind")
        elif dealer_rank == 5:
            print("-- Dealer has Four of a kind")
        elif dealer_rank == 4:
            print("-- Dealer has Full House")
        elif dealer_rank == 3:
            print("-- Dealer has Three of a kind")
        elif dealer_rank == 2:
            print("-- Dealer has Two Pairs")
        elif dealer_rank == 1:
            print("-- Dealer has One Pair")
        else:
            print("-- Dealer has Nothing Special")



        if player_rank > dealer_rank:
            print("** Player wins! **")
            Games_won +=1
        elif player_rank < dealer_rank:
            print("** Dealer wins! **")
            Games_lost +=1
        else:
            print("** Draw **")
            Games_drawn +=1

        Games_num +=1
    print()

# if the user inputs "n" after playing number of games     
    if play_game_again == 'n':
        print("Game Summary")
        print("------------")
        print("------------")
        # this give the score board of the games played 
        print("You played",Games_num,"games")
        print("  |--> Games won:   ",Games_won)
        print("  |--> Games lost:  ",Games_lost)
        print("  |--> Games_drawn: ",Games_drawn)
        print("  Hand Stats: ")
        print("  -----------")
        print("  Nothing Special: ",str0)
        print("  One Pair: ",str1)
        print("  Two Pair: ",str2)
        print("  Three of a kind: ",str3)
        print("  Full House: ",str4)
        print("  Four of a kind: ",str5)
        print("  Five of a kind: ",str6)
        print()
        print("Thanks for playing!")
        break






    
  










