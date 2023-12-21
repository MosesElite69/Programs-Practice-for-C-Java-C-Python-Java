import random
from collections import Counter

some_words = '''apple banana mango strawberry  
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

some_words = some_words.split(' ')
# randomly choose a secret word from our "someWords" LIST. 
word = random.choice(some_words)

if __name__ == '__main__':
    print("What's the word. HINT!! IT'S A FRUIT")
    
    for i in word:
        # For printing the empty spaces for letters of the word
        print('_', end=' ') 
    print()
    
    playing = True
    # list for storing the letters guessed by the player
    letter_guessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0 

