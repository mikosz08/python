import random as r


def human_guess(num):
    rand_num = r.randint(1, num)
    guess = 0
    while(rand_num != guess):
        guess = int(input(f'Guess a number [1 - {num}]'))
        if guess < rand_num:
            print('Too low.')
        elif guess > rand_num:
            print('Too high.')
        else:
            print('Number guessed!')


def computer_guess(num):
    print('Think about the number the computer will try to guess.')
    low = 1
    high = num
    feedback = ''
    while feedback != 'C':
        if low != high:
            comp_guess = r.randint(low, high)
        else:
            print('ha ha!')
            comp_guess = low
        feedback = input(
            f'Is {comp_guess} too high (H), too low (L), or correct (C)??').upper()
        if feedback == 'H':
            high = comp_guess - 1
        elif feedback == 'L':
            low = comp_guess + 1
        elif feedback == 'C':
            print('ayy lmao')


(computer_guess(58675), human_guess(65748))[r.randint(0, 1) == 1]
