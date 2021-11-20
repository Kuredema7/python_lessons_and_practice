import random as r

rock = '''
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print('What is your choice?\n')
user_choice = int(input('''
CHoose the number:-
0: Rock
1: Paper
2: Scissors
'''))

rps_list = [rock, paper, scissors]

computer_choice = r.randint(0, 2)

if (user_choice > 2) or (user_choice < 0):
    print('You chose invalid number, you lose!')
else:
    print(rps_list[user_choice])
    print(f"Computer chose: \n{rps_list[computer_choice]}")

    if (rps_list[user_choice] == rps_list[computer_choice]):
        print("it's a draw")
    elif (rps_list[user_choice] == rps_list[0]) and (rps_list[computer_choice] == rps_list[2]):
        print('You Win')
    elif (rps_list[user_choice] == rps_list[2]) and (rps_list[computer_choice] == rps_list[1]):
        print('You Win')
    elif (rps_list[user_choice] == rps_list[1]) and (rps_list[computer_choice] == rps_list[0]):
        print('You Win')
    else:
        print('You Lose')
