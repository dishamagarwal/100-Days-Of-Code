############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

# TODO: make A equal to 1 or 11 according to the total points
import random

class Game:
    player_points = 0
    dealer_points = 0
    player_hand = []
    dealer_hand = []
    rounds_played = 0
    deck = {
        'A': 11,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'J': 10,
        'Q': 10,
        'K': 10
    }

    def initial_deal(self):
        self.dealer_hand = [random.choice(list(self.deck.keys())), random.choice(list(self.deck.keys()))]
        self.dealer_points += self.deck[self.dealer_hand[0]] + self.deck[self.dealer_hand[1]]
        self.player_hand = [random.choice(list(self.deck.keys())), random.choice(list(self.deck.keys()))]
        self.player_points += self.deck[self.player_hand[0]] + self.deck[self.player_hand[1]]
        self.rounds_played += 2
        self.print_status()

    def print_status(self):
        print("Dealer's first card: " + self.dealer_hand[0])
        print("Your cards: " + str(self.player_hand))
        print("Current score: " + str(self.player_points))

    def deal(self, deal):
        self.rounds_played += 1
        # if self.player_points > 21:
        #     if 'A' in self.player_hand:
        #             self.player_points -= 10
        if deal == 'y' and self.rounds_played <= 4:
            if self.player_points < 21:
                card = random.choice(list(self.deck.keys()))
                self.player_hand.append(card)
                self.player_points += self.deck[card]
            else:
                print("Your total is already at max, cannot deal more cards. You need to go look up the rules")
                return 'n'
            self.print_status()
        return deal
    
    def deal_dealer_cards(self):
        while self.dealer_points < 17:
            card = random.choice(list(self.deck.keys()))
            self.dealer_hand.append(card)
            self.dealer_points += self.deck[card]

    def evaluate_A(self):
        if self.dealer_points > 21:
            if 'A' in self.dealer_hand:
                ...
        if self.player_points > 21:
            if 'A' in self.player_hand:
                ...

    def show(self):
        print("Your hand: " + str(self.player_hand))
        print("Your current score: " + str(self.player_points))
        print("Dealer's hand: " + str(self.dealer_hand))
        print("Dealer's current score: " + str(self.dealer_points))
        if self.player_points > 21 and self.dealer_points > 21:
            print("Everyone's a bust losers")
        elif self.player_points > 21:
            print("You're bust loser, dealer wins")
        elif self.dealer_points > 21:
            print("Kkk you win!")
        elif self.player_points == self.dealer_points:
            print("Whatever, it's a draw")
        elif self.player_points > self.dealer_points:
            print("Aright, you win!")
        else:
            print("Dealer wins, you lose loser!")