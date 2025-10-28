# 6. Word Guessing Game
# Let the user guess letters of a secret word with limited attempts.
secret_word = "python"
guessed_letters = set()
attempts = 6
while attempts > 0:
    display_word = ''.join([letter if letter in guessed_letters else '_' for letter in secret_word])
    print("Word to guess:", display_word)
    guess = input("Guess a letter: ").lower()
    
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    
    guessed_letters.add(guess)
    
    if guess in secret_word:
        print("Good guess!")
    else:
        attempts -= 1
        print(f"Wrong guess! You have {attempts} attempts left.")
    
    if all(letter in guessed_letters for letter in secret_word):
        print(f"Congratulations! You've guessed the word: {secret_word}")
        break