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
player_choice = int(input("Choose 0 for Paper, 1 for Rock, or 2 for Scissors:"))
print("You chose:", game_images[player_choice])
