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

        # Параметры снаряда
        self.bullet_speed = 3
        self.bullet_height = 12
        self.bullet_width = 5
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 4

        # Настройки пришельцев
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1