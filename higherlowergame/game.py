from .deck import Deck

class Game:
    """
        A class to represent a full game tracking the score and controlling each round.

        Attributes
        ----------
        score : int
            The player score of the current round
        max_rounds : int
            How many rounds a game consists of
        deck : Deck
            The full deck of cards used in the game
        current_round : int
            The round the player is currently on

        Methods
        -------
        new_game():
            Sets up a new game.
        play_game():
            Plays all rounds of a new game.
        play_round(round_number: int):
            Plays a specific round of a game.
        take_guess():
            Asks the user to guess higher or lower.
        replay_question():
            Asks the user if they want to replay and starts a new game if so.
    """
    def __init__(self):
        """ Set up a new game"""
        self.score = 0
    
    def new_game(self) -> None:  
        """
        Sets up a new game.

        Sets the max number of rounds, creates the deck of cards, tells the user how to play and starts the game.
        """

        print("Welcome to the Higher/Lower game.")
        self.max_rounds = 3
        self.deck = Deck()

        print(f"""
Instrunctions: 
Press 'h' for higher and 'l' for lower depending on what you think the next card might be.
You score 1 point if you guess right, lose 1 point if you guess wrong and score no points if they match
There are {self.max_rounds} rounds in a game.
Good Luck!
""")
        self.play_game()


    def play_game(self) -> None:
        """
        Plays all rounds of a new game.

        Runs each round of the game from 0.
        After the last round tells the user their final score and asks if they want to play again.
        """

        print(f"Setting up a new game.")
        self.current_round = 0

        for round_number in range(self.max_rounds):
            self.play_round(round_number)
        
        print("Game Over")
        print(f"Your final score was: {self.score}")
        self.replay_question()
        

    def play_round(self, round_number: int) -> None:
        """
            Plays a specific round of a game.

            Starts a new round by taking the next card from the deck.
            Shows the user the previous card and asks the user to guess higher or lower.
            Take the next card from the deck and compares the values.
            If the user was right add one point to their score, if they were wrong remove one point, if they match then keep the same score.


            Parameters
            ----------
            round_number (int):The round number to play

        """
        print(f"Rounder number {round_number+1}:")
        
        self.deck.move_to_next_card()
        previous_card = self.deck.previous_card()
        current_card = self.deck.current_card()

        print(f"The {'first card is' if round_number == 0 else 'previous card was'} {previous_card.card_name()}")
        guess = Game.take_guess()
        
        print(f"The next card is {current_card.card_name()}")
        answer = current_card.compare_cards(previous_card)
        result = "higher" if answer == 1 else "lower"

        if answer == 0:
            print(f"The card's values match. Your score is still {self.score}")
        elif answer == guess:
            self.score = self.score + 1
            print(f"The next card's value is {result}, you got it right! You gain 1 point and your current score is {self.score}")
        else:
            self.score = self.score - 1
            print(f"The next card's value is {result}, you guessed wrong. You lose 1 point and your current score is {self.score}")

    
    @staticmethod
    def take_guess() -> int:
        """
        Asks the user to guess higher or lower.
        
        Takes an input from the user to guess h or l and returns 1 and -1 respectively.
        If the user types anything else remind the user to only enter l or h and call the function again.

        Returns
        ------
        guess (int): An integer for the users guess, 1 if a higher guess and -1 is a lower guess
        """
        guess = input("Is the next card higher (h) or lower (l): ")
        print(guess)

        if guess != "h" and guess != "l":
            print("Please only enter 'h' or 'l' to guess")
            return Game.take_guess()
        
        if guess == "h":
            return 1
        else:
            return -1


    def replay_question(self) -> None:
        """Asks the user if they want to replay and starts a new game if so."""
        replay = input("Would you like to play again? Yes (y) or No (n): ")
        
        if replay != "y" and replay != "n":
            print("Please only answer with 'y' or 'n'")
            self.replay_question()
        
        elif replay == "n":
            print("Thank you for playing.")

        else: 
            self.play_game()
        



        
