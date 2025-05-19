# Higher or lower game
import random

celeb_followers = [
    {"name": "Cristiano Ronaldo", "followers": 622},
    {"name": "Lionel Messi", "followers": 503},
    {"name": "Selena Gomez", "followers": 429},
    {"name": "Kylie Jenner", "followers": 4},
    {"name": "Dwayne Johnson (The Rock)", "followers": 397},
    {"name": "Ariana Grande", "followers": 380},
    {"name": "Kim Kardashian", "followers": 364},
    {"name": "Beyoncé", "followers": 319},
    {"name": "Justin Bieber", "followers": 293},
    {"name": "Kendall Jenner", "followers": 294},
    {"name": "Taylor Swift", "followers": 283},
    {"name": "Neymar Jr", "followers": 218},
    {"name": "Nicki Minaj", "followers": 228},
    {"name": "Khloé Kardashian", "followers": 311},
    {"name": "Miley Cyrus", "followers": 216},
    {"name": "Zendaya", "followers": 184},
    {"name": "Kevin Hart", "followers": 179},
    {"name": "Cardi B", "followers": 169},
    {"name": "LeBron James", "followers": 159},
    {"name": "Virat Kohli", "followers": 266}
]


def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

score = 0
should_continue = True
account_b = random.choice(celeb_followers)

while should_continue:
    account_a = account_b
    account_b = random.choice(celeb_followers)
    if account_a == account_b:
        account_b = random.choice(celeb_followers)

    print(f"Compare A: {account_a["name"]}.")
    print("Versus:")
    print(f"B: {account_b["name"]}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = account_a["followers"]
    b_follower_count = account_b["followers"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        should_continue = False