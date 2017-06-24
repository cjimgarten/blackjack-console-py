# card.py

class Card:

    """ class for a playing card """
    
    # rank pseudo-constants
    ACE = "Ace"
    KING = "King"
    QUEEN = "Queen"
    JACK = "Jack"
    TEN = "Ten"
    NINE = "Nine"
    EIGHT = "Eight"
    SEVEN = "Seven"
    SIX = "Six"
    FIVE = "Five"
    FOUR = "Four"
    THREE = "Three"
    TWO = "Two"

    # suit pseudo-constants
    SPADE = "Spade"
    HEART = "Heart"
    CLUB = "Club"
    DIAMOND = "Diamond"

    # value pseudo-constants
    ELEVEN_VAL = 11
    TEN_VAL = 10
    NINE_VAL = 9
    EIGHT_VAL = 8
    SEVEN_VAL = 7
    SIX_VAL = 6
    FIVE_VAL = 5
    FOUR_VAL = 4
    THREE_VAL = 3
    TWO_VAL = 2
    ONE_VAL = 1

    # constructor
    def __init__(self, rank=ACE, suit=SPADE, value=ELEVEN_VAL, face_up=False):
        self.rank = rank
        self.suit = suit
        self.value = value
        self.face_up = face_up
        
    # swap the value of an Ace
    def swap_ace_value():
        
        # ensure the card is an Ace
        if self.rank == self.ACE:
            return
        
        # swap value
        if self.value == self.ONE_VAL:
            self.value = self.ELEVEN_VAL
        else:
            self.value = self.ONE_VAL

    # to string method
    def __str__(self):
        return ("rank: " + self.rank + ", suit: " + self.suit +
               ", value: " + str(self.value) + ", face_up: " + str(self.face_up))

# main function
def main():
    my_card = Card()
    print(my_card)
    print(my_card.rank)
    print(my_card.suit)
    print(my_card.value)
    print(my_card.face_up)
    
# if run directly
if __name__ == "__main__":
    main()