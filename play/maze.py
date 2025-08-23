import os

import pyautogui

import controller


CARDS_TOP = 41
CARDS_PADDING = 2
LEFT_COLUMN_LEFT = 8
RIGHT_COLUMN_LEFT = 256
CARD_WIDTH = 56
CARD_HEIGHT = 30
COLUMN_SIZE = 3
TOTAL_WIDTH = 320
TOTAL_HEIGHT = 200


def get_number_of_characters(pictures_dir="pictures", precision=0.95):
    pos = controller.find_image(os.path.join(pictures_dir, "wizardry.png"))
    if pos[0] == -1:
        return None
    left, top, right, bottom = controller.window_region()
    top = pos[1]
    window = pyautogui.screenshot(region=(left, top, right-left, bottom-top))
    w, h = window.size
    i = 0
    characters = 0
    for row in range(COLUMN_SIZE):
        for left in (LEFT_COLUMN_LEFT, RIGHT_COLUMN_LEFT):
            card = window.crop((
                left * w // TOTAL_WIDTH,
                (CARDS_TOP + row * (CARD_HEIGHT + CARDS_PADDING)) * h // TOTAL_HEIGHT,
                (left + CARD_WIDTH) * w // TOTAL_WIDTH,
                (CARDS_TOP + row * (CARD_HEIGHT + CARDS_PADDING) + CARD_HEIGHT) * h // TOTAL_HEIGHT,
            ))
            colors = card.getcolors(maxcolors=256)
            if colors and len(colors) > 1:
                characters += 1
            i += 1
    return characters
