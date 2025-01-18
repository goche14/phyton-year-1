print("====================Welcome! To Guess Who!====================")
print("Each player chooses a mystery character and then using yes or no questions,\n they try to figure out the other player's mystery character.\n When they think they know who their opponent's mystery character is,\n players make a guess. If the guess is wrong, that player loses the game!")
print("==========Good luck!==========")


characters = ("messi","maradona","pele","cristiano ronaldo","ronaldo nazario","neymar","suarez","benzema","kaka","ronaldinho")
print(characters)

player_1 = input("Player_1 enter your name: ")
player_2 = input("Player_2 Enter your name: ")

player_1_choice = input(f"{player_1},enter your choice from characters: ")
player_2_choice = input(f"{player_2},enter your choice from characters: ")


print("Now randomizer decides who will start playing the game ")

random_1 = (player_1,player_2)

import random

choice_1 = random.choice(random_1)

if choice_1 == player_1:
    print(f"{player_1} starts the game ")
elif choice_1 == player_2:
    print(f"{player_2} starts the game")


def player_1_questions():
    print("You have to ask 5 questions")
    
    input(f"{player_1},enter your first question: ")
    
    input(f"{player_2},yes/no: ")
    
    input(f"{player_1},enter your second question: ")
    
    input(f"{player_2},yes/no: ")
    
    input(f"{player_1},enter your third question: ")
    
    input(f"{player_2},yes/no: ")

    input(f"{player_1},enter your fourth question: ")

    input(f"{player_2},yes/no: ")

    input(f"{player_1},enter your last question question: ")

    input(f"{player_2},yes/no: ")

    decision_1 = input(f"{player_1},enter your decision: ")

    if decision_1 == player_2_choice:
        print("you won!")
    elif decision_1 != player_2_choice:
        print(f"anwser was {player_2_choice}")

def player_2_questions():
    
    print(f"{player_1}, Its your time to answer")

    input(f"{player_2},enter your first question: ")
    
    input(f"{player_1},yes/no: ")
    
    input(f"{player_2},enter your second question: ")
    
    input(f"{player_1},yes/no: ")
    
    input(f"{player_2},enter your third question: ")
    
    input(f"{player_1},yes/no: ")

    input(f"{player_2},enter your fourth question: ")

    input(f"{player_1},yes/no: ")

    input(f"{player_2},enter your last question question: ")

    input(f"{player_1},yes/no")

    decision_2 = input(f"{player_2},enter your decision: ")

    if decision_2 == player_1_choice:
        print("you won!")
    elif decision_2 != player_1_choice:
        print(f"anwser was {player_1_choice}")



def main():
        if choice_1 == player_1:
            player_1_questions()
            player_2_questions()
        elif choice_1 == player_2:
            player_2_questions()
            player_1_questions()
        
main()
    
    
    




    

