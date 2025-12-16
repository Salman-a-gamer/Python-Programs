import random
import hangman_words
import hangman_art
w = random.choice(hangman_words.word_list)
display_word = ''
l = len(w)
for i in range(l):
    display_word += '_'
#print(w)

chances = 6
display_word_lst = list(display_word)
w_lst = list(w)
win = False
print(hangman_art.logo)

while chances > 0:
    print(hangman_art.stages[chances])
    print('Word to guess: ', display_word)
    guessed_letter = input('Guess a letter: ')
    if guessed_letter in w:
        for i, ch in enumerate(w_lst):
            if guessed_letter == ch:
                display_word_lst[i] = ch
        display_word = ''.join(display_word_lst)
        print(display_word)

        if display_word == w:
            print('you win. this time'.center(60, '_'))
            win = True
            break
        else:
            print('{}/6 lives left'.format(chances).center(60, '-'))
    else:
        chances -= 1
        print('You chose', guessed_letter, 'which is not the word. You lose a life.')
        print('{}/6 lives left'.format(chances).center(60,'-'))
if win == False:
    print("you lose . HAHAHAHA".center(60,'-'))




