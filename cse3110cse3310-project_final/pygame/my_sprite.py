# my_sprite.py in f_inheritance folder

"""
Title: The my sprite abstract class
Author: Marco Ou
Date: April 18th 2024
"""

from Colors import Color
import pygame


class MySprite:
    """
    Abstract sprite class to build other sprites
    """

    def __init__(self, width=0, height=0, x=0, y=0, speed=10, color=Color.WHITE):
        self.__width = width
        self.__height = height
        self._dimensions = (self.__width, self.__height)
        self._x = x
        self._y = y
        self.__position = (self._x, self._y)
        self.__speed = speed
        self._color = color
        self._surface = pygame.Surface
        self.__dir_x = 1
        self.__dir_y = 1

    # Modifier Methods (setter methods)
    def stopAtEdge(self, max_width, max_height, min_width=0, min_height=0):
        if self._x > max_width - self._surface.get_width():
            self._x = max_width - self._surface.get_width()
        if self._x < min_width:
            self._x = min_width

        if self._y > max_height - self._surface.get_height():
            self._y = max_height - self._surface.get_height()
        if self._y < min_height:
            self._y = min_height
        self._updatePosition()

    def WASDMove(self, pressed_keys):
        if pressed_keys[pygame.K_d]:
            self._x += self.__speed
        if pressed_keys[pygame.K_a]:
            self._x -= self.__speed
        if pressed_keys[pygame.K_w]:
            self._y -= self.__speed
        if pressed_keys[pygame.K_s]:
            self._y += self.__speed
        self._updatePosition()

    def marqueeX(self, max_x, min_x=0):
        self._x += self.__speed
        if self._x > max_x:
            self._x = min_x - self._surface.get_width()
        self._updatePosition()

    def setWidth(self, WIDTH):
        self.__width = WIDTH

    def setHeight(self, HEIGHT):
        self.__height = HEIGHT

    def setColor(self, new_color):
        """
        This only changes the variable, it does not change the surface
        :param new_color: tuple
        :return: None
        """
        self._color = new_color

    def setPosition(self, x, y):
        self._x = x
        self._y = y
        self._updatePosition()

    def _updatePosition(self):
        self.__position = (self._x, self._y)

    # Accessor Methods (getter methods)
    # def getX(self):
        # return self.__x

    def getSurface(self):
        return self._surface

    def getPosition(self):
        return self.__position

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def getX(self):
        return self._x

    def getY(self):
        return self._y
      
    def getColor(self):
        return self._color


