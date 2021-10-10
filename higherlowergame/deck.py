import random
from .card import suits, values, Card

class Deck:
    """
    A class to represent a collection of cards in a specific order

    Attributes
    ----------
    deck : list[Card]
        A list of Cards
    current_position : int
        The position in the list of the cards to reperasent the top card in the deck

    Methods
    -------
    shuffle_deck():
        Reorders the list of cards in a random order.
    current_card():
        Returns the Card at the top of the deck.
    previous_card():
        Returns the previous Card that was at the top of the deck.
    move_to_next_card():
        Takes the card from the top of the deck, moving to the next position.
    reset_deck():
        Reorders the deck of cards and sets the position back to the start.
    """
    def __init__(self):
        """
        Constructs all the attributes for a Deck object.

        Sets up a list of Cards for all 52 combinations then shuffles the list and sets the position to the start.
        """
        all_suits = suits.keys()
        all_values = values.keys()

        self.deck = []
        for card_suit in all_suits:
            for card_value in all_values:
                self.deck.append(Card(card_suit, card_value))
        
        self.shuffle_deck()
        self.current_position = 0


    def shuffle_deck(self) -> None:
        """Reorders the list of cards in a random order."""
        random.shuffle(self.deck)

    def current_card(self) -> Card:
        """Returns the Card at the top of the deck."""
        return self.deck[self.current_position]

    def previous_card(self) -> Card:
        """Returns the previous Card that was at the top of the deck."""
        return self.deck[self.current_position - 1]

    def move_to_next_card(self) -> None:
        """
        Takes the card from the top of the deck, moving to the next position.

        Raises
        ------
        Exception: if there are no more cards in the list
        """
        if self.current_position >= len(self.deck):
            raise Exception("last card")

        self.current_position += 1
    
    def reset_deck(self) -> None:
        """Reorders the deck of cards and sets the position back to the start."""
        self.current_position = 0
        self.shuffle_deck()




