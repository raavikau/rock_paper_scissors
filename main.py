from random import randint

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [paper, rock, scissors]

while True:
    player_choice = int(input("Choose 0 for Paper, 1 for Rock, or 2 for Scissors:"))
    if player_choice > 2 or player_choice < 0:
        print("Invalid Option")
    else:
        print("You chose:", game_images[player_choice])
        computer_choose = randint(0, 2)
        print("Computer choose:", game_images[computer_choose])
        if player_choice == computer_choose:
            print("It's a Tie!")
        elif player_choice == 0 and computer_choose == 1:
            print("You won!")
        elif player_choice == 1 and computer_choose == 2:
            print("You won")
        elif player_choice == 2 and computer_choose == 0:
            print("You won")
        else:
            print("Computer win")
    if input("Do you want to play again? (Y/N)").upper() != 'Y':
        break
