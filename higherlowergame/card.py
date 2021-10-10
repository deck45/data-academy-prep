from __future__ import annotations

suits = {
    "Clubs": "C", 
    "Diamonds": "D", 
    "Hearts": "H", 
    "Spades": "S"
}

values = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13
}


class Card:
    """
    A class to represent a Card

    Attributes
    ----------
    suit : str
        The suit of the card
    value: str
        The name of the card mapping to a numerical value 1-13

    Methods
    -------
    card_name():
        Returns a human readable card name.
    card_value():
        Returns the numerical value of a card.
    compare_cards(previous_card):
        Takes another Card and returns which has the higher value.
    """
    def __init__(self, suit: str, value: str) -> None:
        """
        Constructs all the attributes for a card object

        Parameters
        ----------
        suit: str
            The suit of the card
        value: str
            The name of the card

        """
        self.suit = suit
        self.value = value
    
    def card_name(self) -> str:
        """Returns a human readable card name."""
        return f"{self.value}{suits[self.suit]}"

    def card_value(self) -> str:
        """Returns the numerical value of a card."""
        return values[self.value]

    def compare_cards(self, previous_card: Card) -> int:
        """
        Takes another Card and returns which has the higher value.

        Parameters
        ----------
        previous_card (Card): Another card

        Returns
        -------
        compare_result (int): An integer describing which card had the higher value, 1 for this card, -1 for the previous_card and 0 if they match
        """
        current_value = self.card_value()
        previous_value = previous_card.card_value()

        if current_value == previous_value:
            return 0
        elif current_value > previous_value:
            return 1
        else:
            return -1
