from pathlib import Path
import json

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self,ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        self.ai_game = ai_game
        # Reset to 0 to restart all highscores
        self.path = Path('highscore.json')
        contents = self.path.read_text()
        self.new = json.loads(contents)
        # High score should never be reset.
        self.high_score = self.new


    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1