import random

word_list = ['onigiri', 'kimbap', 'eggroll', 'gyoza', 'baozi', 'burrito', 'burger', 'tiramisu']
word = random.choice(word_list)

guessedWords = ['_'] * len(word)
attempts = 10

while attempts > 0:
    print('\nCurrent Word: ' + ' '.join(guessedWords))
    
    guess = input('Guess a letter: ').lower()
    
    if guess in word: 
        for i in range(len(word)):
            if word[i] == guess:
                guessedWords[i] = guess
        print('Great Guess!')
    else:
        attempts -= 1
        print('Wrong Guess! Attempts left: ' + str(attempts))
    if '_' not in guessedWords:
        print('\nCongratulations! You guessed the word: ' + word)
        break

if attempts == 0 and '_' in guessedWords:
    print('\nYou\'ve run out of attempts! The word was: ' + word)
