import random  # Import the random module to allow random choice for the computer

# Initialize counters for user and computer wins
userWins = 0
comWins = 0

# Valid choices: 1 = Rock, 2 = Paper, 3 = Scissors
choices = ["1", "2", "3"]

# Start the game loop
while True:
    # Ask the user for input
    userInput = input("Select an option: \n1. Rock \n2. Paper \n3. Scissors \n0. Quit\n: ")

    # If user chooses to quit
    if userInput == "0":
        print("Quitting game...")
        break  # Exit the loop and end the game

    # Check for invalid input
    if userInput not in choices:
        print("Invalid choice, try again.")
        continue  # Go back to the beginning of the loop

    # Generate a random choice for the computer
    ranNumber = random.randint(0, 2)
    comPick = choices[ranNumber]  # Randomly choose between "1", "2", or "3"

    # Print what the computer picked in words
    print("Computer picked", 
          "Rock." if comPick == "1" else 
          "Paper." if comPick == "2" else 
          "Scissors.")

    # Determine the winner based on classic game rules
    if (userInput == "1" and comPick == "3") or \
       (userInput == "2" and comPick == "1") or \
       (userInput == "3" and comPick == "2"):
        print("You have won!")  # User wins
        userWins += 1  # Increase user score

    elif userInput == comPick:
        print("It's a tie!")  # Same choice means tie

    else:
        print("You lost :(")  # Computer wins
        comWins += 1  # Increase computer score

# After exiting the loop, show the final scores
print("You have won", userWins, "times.")
print("Computer has won", comWins, "times.")
print("Goodbye....")
