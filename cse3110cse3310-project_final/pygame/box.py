# box.py in f_inheritance folder

"""
Title: Box Class
Author: Marco Ou
Date Created: April 19th 2024
"""

from my_sprite import MySprite
import pygame
from random import randrange
from Colors import Color


class Box(MySprite):

    def __init__(self, width=1, height=1, x=0, y=0, color=Color.WHITE):
        MySprite.__init__(self, width=width, height=height, x=x, y=y, )
        # super().__init__(width=width, height=height) This does the same thing as the line above
        self._color = color
        self._surface = pygame.Surface(self._dimensions, pygame.SRCALPHA, 32)
        self._surface.fill(self._color)

    def setColor(self, new_color):
        MySprite.setColor(self, new_color)
        self._surface.fill(self._color)
    
    def getColor(self):
        return MySprite.getColor(self)

    def setScale(self, scale_x, scale_y=None):
        """
        changes the scale of the image making it bigger or smaller
        :param scale_x: float
        :param scale_y: float
        :return: None
        """
        if scale_y is None:
            scale_y = scale_x

        self._surface = pygame.transform.scale(self._surface, (self.get_width()*scale_x, self.get_height()*scale_y))



