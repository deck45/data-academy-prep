import unittest

from ..card import Card

class TestCard(unittest.TestCase):
    def test_initial_card_value(self):
        """Test the card class is initialised with the correct values."""
        card = Card("Clubs", "8")
        assert card.suit == "Clubs"
        assert card.value == "8"

    def test_card_name(self):
        """Test the card_name method returns the correct card description."""
        card = Card("Clubs", "8")
        card_name = card.card_name()
        assert card_name == "8C"

    def test_card_value(self):
        """Test the card_value method returns the number value of a card."""
        card = Card("Clubs", "8")
        card_value = card.card_value()
        assert card_value == 8

    def test_compare_cards_higher(self):
        """Test the compare_cards method returns 1 when the current card is higher."""
        card = Card("Clubs", "8")
        previous_card = Card("Hearts", "6")
        compare = card.compare_cards(previous_card)
        assert compare == 1

        
    def test_compare_cards_lower(self):
        """Test the compare_cards method returns -1 when the current card is lower."""
        card = Card("Clubs", "8")
        previous_card = Card("Hearts", "Q")
        compare = card.compare_cards(previous_card)
        assert compare == -1

        
    def test_compare_cards_same(self):
        """Test the compare_cards method returns 0 when the current card is the same as the previous."""
        card = Card("Clubs", "8")
        previous_card = Card("Hearts", "8")
        compare = card.compare_cards(previous_card)
        assert compare == 0

if __name__ == "__main__":
    unittest.main()