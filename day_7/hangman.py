import random
from day_7.hang_word import *
life = 6
word = random.choice(word_list).lower()
le = len(word)
print(logo)
print('Length of the word', le)
display = ['_'] * le
print(display)
end_of_game = True
guessed_letters=set()
while end_of_game:
    ch = input('\nGuess the letter: ').lower()
    if ch in guessed_letters:
        print('You have already guessed that letter. Try again.')
        continue
    guessed_letters.add(ch)
    letter_guessed = False
    for position in range(le):
        letter = word[position]
        if letter == ch:
            display[position] = ch
            letter_guessed = True

    if not letter_guessed:
        life -= 1
        print(f"you guess the letter: {ch} ,that's not in the word.\n !!!you loose a life!!!")
        print(f"remaining life is:{life}")
        print(stages[life])
        if life == 0:
            print("GAME OVER YOU WILL USE ALL OF YOUR LIFE")
            end_of_game = False
            print(f"THE WORD IS :{word} ")

    print(' '.join(display))
    
    if '_' not in display:
        end_of_game = False
        print('Congratulations, you won!')
