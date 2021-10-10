from .game import Game

def main() -> None:
    """Start a new game."""
    game = Game()
    game.new_game()

if __name__ == "__main__":
    main()