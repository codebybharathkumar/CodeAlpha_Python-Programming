import random

class HangmanGame:
    def __init__(self):
        # Predefined list of 5 words as per requirements
        self.words = ["python", "computer", "programming", "software", "developer"]
        self.max_incorrect_guesses = 6
        self.reset_game()
    
    def reset_game(self):
        """Reset the game state for a new round"""
        self.word = random.choice(self.words).upper()
        self.guessed_letters = []
        self.incorrect_guesses = 0
        self.game_over = False
        self.won = False
    
    def display_hangman(self):
        """Display hangman figure based on incorrect guesses"""
        stages = [
            # Stage 0 - No mistakes
            """
               ___
              |   |
              |
              |
              |
              |
            __|__
            """,
            # Stage 1
            """
               ___
              |   |
              |   O
              |
              |
              |
            __|__
            """,
            # Stage 2
            """
               ___
              |   |
              |   O
              |   |
              |
              |
            __|__
            """,
            # Stage 3
            """
               ___
              |   |
              |   O
              |  /|
              |
              |
            __|__
            """,
            # Stage 4
            """
               ___
              |   |
              |   O
              |  /|\\
              |
              |
            __|__
            """,
            # Stage 5
            """
               ___
              |   |
              |   O
              |  /|\\
              |  /
              |
            __|__
            """,
            # Stage 6 - Game Over
            """
               ___
              |   |
              |   O
              |  /|\\
              |  / \\
              |
            __|__
            """
        ]
        return stages[self.incorrect_guesses]
    
    def display_word(self):
        """Display the word with guessed letters revealed"""
        display = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        return display.strip()
    
    def is_word_guessed(self):
        """Check if the entire word has been guessed"""
        for letter in self.word:
            if letter not in self.guessed_letters:
                return False
        return True
    
    def make_guess(self, guess):
        """Process a player's guess"""
        guess = guess.upper()
        
        # Check if already guessed
        if guess in self.guessed_letters:
            return "already_guessed"
        
        # Add to guessed letters
        self.guessed_letters.append(guess)
        
        # Check if guess is correct
        if guess in self.word:
            # Check if word is completely guessed
            if self.is_word_guessed():
                self.game_over = True
                self.won = True
            return "correct"
        else:
            self.incorrect_guesses += 1
            # Check if game is over
            if self.incorrect_guesses >= self.max_incorrect_guesses:
                self.game_over = True
                self.won = False
            return "incorrect"
    
    def get_game_stats(self):
        """Return current game statistics"""
        return {
            "word_display": self.display_word(),
            "guessed_letters": sorted(self.guessed_letters),
            "incorrect_guesses": self.incorrect_guesses,
            "max_guesses": self.max_incorrect_guesses,
            "remaining_guesses": self.max_incorrect_guesses - self.incorrect_guesses
        }

def display_welcome():
    """Display welcome message and game rules"""
    print("="*50)
    print("🎮 WELCOME TO HANGMAN GAME 🎮")
    print("="*50)
    print("Rules:")
    print("• Guess the word one letter at a time")
    print("• You have 6 incorrect guesses before losing")
    print("• Enter single letters only")
    print("• Good luck!")
    print("="*50)

def display_game_state(game):
    """Display current game state"""
    print("\n" + "="*40)
    print(game.display_hangman())
    print("="*40)
    
    stats = game.get_game_stats()
    print(f"Word: {stats['word_display']}")
    print(f"Guessed letters: {', '.join(stats['guessed_letters']) if stats['guessed_letters'] else 'None'}")
    print(f"Remaining guesses: {stats['remaining_guesses']}")
    print("="*40)

def get_player_guess():
    """Get and validate player input"""
    while True:
        guess = input("\nEnter your guess (single letter): ").strip()
        
        if len(guess) != 1:
            print("❌ Please enter exactly one letter!")
            continue
        
        if not guess.isalpha():
            print("❌ Please enter a valid letter!")
            continue
        
        return guess

def play_hangman():
    """Main game loop"""
    game = HangmanGame()
    display_welcome()
    
    while True:
        # Display current game state
        display_game_state(game)
        
        # Check if game is over
        if game.game_over:
            if game.won:
                print("🎉 CONGRATULATIONS! You won! 🎉")
                print(f"The word was: {game.word}")
            else:
                print("💀 GAME OVER! You lost! 💀")
                print(f"The word was: {game.word}")
            
            # Ask if player wants to play again
            play_again = input("\nDo you want to play again? (y/n): ").strip().lower()
            if play_again == 'y' or play_again == 'yes':
                game.reset_game()
                print("\n🔄 Starting new game...")
                continue
            else:
                print("Thanks for playing Hangman! Goodbye! 👋")
                break
        
        # Get player guess
        guess = get_player_guess()
        
        # Process the guess
        result = game.make_guess(guess)
        
        if result == "already_guessed":
            print(f"⚠️  You already guessed '{guess.upper()}'! Try a different letter.")
        elif result == "correct":
            print(f"✅ Great! '{guess.upper()}' is in the word!")
        elif result == "incorrect":
            print(f"❌ Sorry! '{guess.upper()}' is not in the word.")

if __name__ == "__main__":
    play_hangman()