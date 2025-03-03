import random

# List of simple words
words = ["free", "dog", "sun", "pardon", "execution", "freedom", "justice", "destiny", "verdict", "king", "sorry", "help"]

# Choose a random word
word = random.choice(words)

# Set number of allowed guesses
guesses_left = 5


print("Hello, prisoner!")
print("Guess a correct word. If you guess it right, you will be free. Otherwise, you will be executed...")
print("Good luck!")

print(f"Hint: The word has {len(word)} letters.")

# Game loop
while guesses_left > 0:
    # Get player's guess
    guess = input("Guess a letter: ")
 
    if guess in word:
        print("Correct!")
        print("Congratulations! you will be set free 🎉🥳") 
    else:
        guesses_left -= 1
        print(f"Wrong! you have {guesses_left} guesses left ⚠️☠️")
    
# Check if player lost
if guesses_left == 0:
    print(f"Game over! You lost! The word was {word}.")
    print("I'm sad to tell you that you will soon be executed!")
