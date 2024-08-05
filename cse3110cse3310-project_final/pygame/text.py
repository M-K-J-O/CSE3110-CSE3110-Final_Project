# text.py in f_inheritance folder

"""
Title:
Author: Marco Ou
Date: April 18th 2024
"""

from my_sprite import MySprite
import pygame
from Colors import Color


class Text(MySprite):

    def __init__(self, text, x=0, y=0, font_family="Arial", font_size=36):
        MySprite.__init__(self, x=x, y=y)
        self.__text = text
        self.__font_family = font_family
        self.__font_size = font_size
        self.__font = pygame.font.SysFont(self.__font_family, self.__font_size)
        self._surface = self.__font.render(self.__text, True, Color.BLACK)
        self.__width, self.__height = self.__font.size(text)

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height





