import random
def get_guess():
    while True:
        guess = input('Make a guess: ')
        if not guess.isdigit():
            print('please enter valid number between 1 and 100: ')
            continue
        guess = int(guess)
        if 1 <= guess <= 100:
            return guess
        else:
            print('please enter valid number between 1 and 100: ')

    #  This way is non pythonic:
    # guess = int(input('Make a guess: '))
    # while guess <1 or guess > 100:
    #     guess = int(input('please enter valid number between 1 and 100: '))
    # return guess

def game():
    print('Welcome to guessing game\nI\'m thinking of a number between 1 and 100 inclusive')
    x = random.randint(1, 100)
    print(x)
    dif = input('Choose a difficulty: easy/hard: ')
    dif = dif.lower().strip()
    while dif not in ('easy', 'hard'):
        dif = input('Invalid input, please enter again: ')
    chances = 10 if dif == 'easy' else 5
    won = False
    for i in range(chances,0,-1):
        print('You have ' + str(i) + ' chances to guess the number.')
        guess = get_guess()
        if guess == x:
            print('You guessed it right. You win!')
            won = True
            break
        elif guess < x:
            print('Too low\nGuess again.')
        else:
            print('Too high\nGuess again.')
    if won == False:
        print("you've run out of guess")

def main():
    while True:
        game()
        ch = input("Enter 'y' to play again else enter 'n' :")
        if ch.lower().strip() == 'y':
            continue
        else:
            break
main()
