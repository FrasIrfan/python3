import random
def check(AI, User):
    if AI == User:
        return 0 # indicates a tie
    
    # all the conditions in which AI wins 
    if (AI == 0 and User == 2) or (AI == 1 and User == 0) or (AI == 2 and User == 1):
        return -1 # indicates AI has won
    return 1 # indicates user has won

print("0 for Rock, 1 for Paper, 2 for Scissor, or any other number to quit")

# Input
user_choice = int(input("Enter your choice: "))

# Generates random number using the randint method
AI_choice = random.randint(0, 2)

print(f"\nYou chose: {user_choice}")
print(f"AI chose: {AI_choice}")

result = check(AI_choice, user_choice)

#conditions to check the Result
if result == 0:
    print("It's a tie!")
elif result == 1:
    print("You win!")
else:
    print("AI wins!")
