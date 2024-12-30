import random
words = ["India","srilanka","Pakistan","canada","America","japan","germany","denmark","china","brazil","chile","australia","norway","iran","palastine", "korea","finland","africa","bhutan","nepal","england"]
chosen_word = random.choice(words)
lives = 6

display = []
for i in chosen_word:
    display += '_'
print(display)

game_over = False
while not game_over:
    guess = input("Enter a letter:").lower()
    for position in range(len(chosen_word)): #0 1 2 3 4...
        letter = chosen_word[position]
        if letter == guess:
           display[position] = guess
    print(display)

    if guess not in chosen_word:
        lives-=1
        if lives == 0:
            game_over == True
            print("oops, you lose!")
    if '_' not in display:
        game_over == True
        print("wow, you win!")  
        break 