import random

# scores = [1,2,3,4,5,6,7,8,9,10]

#
# final_score = 0
#
# final_computer_score = 0
#
# user_numbers = []
#
# random_scores = random.choices(scores,k=2)
#
# user_numbers += random_scores
#
# for number in user_numbers:
#     final_score += number
# print(f"Your cards: {user_numbers}, current score: {final_score}")
#
# computer_score = []
#
# computer_random_score = random.choice(scores)
# computer_score += [computer_random_score]
# print(f"Computer's first card: {computer_score[0]}")
# final_computer_score = computer_score[0]
# play = True
#
# while play:
#     user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
#
#     if user_choice == 'y':
#         another_one_card = random.choice(scores)
#         user_numbers.append(another_one_card)
#         final_score = 0
#         final_computer_score = 0
#         for number in user_numbers:
#             final_score += number
#         if final_score > 21:
#             print(f"Your final hand: {user_numbers}, final score: {final_score}")
#             print(f"Computer's final hand: {computer_score}, final score: {final_computer_score}")
#             print("You went over. You lose 😭")
#             play = False
#         else:
#             print(f"Your cards: {user_numbers}, current score: {final_score}")
#             print(f"Computer's first card: {computer_score[0]}")
#             computer_score.append(random.choice(scores))
#             for number in computer_score:
#                 final_computer_score += number
#     else:
#         final_computer_score = 0
#         computer_score.append(random.choice(scores))
#         for number in computer_score:
#             final_computer_score += number
#
#         if final_computer_score > 21:
#             print(f"Your final hand: {user_numbers}, final score: {final_score}")
#             print(f"Computer's final hand: {computer_score}, final score: {final_computer_score}")
#             print("Opponent went over.You win 😁")
#         elif final_computer_score < final_score:
#             print(f"Your final hand: {user_numbers}, final score: {final_score}")
#             print(f"Computer's final hand: {computer_score}, final score: {final_computer_score}")
#             print("Opponent went over.You win 😁")
#         else:
#             print("You went over. You lose 😭")
#         play = False

#

import random


CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():

    return random.choice(CARDS)


def calculate_score(hand):

    score = sum(hand)


    if score > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        score = sum(hand)

    return score


def print_current_state(user_hand, comp_hand, final=False):
    if final:
        print(f"Your final hand: {user_hand}, score: {calculate_score(user_hand)}")
        print(f"Computer final hand: {comp_hand}, score: {calculate_score(comp_hand)}")
    else:
        print(f"Your cards: {user_hand}, current score: {calculate_score(user_hand)}")
        print(f"Computer’s first card: {comp_hand[0]}")



user_hand = [deal_card(), deal_card()]
computer_hand = [deal_card()]

game_over = False

print_current_state(user_hand, computer_hand)


while not game_over:
    if calculate_score(user_hand) > 21:
        game_over = True
        break

    action = input("Type 'y' to get another card, 'n' to pass: ").lower()

    if action == "y":
        user_hand.append(deal_card())
        print_current_state(user_hand, computer_hand)
    else:
        game_over = True


while calculate_score(computer_hand) < 17:
    computer_hand.append(deal_card())


print_current_state(user_hand, computer_hand, final=True)

user_score = calculate_score(user_hand)
comp_score = calculate_score(computer_hand)


if user_score > 21:
    print("You went over. You lose 😭")
elif comp_score > 21:
    print("Computer went over. You win 😁")
elif user_score > comp_score:
    print("You win 😎")
elif user_score < comp_score:
    print("You lose 😭")
else:
    print("Draw 🙃")
