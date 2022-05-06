from datagame import data
import random

score = 0

while True:
    choice_a = random.choice(data)
    choice_b = random.choice(data)
    if choice_a == choice_b:
        choice_b = random.choice(data)
    
    print(f"Compare A: {choice_a['name']}, {choice_a['description']}, from {choice_a['country']}")
    print(f"Against B: {choice_b['name']}, {choice_b['description']}, from {choice_b['country']}")


    def pick(followers):
        return followers['follower_count']

    
    guess = input("Who has more followers? Type 'A' or 'B': ")
    if guess in 'Aa':
        if pick(choice_a) > pick(choice_b):
            score += 1
            print(f"You're right! Your score is {score}")
            choice_a == choice_b
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break
    elif guess in 'Bb':
        if pick(choice_b) > pick(choice_a):
            score += 1
            print(f"You're right! Your score is {score}")
            choice_a == choice_b
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break
    else:
        print('Sorry, thats an invalid option. Try again. ')
        break
