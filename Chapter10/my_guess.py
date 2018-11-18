#!/usr/bin/env python
# encoding: utf-8

import random,sys
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = raw_input().lower()
dict_toss={0:'heads',1:'tails'}
toss = dict_toss[random.randint(0, 1)] # 0 is tails, 1 is heads
if guess == toss:
    print('You got it!')
    sys.exit(0)
else:
    print('Nope! Guess again!')
    print('Guess the coin toss! Enter heads or tails:')
    guess = raw_input().lower()
    if guess == toss:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
