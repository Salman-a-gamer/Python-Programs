import Questions
import random

def ask_question(name,dif,correct_points, wrong_points, question_list):
    if not question_list:
        print('All questions under ' + dif + ' have been asked!')
        return ask_difficulty(name)
    q = random.choice(question_list)
    question_list.remove(q)
    ans = input(name + ' answer this '+dif+' question: ' + q['question'] + ' ')
    if ans.lower().strip() == q['answer']:
        print('Correct Answer! ✅')
        return correct_points
    else:
        print('Wrong Answer! ❌ \nThe correct answer was ' + q['answer'])
        return wrong_points

def ask_difficulty(name):
    dif = input(name + ' chose the difficulty: easy / medium / hard : ')
    dif = dif.lower().strip()
    while dif != 'easy' and dif != 'medium' and dif != 'hard':
        dif = input('Invalid input, please try again: ')
    if dif == 'easy':
        return ask_question(name, dif, 3,-1, Questions.easy_questions)
    elif dif == 'm':
        return ask_question(name, dif, 5,-2, Questions.medium_questions)
    else :
        return ask_question(name, dif, 8, -4, Questions.hard_questions)


print('Welcome to 🧠 The Trivia Challenge!'.center(80, '_'))
print('Easy Question: Correct = +3, Wrong = -1\nMedium Question: Correct = +5, Wrong = -2\nHard Question: Correct = +8, Wrong = -4')

player1 = input("Player no.1, What's your name? : ")
player1 = player1.title()
player2 = input("Player no.2, What's your name? : ")
player2 = player2.title()
player1_score = 0
player2_score = 0
number_of_questions = int(input("\nHow many rounds do you wanna play? "))
total_questions = len(Questions.easy_questions) + len(Questions.medium_questions)+len(Questions.hard_questions)

while number_of_questions > total_questions//2:
    print(f'Sorry number of question cant be greater than {total_questions //2}')
    number_of_questions = int(input('Please enter again: '))

print('🎮 Game starts!!'.center(80,'_'))

for n in range(number_of_questions):
    # Player 1's turn :
    print(f'Round {n +1} begins'.center(80, '_'))
    player1_score += ask_difficulty(player1)
    # player 2's turn
    player2_score += ask_difficulty(player2)
    print(f'The scores are: Player 1: {player1_score}, Player2: {player2_score}')

if player1_score > player2_score:
    print(f'{player1} wins!'.center(80,'_'))
elif player2_score > player1_score:
    print(f'{player2} wins!'.center(80, '_'))
else:
    print(f"It's a draw".center(80, '_'))

