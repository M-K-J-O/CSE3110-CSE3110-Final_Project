"""
Title: Graphing Inputs
Author: Marco Ou & Rana Deep Chohan
Date: May 27th 2024
"""

# Imports
import pygame
from Window import Window
from Colors import Color
from Buttons import Button
from graph import Graph
import unicodedata
import re
from Math_Functions import *

# VARIABLES
TIME = 0
TEMP_TIME = 0
pygame.init()
clock = pygame.time.Clock()
WINDOW = Window("Graphing Inputs", 400, 580)  # Window name and size
SECOND_BUTTONS = False  # the State of the buttons with a second version
HYPO_BUTTON = False  # the State of the buttons with a HYPO version
button_box_width = (WINDOW.getVirtualWidth() - 24) / 5
button_box_height = (WINDOW.getVirtualHeight() - 44) / 12
BUTTON_NUMBER = 0
ans = 0  # Variable used for getting the number in the output box, can be used in the input box once a valid output exists
BUTTON = []  # Holds Button objects
input_text_size = 32  # size of the text in the input box
input_box_width = WINDOW.getVirtualWidth() - 8  # width of the input box
input_box_height = 64  # height of the input box
user_text = 'Enter a Expression'  # USER INPUT TEXT
input_box_active_state = False  # dictates whether or not the user can type into the input
output_text = ""  # OUTPUT TEXTBOX TEXT
BUTTON_RETURN_VALUES = [
    # "Button Text", "Actual output text",
    ["ENTER", "ENTER_FUNCTION", 0],
    [".", ".", 1],
    ["0", "0", 2],
    ["(-)", "(-", 3],
    ["ln(x)", "ln(", "e^x", "e**", 4],
    ["+", "+", 5],
    ["3", "3", 6],
    ["2", "2", 7],
    ["1", "1", 8],
    ["log(x)", "log(", "log(x, b)", "log(", 9],
    ["-", "-", 10],
    ["6", "6", 11],
    ["5", "5", 12],
    ["4", "4", 13],
    ["10^x", "10**(", "2^x", "2**", 14],
    ["*", "*", 15],
    ["9", "9", 16],
    ["8", "8", 17],
    ["7", "7", 18],
    ["x^y", "**(", "root(x, y, z)", "root(", 19],
    ["/", "/", 20],
    ["=", "=", 21],
    [")", ")", 22],
    ["(", "(", 23],
    ["sqr(x)", "root(", "cbr(x)", "cbr(", 24],
    ["y", "y", 25],
    ["x", "x", 26],
    ["|x|", "abs(", 27],
    ["1/x", "1/", 28],
    ["x^2", "**2", 29],
    ["<x]", "BACKSPACE_FUNCTION"],
    ["C", "CLEAR_FUNCTION", 31],
    ["e", "e", 32],
    [unicodedata.lookup("GREEK SMALL LETTER PI"), "pi", 33],
    ["2nd", "SECOND_FUNCTION", 34],
    ["sin", "sin(", "asin", "asin(", "sinh", "sinh(", "asinh", "asinh("],
    ["cos", "cos(", "acos", "acos(", "cosh", "cosh(", "acosh", "acosh("],
    ["tan", "tan(", "atan", "atan(", "tanh", "tanh(", "atanh", "atanh("],
    ["floor(x)", "floor(", "ceiling(x)", "ceiling("],
    ["hyp", "HYPO_FUNCTION"],
    ["cot", "cot(", "acot", "acot(", "coth", "coth(", "acoth", "acoth("],
    ["csc", "csc(", "acsc", "acsc(", "csch", "csch(", "acsch", "acsch("],
    ["sec", "sec(", "asec", "asec(", "sech", "sech(", "asech", "asech("],
    ["<", "<", "<=", "<="],
    [">", ">", "=>", "=>"]

]  # holds button tet, and return text

# OBJECTS
input_box = Button(input_box_width, input_box_height, 4, 4, user_text, None, input_text_size, False, 1)
OUTPUT_BOX = Button(input_box_width, input_box_height, 4, input_box_height + 8, output_text, None, input_text_size,
                    False, 1)


# FUNCTIONS
def parse(strexq):
    parsed = []
    counter = 0
    Error = ""
    isX = False

    parsed = re.sub(r'(?<=\d)(x|y)', r'*\1', strexq)
    parsed = re.sub(r'\)(\d)', r')*\1', parsed)

    parsed = re.sub(r'sin\((.*?)\)', r'np.sin(\1)', parsed)
    parsed = re.sub(r'cos\((.*?)\)', r'np.cos(\1)', parsed)
    parsed = re.sub(r'tan\((.*?)\)', r'np.tan(\1)', parsed)
    parsed = re.sub(r'asin\((.*?)\)', r'np.arcsin(\1)', parsed)
    parsed = re.sub(r'acos\((.*?)\)', r'np.arccos(\1)', parsed)
    parsed = re.sub(r'atan\((.*?)\)', r'np.arctan(\1)', parsed)

    # split parsed for further processing
    parsed = list(parsed)

    parsed = ''.join(parsed)
    # checking if both x and y are present after parsed to make sure they work in plotting
    if 'x' in parsed and 'y' in parsed:
        Error = "Cannot parse your expression"
    elif 'x' in parsed:  # needed to know for plot
        isX = True
    return parsed, isX, Error


def outputFunc():
    global output_text
    global ans
    try:
        is_exq = False
        if "x" in user_text:
            is_exq = True
            output, isX, Error = parse(user_text)
            print(output, (isX != True))
        if not is_exq:
            ans = eval(user_text)
            output_text = f"{ans}"
        else:
            if Error:
                output_text = f"{Error}"
            else:
                GRAPH = Graph()
                GRAPH.plot(output, (isX != True))
    except Exception as Err:
        print(f"Error, {Err}")
        output_text = f"Error, {Err}"
        if user_text == "Enter a Expression":
            output_text = ""


# Main Code Body
if __name__ == "__main__":
    # Button Creator
    for layer in range(9):
        BUTTON_Y = WINDOW.getVirtualHeight() - (layer + 1) * (button_box_height + 4)
        for button in range(5):
            BUTTON_X = WINDOW.getVirtualWidth() - (button + 1) * (button_box_width + 4)
            BUTTON.append(
                Button(button_box_width, button_box_height, BUTTON_X, BUTTON_Y, BUTTON_RETURN_VALUES[BUTTON_NUMBER][0],
                       BUTTON_RETURN_VALUES[BUTTON_NUMBER][1], 16))
            BUTTON_NUMBER += 1

    # Running Loop
    while True:
        TIME += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.onHover():
                    input_box_active_state = True
                else:
                    input_box_active_state = False
                    if user_text == "":
                        user_text = "Enter a Expression"
            if event.type == pygame.KEYDOWN and input_box_active_state:
                if event.key == pygame.K_BACKSPACE:
                    if user_text == "Enter a Expression":
                        user_text = ""
                    user_text = user_text[:-1]
                elif event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    outputFunc()
                else:
                    if user_text == "Enter a Expression":
                        user_text = ""
                    user_text += event.unicode

        if input_box.onHover():
            input_box.setColor(Color.SILVER)
        else:
            input_box.setColor(Color.WHITE)

        INDEX = 0
        for button in BUTTON:
            if len(BUTTON_RETURN_VALUES[INDEX]) > 3:
                if HYPO_BUTTON and SECOND_BUTTONS and len(BUTTON_RETURN_VALUES[INDEX]) > 6:
                    BUTTON.pop(INDEX)
                    BUTTON.insert(INDEX, Button(button_box_width, button_box_height, button.getX(), button.getY(),
                                                BUTTON_RETURN_VALUES[INDEX][6], BUTTON_RETURN_VALUES[INDEX][7], 16))
                elif HYPO_BUTTON and len(BUTTON_RETURN_VALUES[INDEX]) > 5:
                    BUTTON.pop(INDEX)
                    BUTTON.insert(INDEX, Button(button_box_width, button_box_height, button.getX(), button.getY(),
                                                BUTTON_RETURN_VALUES[INDEX][4], BUTTON_RETURN_VALUES[INDEX][5], 16))
                elif SECOND_BUTTONS:
                    BUTTON.pop(INDEX)
                    BUTTON.insert(INDEX, Button(button_box_width, button_box_height, button.getX(), button.getY(),
                                                BUTTON_RETURN_VALUES[INDEX][2], BUTTON_RETURN_VALUES[INDEX][3], 16))
                else:
                    BUTTON.pop(INDEX)
                    BUTTON.insert(INDEX, Button(button_box_width, button_box_height, button.getX(), button.getY(),
                                                BUTTON_RETURN_VALUES[INDEX][0], BUTTON_RETURN_VALUES[INDEX][1], 16))

            if button.onHover():
                if button.getClick() and TIME - TEMP_TIME >= 16:
                    TEMP_TIME = TIME
                    if button.returnText() == "ENTER_FUNCTION":
                        outputFunc()
                    elif button.returnText() == "BACKSPACE_FUNCTION":
                        if user_text == "Enter a Expression":
                            user_text = ""
                        user_text = user_text[:-1]
                    elif button.returnText() == "CLEAR_FUNCTION":
                        user_text = ""
                    elif button.returnText() == "SECOND_FUNCTION":
                        if not SECOND_BUTTONS:
                            SECOND_BUTTONS = True
                        else:
                            SECOND_BUTTONS = False
                    elif button.returnText() == "HYPO_FUNCTION":
                        if not HYPO_BUTTON:
                            HYPO_BUTTON = True
                        else:
                            HYPO_BUTTON = False
                    else:
                        if user_text == "Enter a Expression":
                            user_text = ""
                        user_text += button.returnText()
            elif not button.onHover():
                button.setColor(Color.WHITE)
            INDEX += 1

        WINDOW.clearScreen()
        input_box = Button(input_box_width, input_box_height, 4, 4, user_text, None, input_text_size, False, 1)
        OUTPUT_BOX = Button(input_box_width, input_box_height, 4, input_box_height + 8, output_text, None,
                            input_text_size, False, 1)
        input_box.displayButton(WINDOW)
        OUTPUT_BOX.displayButton(WINDOW)
        for button in BUTTON:
            if button.onHover():
                button.setColor(Color.SILVER)
            button.displayButton(WINDOW)
        WINDOW.updateFrame()
        clock.tick(60)
