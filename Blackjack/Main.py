import Game

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
def main():
    print(logo)
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    while play.lower() == 'y':
        game = Game.Game()
        game.initial_deal()
        game.deal_dealer_cards()
        deal = 'y'
        while deal == 'y':
            deal = input("Type 'y' to get another card, type 'n' to pass: ")
            deal = game.deal(deal)
        game.show()
        play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    print("Thank you for playing! Bye.")

if __name__ == '__main__':
    main()