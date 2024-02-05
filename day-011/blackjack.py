from blackjack_art import logo
import random


def ask_continue_playing():
    should_play = input("Do you want do play a game of Blackjack ? Type 'y' or 'n': ")
    if should_play == 'y':
        return True
    return False

def draw_cards(number_of_cards=1):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    new_cards = []
    
    for _ in range(number_of_cards):
        new_cards.append(random.choice(cards))
    
    return new_cards

def sum_scores(cards: list):
    if sum(cards) == 21 and len(cards) == 2: # blackjack
        return 0

    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare_scores(user_score, computer_score):
    
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def print_game_to_user(game):
    print(f"Your cards: {game['player']['cards']}, current score: {game['player']['score']}")
    print(f"Computer's first card: [{game['computer']['cards'][0]}]")

def initial_game():
    game = {
        "player": {
            "cards": [],
            "score": 0
        },
        "computer": {
            "cards": [],
            "score": 0
        }
    }
    
    game['player']['cards'] = draw_cards(2)
    game['player']['score'] = sum_scores(game['player']['cards'])

    game["computer"]['cards'] = draw_cards(2)
    game["computer"]['score'] = sum_scores(game["computer"]['cards'])

    print_game_to_user(game)

    return game

def blackjack():
    is_playing = True

    game = initial_game()

    while is_playing:

        if game['player']['score'] == 0 or game['computer']['score'] == 0 or game['player']['score'] > 21:
            is_playing = False
        else:
            draw_new_card = input("Type 'y' to get another card, type 'n' to pass: ")

            if draw_new_card == 'y':
                game['player']['cards'].append(draw_cards()[0])
                game['player']['score'] = sum_scores(game['player']['cards'])

                print_game_to_user(game)
            else:
                is_playing = False

    while game['computer']['score'] != 0 and game['computer']['score'] < 17:
        game['computer']['cards'].append(draw_cards()[0])
        game['computer']['score'] = sum_scores(game['computer']['cards'])
    
    print('---------------------------------------------------------------')
    print(f"Your final hand: {game['player']['cards']}, final score: {game['player']['score']}")
    print(f"Computer's final hand: {game['computer']['cards']}, final score: {game['computer']['score']}")

    print(compare_scores(game['player']['score'],game['computer']['score']))


blackjack()




