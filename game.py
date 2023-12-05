import random

word_file = open('words.txt', 'r')
word_list = []
for line in word_file:
    word_list.append(line.rstrip().upper())
word_to_guess = random.choice(word_list)
print(word_to_guess)
print('Welcome to "Definitely Not Just a Rip-Off of Wordle"!\nYou have 5 guesses to guess a 5 letter word.\nGood Luck!')

correct_letters_guessed = ['-','-','-','-','-']
out_of_place_letters_guessed = set()

for turn in range(5):
    word_guessed = input('Please guess a word: ').upper()
    print('Your guess: {}'.format(word_guessed))
    letters_to_guess = list(word_to_guess)
    letters_guessed = list(word_guessed)
    if word_guessed == word_to_guess:
        winner_message = "Congratulations, you guessed the right word: {}".format(word_to_guess.upper())
        print(winner_message)
        break
    elif len(word_guessed) != 5:
        print('Oops! Try again with a 5 letter word. You have {} turns left.'.format(4-turn))
        continue
    else:
        print(letters_guessed)
        for letter in letters_guessed:
            try:
                index_on_word_to_guess = letters_to_guess.index(letter)
                index_on_word_guessed = letters_guessed.index(letter)
                if index_on_word_guessed == index_on_word_to_guess:
                    correct_letters_guessed[index_on_word_to_guess] = letter
                    if letter in out_of_place_letters_guessed:
                        out_of_place_letters_guessed.remove(letter)
                else:
                    if letter not in correct_letters_guessed:
                        out_of_place_letters_guessed.add(letter)
                    else:
                        continue
            except:
                continue
        print(correct_letters_guessed)
        if len(out_of_place_letters_guessed) > 0:
            print(out_of_place_letters_guessed)