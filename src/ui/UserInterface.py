#./src/ui/UserInterface.py
from src.ui.HealthBar import HealthBar
from config import SCREEN_HEIGHT

class UserInterface:
    def __init__(self, batch):
        self.health_bar = HealthBar(60, SCREEN_HEIGHT - 60, batch)