
import unittest
from unittest.mock import Mock
import io
import pytest

from ..game import Game
from ..deck import Deck


class TestGame(unittest.TestCase):
    def test_initial_game_values(self):
        """Tests the Game class is initiialsed with the score set to 0."""
        game = Game()

        assert game.score == 0
    
    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    @unittest.mock.patch("higherlowergame.game.Game.play_game")
    def test_new_game(self, mock_play_game, mock_stdout):
        """Tets the new game_method starts up a new game with a new deck and rounds then starts the game."""

        game = Game()

        game.new_game()

        assert isinstance(game.deck, Deck)
        assert game.max_rounds == 3
        assert mock_play_game.assert_called_once
        assert "Instrunctions" in mock_stdout.getvalue()

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    @unittest.mock.patch("higherlowergame.game.Game.play_round")
    @unittest.mock.patch("higherlowergame.game.Game.replay_question")
    def test_play_game(self, replay_question, mock_play_round, mock_stdout):
        """Tests the play game method will loop over each round, display the final score and ask if the player wants to replay"""
    
        game = Game()
        max_rounds = 2
        game.max_rounds = max_rounds
        game.deck = Deck()
        final_score = 4
        game.score = final_score

        game.play_game()

        assert mock_play_round.call_count == max_rounds
        assert replay_question.assert_called_once
        assert str(final_score) in mock_stdout.getvalue()

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    @unittest.mock.patch("higherlowergame.game.Deck")
    @unittest.mock.patch("higherlowergame.game.Game.take_guess")
    def test_play_round_higher_correct(self, mock_take_guess, mock_deck, mock_stdout):
        """Tests the play round method adds 1 to the score if the guess was correct (higher) the first round"""
        game = Game()
        initial_score = 4
        game.score = initial_score

        first_card = Mock()
        first_card.card_value.return_value = 3
        first_card_name = "3H"
        first_card.card_name.return_value = first_card_name
        mock_deck.previous_card.return_value = first_card

        current_card = Mock()
        current_card.card_value.return_value = 6
        current_card_name = "6S"
        current_card.card_name.return_value = current_card_name
        current_card.compare_cards.return_value = 1
        mock_deck.current_card.return_value = current_card

        deck_intitial_position = 0
        game.deck = mock_deck
        game.deck.current_position = deck_intitial_position

        mock_take_guess.return_value = 1

        game.play_round(0)

        stdout =  mock_stdout.getvalue()
        assert f"The first card is {first_card_name}" in stdout
        assert mock_take_guess.called_once()
        assert f"The next card is {current_card_name}" in stdout
        assert mock_take_guess.called_once()
        current_card.compare_cards.assert_called_once_with(first_card)
        assert f"The next card's value is higher" in stdout
        assert f"you got it right!" in stdout
        assert game.score == initial_score+1

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    @unittest.mock.patch("higherlowergame.game.Deck")
    @unittest.mock.patch("higherlowergame.game.Game.take_guess")
    def test_play_round_lower_incorrect(self, mock_take_guess, mock_deck, mock_stdout):
        """Tests the play round method removes 1 from the score if the guess was incorrect (lower) not in the first round"""
        game = Game()
        initial_score = 4
        game.score = initial_score

        previous_card = Mock()
        previous_card.card_value.return_value = 3
        previous_card_name = "3H"
        previous_card.card_name.return_value = previous_card_name
        mock_deck.previous_card.return_value = previous_card

        current_card = Mock()
        current_card.card_value.return_value = 6
        current_card_name = "6S"
        current_card.card_name.return_value = current_card_name
        current_card.compare_cards.return_value = -1
        mock_deck.current_card.return_value = current_card

        game.deck = mock_deck
        deck_intitial_position = 2
        game.deck.current_position = deck_intitial_position

        mock_take_guess.return_value = 1

        game.play_round(1)

        stdout =  mock_stdout.getvalue()
        assert f"The previous card was {previous_card_name}" in stdout
        assert mock_take_guess.called_once()
        assert f"The next card is {current_card_name}" in stdout
        assert mock_take_guess.called_once()
        current_card.compare_cards.assert_called_once_with(previous_card)
        assert f"The next card's value is lower" in stdout
        assert f"you guessed wrong" in stdout
        assert game.score == initial_score-1


    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    @unittest.mock.patch("higherlowergame.game.Deck")
    @unittest.mock.patch("higherlowergame.game.Game.take_guess")
    def test_play_round_equal(self, mock_take_guess, mock_deck, mock_stdout):
        """Tests the play round methodleaves the score as it was when the cards value match"""
        game = Game()
        initial_score = 4
        game.score = initial_score

        previous_card = Mock()
        previous_card.card_value.return_value = 6
        previous_card_name = "6H"
        previous_card.card_name.return_value = previous_card_name
        mock_deck.previous_card.return_value = previous_card

        current_card = Mock()
        current_card.card_value.return_value = 6
        current_card_name = "6S"
        current_card.card_name.return_value = current_card_name
        current_card.compare_cards.return_value = 0
        mock_deck.current_card.return_value = current_card

        game.deck = mock_deck
        deck_intitial_position = 2
        game.deck.current_position = deck_intitial_position

        mock_take_guess.return_value = 1

        game.play_round(1)

        stdout =  mock_stdout.getvalue()
        assert f"The card's values match" in stdout
        assert game.score == initial_score

    @unittest.mock.patch("builtins.input")
    def test_take_guess_higher(self, mock_input):
        """Test the take guess method returns 1 when guessing higher"""
        mock_input.return_value = "h"

        guess = Game.take_guess()

        assert guess == 1
    
    @unittest.mock.patch("builtins.input")
    def test_take_guess_lower(self, mock_input):
        """Test the take guess method returns -1 when guessing lower"""
        mock_input.return_value = "l"

        guess = Game.take_guess()

        assert guess == -1

    @unittest.mock.patch("builtins.input")
    def test_take_guess_invalid_input(self, mock_input):
        """Test the take guess method asks again if the user doesnt enter l or h"""
        mock_input.side_effect = ["anthing", "else", "l"]

        Game.take_guess()


        assert mock_input.call_count == 3

        





