import random

def guessing_game():
    # List of popular sports
    sports = ["Football", "Basketball", "Tennis", "Cricket", "Golf", "Baseball", "Rugby", "Boxing", "Swimming", "Athletics"]
    
    # Randomly select a sport from the list
    sport_to_guess = random.choice(sports).lower()
    
    # Initialize variables
    guessed = False
    attempts = 0
    
    print("Welcome to the Guessing Game - Popular Sports Edition!")
    print("I'm thinking of a popular sport. Can you guess what it is?")
    
    while not guessed:
        guess = input("Enter your guess: ").strip().lower()
        attempts += 1
        
        if guess == sport_to_guess:
            print(f"Congratulations! You guessed it right! The sport was {sport_to_guess.capitalize()}.")
            print(f"It took you {attempts} attempts.")
            guessed = True
        else:
            print("Oops! That's not the sport I'm thinking of. Try again!")

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        guessing_game()
    else:
        print("Thanks for playing!")

# Start the game
guessing_game()
