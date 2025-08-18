import os
import time

from python_imagesearch.imagesearch import imagesearcharea
from PIL import Image
import pyautogui

import controller


def click_image(img_path, precision=0.95, move_to_safe=True, pictures_dir="pictures", safe_img="safe.png"):
    pos = controller.find_image(img_path, precision=precision)
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
    pos = controller.find_image(safe_path, precision=precision)
    if pos[0] != -1:
        img = Image.open(safe_path)
        w, h = img.size
        center_x = pos[0] + w // 2
        center_y = pos[1] + h // 2
        pyautogui.moveTo(center_x, center_y, duration=0.05)


def wait_for_image(img_path, timeout=10, precision=0.95):
    start = time.time()
    while time.time() - start < timeout:
        pos = controller.find_image(img_path, precision=precision)
        if pos[0] != -1:
            return pos
        time.sleep(0.1)
    return (-1, -1)


def get_number_of_groups(pictures_dir="pictures", precision=0.95):
    monsters_path = os.path.join(pictures_dir, "monsters.png")
    groupleft_path = os.path.join(pictures_dir, "groupleft.png")

    monsters_pos = controller.find_image(monsters_path, precision=precision)
    if monsters_pos[0] == -1:
        print("monsters.png not found")
        return 0

    groupleft_pos = imagesearcharea(groupleft_path, 0, monsters_pos[1], *pyautogui.size(), precision=precision)
    if groupleft_pos[0] == -1:
        print("groupleft.png not found")
        return 0

    groupleft_pos = (groupleft_pos[0], groupleft_pos[1] + monsters_pos[1])
    groupleft_img = Image.open(groupleft_path)
    monsters_img = Image.open(monsters_path)

    scan_x = monsters_pos[0]
    scan_y = monsters_pos[1] + monsters_img.height
    scan_w = monsters_img.width
    scan_h = groupleft_pos[1] + groupleft_img.height - scan_y
    line_height = scan_h // 6

    screenshot = pyautogui.screenshot(region=(scan_x, scan_y, scan_w, scan_h))
    num_groups = 0
    for i in range(5):
        y1 = i * line_height
        y2 = y1 + line_height
        line_crop = screenshot.crop((0, y1, scan_w, y2))
        if not is_line_empty(line_crop):
            num_groups += 1
        else:
            break
    return num_groups


def is_line_empty(line_img):
    colors = line_img.getcolors(maxcolors=256)
    if not colors or len(colors) == 1:
        return True
    return False


def run_away(pictures_dir="pictures", precision=0.95):
    run_path = os.path.join(pictures_dir, "run.png")
    clicked = click_image(run_path, precision=precision, move_to_safe=True, pictures_dir=pictures_dir)
    if not clicked:
        print("run.png not found for run_away")


def fight_one_group(pictures_dir="pictures", precision=0.95):
    button_imgs = ["run.png", "startfighting.png", "bash.png", "fight.png"]
    text_imgs = ["rip.png", "gameover.png", "victory.png", "options.png"]
    safe_img = "safe.png"
    while True:
        # Find all available buttons and texts
        available_buttons = []
        for btn in button_imgs:
            if controller.find_image(os.path.join(pictures_dir, btn), precision=precision)[0] != -1:
                available_buttons.append(btn)
        available_texts = []
        for txt in text_imgs:
            if controller.find_image(os.path.join(pictures_dir, txt), precision=precision)[0] != -1:
                available_texts.append(txt)

        # Decision logic
        if "rip.png" in available_texts and "run.png" in available_buttons:
            run_away(pictures_dir, precision=precision)
            time.sleep(0.1)
            continue

        for end_img in ["gameover.png", "victory.png", "options.png"]:
            if end_img in available_texts:
                print(f"{end_img} detected, ending fight_one_group loop.")
                if end_img == "victory.png":
                    after_fight(pictures_dir, precision=precision)
                return

        for action_img in ["startfighting.png", "bash.png", "fight.png"]:
            if action_img in available_buttons:
                click_image(os.path.join(pictures_dir, action_img), precision=precision, move_to_safe=True, pictures_dir=pictures_dir, safe_img=safe_img)
                break

        time.sleep(0.1)


def fight_many_groups(pictures_dir="pictures", precision=0.95):
    button_imgs = ["run.png", "startfighting.png", "bash.png", "fight.png"]
    text_imgs = ["rip.png", "gameover.png", "victory.png", "options.png", "fightgroup.png"]
    safe_img = "safe.png"
    while True:
        # Find all available buttons and texts
        available_buttons = []
        for btn in button_imgs:
            if controller.find_image(os.path.join(pictures_dir, btn), precision=precision)[0] != -1:
                available_buttons.append(btn)
        available_texts = []
        for txt in text_imgs:
            if controller.find_image(os.path.join(pictures_dir, txt), precision=precision)[0] != -1:
                available_texts.append(txt)

        # Decision logic
        if "rip.png" in available_texts and "run.png" in available_buttons:
            run_away(pictures_dir, precision=precision)
            time.sleep(0.1)
            continue

        for end_img in ["gameover.png", "victory.png", "options.png"]:
            if end_img in available_texts:
                print(f"{end_img} detected, ending fight_many_groups loop.")
                if end_img == "victory.png":
                    after_fight(pictures_dir, precision=precision)
                return

        if "fightgroup.png" in available_texts:
            print("fightgroup.png detected, clicking first group...")
            monsters_path = os.path.join(pictures_dir, "monsters.png")
            groupleft_path = os.path.join(pictures_dir, "groupleft.png")
            monsters_pos = controller.find_image(monsters_path)
            groupleft_pos = imagesearcharea(groupleft_path, 0, monsters_pos[1], *pyautogui.size())
            groupleft_img = Image.open(groupleft_path)
            scan_x = groupleft_pos[0] + groupleft_img.width
            scan_y = monsters_pos[1] + Image.open(monsters_path).height
            click_x = scan_x + 40
            click_y = scan_y + 10
            pyautogui.moveTo(click_x, click_y, duration=0.05)
            time.sleep(0.05)
            pyautogui.click(click_x, click_y)
            time.sleep(0.1)
            move_mouse_to_safe(pictures_dir, safe_img, precision=precision)

        for action_img in ["startfighting.png", "bash.png", "fight.png"]:
            if action_img in available_buttons:
                click_image(os.path.join(pictures_dir, action_img), precision=precision, move_to_safe=True, pictures_dir=pictures_dir, safe_img=safe_img)
                break

        time.sleep(0.1)


def after_fight(pictures_dir="pictures", precision=0.95):
    safe_img = "safe.png"
    while True:
        options_path = os.path.join(pictures_dir, "options.png")
        if controller.find_image(options_path, precision=precision)[0] != -1:
            print("options.png detected, exiting after_fight loop.")
            break

        takenone_path = os.path.join(pictures_dir, "takenone.png")
        if click_image(takenone_path, precision=precision, move_to_safe=True, pictures_dir=pictures_dir, safe_img=safe_img):
            break

        time.sleep(0.2)
