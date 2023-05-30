import random
dict = { 1: "Rock", 2: "Paper", 3: "Scissor"}
while True:
    try:
        round = int(input("How many rounds do you wanna play?: ")) 
        break  
    except ValueError:
        print("Please Enter a Number")
        continue
player_score = 0
computer_score = 0
count = 0
equality = 0
while count < round:
    try:
        player_selection = int(input("1- Rock\n2- Paper\n3- Scissor\nYour Selection: "))
    except ValueError:
        print("Please Enter a Number")
        continue
    print(9*"*")
    print (f"{count+1}. Round")
    print(9*"*")
    try:
        print(f"Player Selection = {dict[player_selection]}")
    except KeyError as e:
        print("Please Enter a Valable Number")
        continue   
    computer_selection = random.randint(1,3)
    print(f"Computer Selection = {dict[computer_selection]}")
    print(30*"#")
    if player_selection == 1 and computer_selection == 2:
        computer_score += 1
        print(f"Player Score = {player_score}\nComputer Score = {computer_score}\nDraw = {equality}\n" + 30*"#"+ "\n")
    elif player_selection == 1 and computer_selection == 3:
        player_score += 1
        print(f"Player Score = {player_score}\nComputer Score = {computer_score}\nDraw = {equality}\n" + 30*"#"+ "\n")
    elif player_selection == 2 and computer_selection == 1:
        player_score += 1
        print(f"Player Score = {player_score}\nComputer Score = {computer_score}\nDraw = {equality}\n" + 30*"#"+ "\n")
    elif player_selection == 2 and computer_selection == 3:
        computer_score += 1
        print(f"Player Score = {player_score}\nComputer Score = {computer_score}\nDraw = {equality}\n" + 30*"#"+ "\n")
    elif player_selection == 3 and computer_selection == 1:
        computer_score += 1
        print(f"Player Score = {player_score}\nComputer Score = {computer_score}\nDraw = {equality}\n" + 30*"#"+ "\n")
    elif player_selection == 3 and computer_selection == 2:
        player_score += 1
        print(f"Player Score = {player_score}\nComputer Score = {computer_score}\nDraw = {equality}\n" + 30*"#"+ "\n")
    else:
        equality += 1
        print(f"Player Score = {player_score}\nComputer Score = {computer_score}\nDraw = {equality}\n" + 30*"#"+ "\n")
    count += 1

if computer_score > player_score:
    print("The Computer Wins...\n")
elif computer_score == player_score:
    print("Tie, there is no winner...\n")
else:
    print("The Player Wins...\n")