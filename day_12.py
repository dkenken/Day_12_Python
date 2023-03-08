# Exercises #Day #15

# AGENDA: SCOPE

enemies = 1

def increase_enemies():
    enemies = 2
    print(f'enemies inside fuction: {enemies}')


increase_enemies()
print(f'enemies outside function: {enemies}')

# Local Scope:
def drink_position():
    position_strength = 2
    print(position_strength)

drink_position()
print(position_strength)  #Won't be able to call the print function on position_strength since it is insde the function


# Global Scope
player_health = 10


def game():
    def drink_position():
        position_strength = 2
        print(player_health)

    drink_position()
print(player_health)

# There is no Block scope 

game_level = 3
def create_enemy():
    enemies = ['Skeletons', 'Zombies', 'Alien']
    if game_level < 5:
       new_enemy = enemies[0]
    print(new_enemy)  

# Modifying Global Scope

enemies = 1

def increase_enemies():
    enemies = 2
    print(f'enemies inside fuction: {enemies}')
    return enemies + 1

enemies = increase_enemies()
print(f'enemies outside function: {enemies}')

# Global constants

PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@ken_deli"

# Number_Guessing_Game

from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}") 

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()
