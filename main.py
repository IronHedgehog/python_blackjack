import random

scores = [1,2,3,4,5,6,7,8,9,10]

final_score = 0

user_numbers = []

random_scores = random.choices(scores,k=2)

user_numbers += random_scores

for number in user_numbers:
    final_score += number
print(f"Your cards: {user_numbers}, current score: {final_score}")

computer_score = []

computer_random_score = random.choice(scores)
computer_score += [computer_random_score]
print(f"Computer's first card: {computer_score[0]}")

play = True

while play:
    user_choice = input("Type 'y' to get another card, type 'n' to pass: ")

    if user_choice == 'y':
        another_one_card = random.choice(scores)
        user_numbers.append(another_one_card)
        final_score = 0
        for number in user_numbers:
            final_score += number
        if final_score > 21:
            print(f"Your final hand: {user_numbers}, final score: {final_score}")
            print(f"Computer's final hand: {computer_score}")
            print("You went over. You lose 😭")
            play = False
        else:
            print(f"Your cards: {user_numbers}, current score: {final_score}")
            print(f"Computer's first card: {computer_score[0]}")
            computer_score.append(random.choice(scores))
    else:
        print(f"Your final hand: {user_numbers}, final score: {final_score}")
        print(f"Computer's final hand: {computer_score}")
        print("Opponent went over.You win 😁")
        play = False


