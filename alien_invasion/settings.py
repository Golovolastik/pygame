import pygame

class Settings():
    """Класс для хранения всех настроек игры Alien Invasion"""

    def __init__(self):
        """Инициализирует настройки игры"""
        pygame.display.set_caption('Alien Invasion')

        # Параметры экрана
        self.bg_color = (230, 230, 230)
        
        # Настройки корабля
        self.ship_speed = 5