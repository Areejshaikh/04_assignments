import random

# Secret Word
words = ["developer", "programming", "hangman", "artificial", "beginning"]

# Select a random word
word = random.choice(words).lower()  # Convert word to lowercase for consistency
guessed_word = ["_"] * len(word)
attempt = 6
guessed_letters = []  # Fixed variable name

print("Welcome To Hangman!")

while attempt > 0 and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print(f"Attempts left: {attempt}")

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You have already guessed that letter!")
        continue

    guessed_letters.append(guess)  # Now correctly indented

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        attempt -= 1  # Fixed variable name
        print("Wrong guess!")

if "_" not in guessed_word:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over! The word was:", word)
