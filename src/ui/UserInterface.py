from src.ui.HealthBar import HealthBar
from config import SCREEN_HEIGHT
from config import SCREEN_WIDTH

class UserInterface:
    def __init__(self, batch, group):
        self.health_bar = HealthBar(0, SCREEN_HEIGHT - 50, batch, group)