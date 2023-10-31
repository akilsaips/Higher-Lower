import random
from art import logo,vs
from dataz import data
from replit import clear

def randaccount():
  return random.choice(data)

def format(account):
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}."

def check(guess, a, b):
  if a>b:
    return guess == "a"
  else:
    return guess == "b"

def game():
  score = 0
  print(logo)
  should_continue = True
  user_a = randaccount()
  user_b = randaccount()
  
  while should_continue:
    user_a = user_b
    user_b = randaccount()
    
    while user_a == user_b:
      user_b = randaccount()
    
    print(f"Compare A: {format(user_a)}")
    print(vs)
    print(f"Against B: {format(user_b)}")
    
    guess = input("Who has more instagram followers? A/B : ").lower()
    
    follower_a = user_a["follower_count"]
    follower_b = user_b["follower_count"]
    
    is_correct = check(guess, follower_a, follower_b)
  
    clear()
    print(logo)
    
    if is_correct:
      score += 1
      print(f"That is right!, your current score is {score}")
      user_a = user_b
  
    else:
      should_continue = False
      print(f"That is wrong, your final score is {score}")

game()
