name = input("Welcome to GC mini golf! What is your name? ")
number_of_holes = 0

# Function used when 3 holes is selected
def three_holes():
    score = 0
    par = 0
    score += int(input("How many putts for hole 1? (par is 3) "))
    score += int(input("How many putts for hole 2? (par is 3) "))
    score += int(input("How many putts for hole 3? (par is 3) "))
    total_score = score - 9
    if total_score == par:
        print(f"Good game, {name}. Your total par was: {total_score}")
    elif total_score < par:
        print(f"Great job, {name}! Your total par was: {total_score}")
    elif total_score > par:
        print(f"Nice try, {name}... Your total par was: +{total_score}")


# Function used when 6 holes is selected
def six_holes():
    score = 0
    par = 0
    score += int(input("How many putts for hole 1? (par is 3) "))
    score += int(input("How many putts for hole 2? (par is 3) "))
    score += int(input("How many putts for hole 3? (par is 3) "))
    score += int(input("How many putts for hole 4? (par is 3) "))
    score += int(input("How many putts for hole 5? (par is 3) "))
    score += int(input("How many putts for hole 6? (par is 3) "))
    total_score = score - 18
    if total_score == par:
        print(f"Good game, {name}. Your total par was: {total_score}")
    elif total_score < par:
        print(f"Great job, {name}! Your total par was: {total_score}")
    elif total_score > par:
        print(f"Nice try, {name}... Your total par was: +{total_score}")

# Line Break

while name == "":
        print("You must enter a name to begin")
        name = input("Welcome to GC mini golf! What is your name? ")

while number_of_holes != 3 or number_of_holes != 6:
    number_of_holes = int(input(f"Hi, {name} Would you like to play 3 or 6 holes today? "))
    if number_of_holes == 3:
        three_holes()
    elif number_of_holes == 6:
        six_holes()


