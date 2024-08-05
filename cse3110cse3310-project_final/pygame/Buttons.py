"""
Title: Button
Author: Marco Ou
Date: May 15th 2024
"""

import pygame
from box import Box
from text import Text
from Window import Window
from Colors import Color
from my_sprite import MySprite


class Button(MySprite):
    def __init__(self, width, height, x=0, y=0, text="", return_text="", font_size=36, border=False, tx=0, ty=0):
        MySprite.__init__(self, width=width, height=height, x=x, y=y)
        self.__x = x
        self.__y = y
        self.__string_text = text
        self.__font_size = font_size
        self._surface = pygame.Surface(self._dimensions, pygame.SRCALPHA, 32)
        self._surface.fill(Color.WHITE)
        self.__text = Text(text, x, y, "Arial", font_size)
        self.__border = border
        self.__return_text = return_text
        self.return_function = None
        if tx == 0 and ty == 0:
            self.__text.setPosition((x+width//2) - self.__text.get_width()//2, (y + height // 2) - self.__text.get_height()//2)
        elif tx and not ty:
            self.__text.setPosition(x+2, (y + height // 2) - self.__text.get_height()//2)
        if self.__border:
            self.__TOP_BORDER = Box(width, 1, x, y, Color.BLACK)
            self.__BOTTOM_BORDER = Box(width, 1, x, y + height - 1, Color.BLACK)
            self.__LEFT_BORDER = Box(1, height, x, y, Color.BLACK)
            self.__RIGHT_BORDER = Box(1, height, x + width, y, Color.BLACK)

    def onHover(self) -> bool:
        """
        if mouse is over button return True
        :return: bool
        """
        MOUSE_POSITION = pygame.mouse.get_pos()
        if self.getX() <= MOUSE_POSITION[0] <= self.getX() + self.get_width() and self.getY() <= MOUSE_POSITION[
            1] <= self.getY() + self.get_height():
            return True

    def getClick(self) -> bool:
        """
        if mouse is over button and gets click returns True
        :return: bool
        """
        MOUSE_PRESSED = pygame.mouse.get_pressed(num_buttons=3)
        if MOUSE_PRESSED[0] and self.onHover():
            return True

    def setColor(self, new_color):
        self._surface.fill(new_color)

    def displayButton(self, WINDOW):
        WINDOW.getScreen().blit(self.getSurface(), self.getPosition())
        WINDOW.getScreen().blit(self.__text.getSurface(), self.__text.getPosition())
        if self.__border:
            WINDOW.getScreen().blit(self.__TOP_BORDER.getSurface(), self.__TOP_BORDER.getPosition())
            WINDOW.getScreen().blit(self.__BOTTOM_BORDER.getSurface(), self.__BOTTOM_BORDER.getPosition())
            WINDOW.getScreen().blit(self.__LEFT_BORDER.getSurface(), self.__LEFT_BORDER.getPosition())
            WINDOW.getScreen().blit(self.__RIGHT_BORDER.getSurface(), self.__RIGHT_BORDER.getPosition())

    def returnText(self):
        return self.__return_text
