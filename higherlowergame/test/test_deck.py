
import unittest
import pytest

from ..deck import Deck 
from ..card import Card, suits, values

class TestDeck(unittest.TestCase):
    def test_initial_deck_values(self):
        """Test the card class is initialised with the correct values and calls the shuffle_deck method"""
        ordered_deck = []
        for card_suit in suits.keys():
            for card_value in values.keys():
                ordered_deck.append(Card(card_suit, card_value))
        
        deck = Deck()
        
        assert len(deck.deck) == 52
        assert deck.current_position == 0
    
    def test_current_card(self):
        """Tests the current card method returns the card in the current position of the deck"""
        deck = Deck()
        position = 23
        deck.current_position = position
        current_card = deck.deck[position]

        result = deck.current_card()

        assert result == current_card

    def test_previous_card(self):
        """Tests the previous card method returns the card in the before the one in the current position of the deck"""
        deck = Deck()
        position = 23
        deck.current_position = position
        previous_card = deck.deck[position-1]

        result = deck.previous_card()

        assert result == previous_card

    
    def test_move_to_next_card(self):
        """Tests the move to next card method moves the current position along if its not the last position"""
        deck = Deck()
        position = 23
        deck.current_position = position

        deck.move_to_next_card()

        assert deck.current_position == position+1

    def test_move_to_next_card_errors_on_last_card(self):
        """Tests the move to next card method moves throws an excpetion if trying to move past the end of the deck"""
        deck = Deck()
        deck.current_position = 52

        with pytest.raises(Exception) as error:
            deck.move_to_next_card()
        
        assert "last card" in str(error.value)
    
    def test_reset_deck(seld):
        """Tests the reset_deck method will set the deck poition back to 0 and shuffel the cards"""
        deck = Deck()
        deck.current_position = 23
        initial_deck = deck.deck.copy()

        deck.reset_deck()

        assert deck.deck != initial_deck
        assert deck.current_position == 0



        


       


if __name__ == "__main__":
    unittest.main()