# deck.py

import random
from card import Card

class Deck(list):

    """ class for a deck of cards """
    
    # pseudo-constants
    START_SIZE = 52
    
    # list to hold rank values
    ranks = [
        Card.ACE, Card.KING, Card.QUEEN,
        Card.JACK, Card.TEN, Card.NINE,
        Card.EIGHT, Card.SEVEN, Card.SIX,
        Card.FIVE, Card.FOUR, Card.THREE,
        Card.TWO
    ]
    
    # list to hold suit values
    suits = [ Card.SPADE, Card.HEART, Card.CLUB, Card.DIAMOND ]
    
    # list to hold numeric card values
    values = [
        Card.ELEVEN_VAL, Card.TEN_VAL, Card.TEN_VAL,
        Card.TEN_VAL, Card.TEN_VAL, Card.NINE_VAL,
        Card.EIGHT_VAL, Card.SEVEN_VAL, Card.SIX_VAL,
        Card.FIVE_VAL, Card.FOUR_VAL, Card.THREE_VAL,
        Card.TWO_VAL
    ]
    
    # constructor
    def __init__(self):
        super()
        c = None
        for i in range(self.START_SIZE):
            if (i < (self.START_SIZE / 4)):
                c = Card(self.ranks[i%13], self.suits[0], self.values[i%13])
            elif (i < (self.START_SIZE / 4 * 2)):
                c = Card(self.ranks[i%13], self.suits[1], self.values[i%13])
            elif (i < (self.START_SIZE / 4 * 3)):
                c = Card(self.ranks[i%13], self.suits[2], self.values[i%13])
            else:
                c = Card(self.ranks[i%13], self.suits[3], self.values[i%13])
            self.append(c)
                
    # get the top card
    def get_top_card(self):
        return self.pop(0)
    
    # shuffle the deck
    def shuffle(self):
        random.shuffle(self)
    
    # to string method
    def __str__(self):
        to_string = ""
        for card in self:
            to_string += str(card) + "\n"
        return to_string
    
# main function
def main():
    shuffle = input("Shuffle first? (y/n) ")
    
    my_deck = Deck()
    if shuffle == "y" or shuffle =="yes":
        my_deck.shuffle()
        
    print("\nDeck:\n" + str(my_deck))
    print("Top card:\n" + str(my_deck.get_top_card()))
    
# if run directly
if __name__ == "__main__":
    main()