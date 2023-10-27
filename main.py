from data import  data
import random

def get_random_data():
    return random.choice(data)

def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]

    return f"{name}, a {description}, from {country}"

def check_answer(guess, account_a, account_b):
    if account_a > account_b:
        return guess == "a"
    else:
        return guess == "b"


def game():
    score = 0
    game_should_continue = True
    account_a = get_random_data()
    account_b = get_random_data()
    while game_should_continue:
        account_a = account_b
        account_b = get_random_data()

        while account_a == account_b:
            account_b = get_random_data()
        print(f"Compare A: {format_data(account_a)}")
        print(f"Against B: {format_data(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        follower_count_a = account_a['follower_count']
        follower_count_b = account_b['follower_count']
        is_correct = check_answer(guess, follower_count_a, follower_count_b)
        if is_correct:
            score += 1
            print("You are right")
        else:
            game_should_continue = False
            print(f"You are wrong. Your score is {score}")



game()