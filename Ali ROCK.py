import random

def get_user_choice():
    while True:
        user_choice=input("Choose Rock,Paper or Scissors :").strip().lower()
        if user_choice in("rock","paper","scissors"):
            return user_choice
        print("Invalid Choice.Please choose Rock,Paper or Scissors.")

def get_computer_choice():
    return random.choice(["rock","paper","scissors"])

def determine_winner(user_choice,computer_choice):
    if user_choice==computer_choice:
        return "DRAW"
    if(user_choice=="rock" and computer_choice=="scissors") or \
      (user_choice=="scissors" and computer_choice=="paper") or \
      (user_choice=="paper" and computer_choice=="rock"):
        return "You Win"
    return "Computer Wins"

def main():
    user_score=0
    computer_score=0
    print("WELCOME TO ROCK,PAPER SCISSORS GAME.The COMPUTER will be your opponent.")
    user_name=input("Enter your name : ")
    print(f'Welcome,{user_name}')
    while True:
        user_choice = get_user_choice()
        computer_choice=get_computer_choice()
        print(f'{user_name}, you chose {user_choice}. Computer chose {computer_choice}')
        result= determine_winner(user_choice,computer_choice)
        print(result)
        if "You Win" in result:
            user_score+=1
        elif"Computer Wins" in result:
            computer_score+=1
        print(f' Your score : {user_score},Computer score : {computer_score}')
        play_again = input("Do you want to play another round??? (yes/no) : ").strip().lower()
        if play_again!="yes":
            break
    print("Thank You for playing!")
        

if __name__=="__main__":
    main()
        
