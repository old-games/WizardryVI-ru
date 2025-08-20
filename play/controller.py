import os
import time

import pygetwindow
import python_imagesearch.imagesearch
import pyautogui
from PIL import Image


def find_dosbox_window(title_prefix: str = "DOSBox-X"):
    all_titles = pygetwindow.getAllTitles()
    matches = [t for t in all_titles if t and title_prefix in t]
    if not matches:
        raise RuntimeError(f'No window with title containing "{title_prefix}" found')
    return matches[0]  # Return the window title string


def window_region() -> tuple[int, int, int, int]:
    title = find_dosbox_window()
    x, y, w, h = pygetwindow.getWindowGeometry(title)
    return x, y, x + w, y + h


def find_image(img_path, precision=0.95):
    left, top, right, bottom = window_region()
    pos = python_imagesearch.imagesearch.imagesearcharea(img_path, left, top, right, bottom, precision=precision)
    if pos[0] == -1:
        return (-1, -1)
    else:
        return (pos[0] + left, pos[1] + top)


def click_image(img_path, precision=0.95, move_to_safe=True, pictures_dir="pictures", safe_img="safe.png"):
    pos = find_image(img_path, precision=precision)
    if pos[0] == -1:
        return False
    img = Image.open(img_path)
    w, h = img.size
    center_x = pos[0] + w // 2
    center_y = pos[1] + h // 2
    pyautogui.moveTo(center_x, center_y, duration=0.05)
    time.sleep(0.05)
    pyautogui.click(center_x, center_y)
    time.sleep(0.1)
    if move_to_safe:
        move_mouse_to_safe(pictures_dir, safe_img, precision=precision)
    return True


def move_mouse_to_safe(pictures_dir, safe_img="safe.png", precision=0.95):
    safe_path = os.path.join(pictures_dir, safe_img)
    pos = find_image(safe_path, precision=precision)
    if pos[0] != -1:
        img = Image.open(safe_path)
        w, h = img.size
        center_x = pos[0] + w // 2
        center_y = pos[1] + h // 2
        pyautogui.moveTo(center_x, center_y, duration=0.05)


def wait_for_image(img_path, timeout=10, precision=0.95):
    start = time.time()
    while time.time() - start < timeout:
        pos = find_image(img_path, precision=precision)
        if pos[0] != -1:
            return pos
        time.sleep(0.1)
    return (-1, -1)
