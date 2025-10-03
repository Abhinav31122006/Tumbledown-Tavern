import random
scoreWOTH = 0
scoreTNS = 0
scoreTB7 = 100
while True:
  print('''
                          Tumbledown Tavern
                          
  Welcome to the Tumbledown Tavern!
  
  1> War of the Hand
  2> The Number Sieve
  3> Trial by Seven
  4> Check Scores
  0> Quit
  ''')
  
  choice = int(input('What would you like to do? '))
  print()
  print()
  if choice == 1:
    print("                    War of the Hand")
    print('''
        This is a duel of hands. Outwit the tavern's champion!
        - Rock (1) crushes Scissors.
        - Paper (2) covers Rock.
        - Scissors (3) cuts Paper.
    ''')
    wins = ["A cunning move! The victory is yours.","Masterfully played! You've bested the house.","Your strategy prevails!", "Well played! The tavern cheers for you."]
    losses = ["Outplayed! The house's trickery wins this time.","A clever feint from your opponent.","Your opponent saw through your plan.","Defeated! Better luck next round, traveler."]
    while True:
      print()
      print()
      print("(ENTER 1:rock, 2:paper, 3:scissors, 0:quit)")
      print("Score:", scoreWOTH)
      print()
      player = int(input("What do you choose? "))
      print()
      comp=random.randint(1,3)
      c=0
      if player == 1:
        if comp== 3:
          c+=1
        elif comp == 2:
          c-=1
      elif player == 2:
        if comp == 1:
          c+=1
        elif comp == 3:
          c-=1
      elif player == 3:
        if comp == 2:
          c+=1
        elif comp == 1:
          c-=1
      elif player == 0:
        print("Thanks for playing!")
        break
      else:
        print("Invalid choice!")
      if c == 1:
        scoreWOTH += 1
        print(wins[random.randint(0,len(wins)-1)])
      elif c == -1:
        scoreWOTH -= 1
        print(losses[random.randint(0,len(losses)-1)])
      else:
        print("Tie!")

  elif choice == 2:
    print("                    The Number Sieve")
    print('''A correct guess wins you a point, but every wrong guess costs you one.
    After you win, I will choose a new secret number. Good luck!''')
    wins = ["You've cracked the code! A masterful deduction.", "The sieve reveals its secret to you!", "Brilliant! Your mind is as sharp as any blade here.", "The puzzle is solved!"]
    losses = ["Alas, the number remains hidden.", "The sieve holds its secret tight.", "Another guess, another coin to the pot.", "The tavern keeper chuckles at your attempt."]
    print("Guess the number between 1 and n (both inclusive).")
    n=int(input("Choose the last number(n): "))
    comp = random.randint(1,n)
    while True:
      print()
      print()
      print("(enter 0 to quit)")
      print("Score:", scoreTNS)
      print()
      player = int(input("What's your guess? ")) 
      print()
      if player == comp:
        scoreTNS += 1
        print(wins[random.randint(0,len(wins)-1)])
        comp = random.randint(1,n)
      elif player == 0:
        print("Thanks for playing!")
        break
      elif player != comp:
        scoreTNS -= 1
        print(losses[random.randint(0,len(losses)-1)])
      
  elif choice == 3:
    print("                    Trial by Seven")
    print('''
        A game of pure luck! Place a wager on the roll of two dice.
        - Bet on 'Below 7' (1) or 'Above 7' (2) to double your wager.
        - Bet on a 'Lucky 7' (3) for a grand 4-to-1 payout.
        Let's see if fortune favors you today!
    ''')
    wins = ["Fortune smiles upon you!", "The dice have favored you this day!", "Your wager pays off handsomely! Your purse feels heavier.", "Lady Luck is on your side!"]
    losses = ["Alas, fortune is a fickle mistress.", "The dice were not in your favor.", "The house claims your wager.", "Your coin clinks into the keeper's pouch."]
    print("You have ₹100 in starting.")
    while True:
      print()
      print()
      print("(ENTER 1:Below 7, 2:Above 7, 3:Lucky 7, 0:Quit)")
      print("Balance: ₹"+str(scoreTB7))
      print()
      player = int(input("Choose your number: "))
      bet = float(input("What's your bet? "))
      comp1 = random.randint(1,6)
      comp2 = random.randint(1,6)
      comp = comp1+comp2
      print()
      if bet>scoreTB7:
        print("You don't have enough money!")
        break
      else:
        if (player == 1 and comp<7) or (player == 2 and comp>7):
          scoreTB7 += bet
          print(wins[random.randint(0,len(wins)-1)])
        elif player == 3 and comp==7:
          scoreTB7 += bet*4
          print(wins[random.randint(0,len(wins)-1)])
        elif player == 0:
          print("Thanks for playing!")
          break
        else:
          scoreTB7 -= bet
          print(losses[random.randint(0,len(losses)-1)])

  elif choice == 4:
    print("                    Check Scores")
    print("War of the Hand:", scoreWOTH)
    print("The Number Sieve:", scoreTNS)
    print("Trial by Seven: ₹"+str(scoreTB7))
  elif choice == 0:
    print("Thanks for playing!")
    break
