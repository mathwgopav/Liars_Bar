from game import Char, Deck

def main():
    deck = Deck()
    char1 = Char(deck)
    char1.play_cards()


if __name__ == "__main__":
    main()
