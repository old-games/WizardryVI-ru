import os
import sys
import time
from typing import Optional, Tuple

# Requires: python-imagesearch, pygetwindow, pyautogui
# pip install python-imagesearch pygetwindow pyautogui

from python_imagesearch.imagesearch import imagesearcharea
import pygetwindow as gw
import pyautogui

import fight


def find_dosbox_window(title_prefix: str = "DOSBox-X"):
    all_titles = gw.getAllTitles()
    matches = [t for t in all_titles if t and title_prefix in t]
    if not matches:
        raise RuntimeError(f'No window with title containing "{title_prefix}" found')
    print(f"Found DOSBox-X window: {matches[0]}")
    return matches[0]  # Return the window title string


def window_region(window=None) -> Tuple[int, int, int, int]:
    import pyautogui
    width, height = pyautogui.size()
    return 0, 0, width, height


def find_and_click_in_window(window, img_path: str, retries: int = 5, delay: float = 0.25, safe_img_path: str = None) -> None:
    left, top, right, bottom = window_region(window)
    for _ in range(retries):
        print(f"Searching for {img_path} in region {left, top, right, bottom}")
        pos = imagesearcharea(img_path, left, top, right, bottom)
        if pos[0] != -1:
            print(f"Found {img_path} at {pos}")
            # Click the center of the found image
            from PIL import Image
            img = Image.open(img_path)
            w, h = img.size
            center_x = pos[0] + w // 2
            center_y = pos[1] + h // 2
            print(f"Clicking at center: {center_x}, {center_y}")
            time.sleep(0.05)
            pyautogui.moveTo(center_x, center_y, duration=0.05)
            time.sleep(0.05)
            pyautogui.click(center_x, center_y)
            time.sleep(delay)
            # Move mouse to safe spot if provided
            if safe_img_path:
                safe_pos = imagesearcharea(safe_img_path, left, top, right, bottom)
                if safe_pos[0] != -1:
                    safe_img = Image.open(safe_img_path)
                    safe_w, safe_h = safe_img.size
                    safe_center_x = safe_pos[0] + safe_w // 2
                    safe_center_y = safe_pos[1] + safe_h // 2
                    pyautogui.moveTo(safe_center_x, safe_center_y, duration=0.05)
            if img_path.endswith("options.png"):
                pos = imagesearcharea(img_path, left, top, right, bottom)
                if pos[0] == -1:
                    print(f"Successfully clicked {img_path} at {pos}")
                else:
                    print(f"Click did not register, found again at {pos}")
                    # Some bug
                    continue
            return
        time.sleep(delay)
    raise RuntimeError(f"Image not found in window region: {img_path}")


def save_via_options(window, pictures_dir: str,
                     options_img: str = "options.png",
                     disk_img: str = "disk.png",
                     save_img: str = "save.png",
                     safe_img: str = "safe.png") -> None:
    # window.activate()  # REMOVE THIS LINE
    time.sleep(0.1)
    find_and_click_in_window(window, os.path.join(pictures_dir, options_img), safe_img_path=os.path.join(pictures_dir, safe_img))
    time.sleep(0.1)
    find_and_click_in_window(window, os.path.join(pictures_dir, disk_img), safe_img_path=os.path.join(pictures_dir, safe_img))
    time.sleep(0.1)
    find_and_click_in_window(window, os.path.join(pictures_dir, save_img), safe_img_path=os.path.join(pictures_dir, safe_img))


def main():
    if sys.argv[1:] == ["--groups"]:
        # If called with --groups, count groups
        pictures_dir = os.path.join(os.path.dirname(__file__), "pictures")
        num_groups = fight.get_number_of_groups(pictures_dir=pictures_dir)
        print(f"Number of groups: {num_groups}")
        return
    pictures_dir = os.path.join(os.path.dirname(__file__), "pictures")
    options_img = "options.png"
    rest_img = "rest.png"
    disk_img = "disk.png"
    save_img = "save.png"
    encounter_img = "encounter.png"
    safe_img = "safe.png"

    pyautogui.MINIMUM_DURATION = 0.01
    pyautogui.MINIMUM_SLEEP = 0.003
    pyautogui.DARWIN_CATCH_UP_TIME = 0.001
    pyautogui.PAUSE = 0

    win_title = find_dosbox_window("DOSBox-X")
    print(f"Found window: {win_title} at {window_region()}")
    print(gw.getWindowGeometry(win_title)) # Code is adjusted to (1280.0, 828.0)

    # Do NOT call win.activate() or use win as an object
    time.sleep(0.2)
    # Move mouse to safe spot before starting automation
    safe_img_path = os.path.join(pictures_dir, safe_img)
    left, top, right, bottom = window_region()
    safe_pos = imagesearcharea(safe_img_path, left, top, right, bottom)
    if safe_pos[0] != -1:
        from PIL import Image
        safe_img_obj = Image.open(safe_img_path)
        safe_w, safe_h = safe_img_obj.size
        safe_center_x = safe_pos[0] + safe_w // 2
        safe_center_y = safe_pos[1] + safe_h // 2
        pyautogui.moveTo(safe_center_x, safe_center_y, duration=0.05)
        time.sleep(0.1)
    else:
        print("Warning: safe spot image not found, mouse will")

    print("Resting until enemy appears...")
    try:
        for outer in range(1000):  # Outer loop, adjust as needed
            rip_pos = imagesearcharea(os.path.join(pictures_dir, "rip.png"), left, top, right, bottom)
            if rip_pos[0] != -1:
                print("RIP image found, going to main menu and resuming...")
                # Go to options
                find_and_click_in_window(None, os.path.join(pictures_dir, options_img), safe_img_path=os.path.join(pictures_dir, safe_img))
                time.sleep(0.1)
                # Go to disk
                find_and_click_in_window(None, os.path.join(pictures_dir, disk_img), safe_img_path=os.path.join(pictures_dir, safe_img))
                time.sleep(0.1)
                # Click mainmenu.png
                find_and_click_in_window(None, os.path.join(pictures_dir, "mainmenu.png"), safe_img_path=os.path.join(pictures_dir, safe_img))
                time.sleep(0.2)
                # Click resume.png
                find_and_click_in_window(None, os.path.join(pictures_dir, "resume.png"), safe_img_path=os.path.join(pictures_dir, safe_img))
                time.sleep(0.2)
                continue  # Continue main outer loop
            game_over_pos = imagesearcharea(os.path.join(pictures_dir, "gameover.png"), left, top, right, bottom)
            if game_over_pos[0] != -1:
                print("Game over image found, clicking gameover until it disappears, then clicking resume, then continuing main loop...")
                # Click on gameover.png repeatedly until it disappears
                while True:
                    game_over_pos = imagesearcharea(os.path.join(pictures_dir, "gameover.png"), left, top, right, bottom)
                    if game_over_pos[0] == -1:
                        break
                    find_and_click_in_window(None, os.path.join(pictures_dir, "gameover.png"), safe_img_path=os.path.join(pictures_dir, safe_img))
                    time.sleep(0.1)
                # Click on resume.png
                find_and_click_in_window(None, os.path.join(pictures_dir, "resume.png"), safe_img_path=os.path.join(pictures_dir, safe_img))
                time.sleep(0.1)
                continue  # Continue main outer loop
            # Save before each rest attempt
            try:
                save_via_options(None, pictures_dir, options_img, disk_img, save_img, safe_img)
            except Exception as e:
                print(f"Save via images failed: {e}; falling back to Ctrl+S")
            for attempt in range(5):
                # Open options menu and click rest
                find_and_click_in_window(None, os.path.join(pictures_dir, options_img), safe_img_path=os.path.join(pictures_dir, safe_img))

                # Wait for either encounter or rest to appear
                wait_timeout = 5  # seconds
                start_time = time.time()
                encounter_pos = (-1, -1)
                options_pos = (-1, -1)
                while True:
                    left, top, right, bottom = window_region()
                    encounter_pos = imagesearcharea(os.path.join(pictures_dir, encounter_img), left, top, right, bottom)
                    rest_pos = imagesearcharea(os.path.join(pictures_dir, rest_img), left, top, right, bottom)
                    options_pos = imagesearcharea(os.path.join(pictures_dir, options_img), left, top, right, bottom)
                    if encounter_pos[0] != -1:
                        pos = encounter_pos
                        break
                    if rest_pos[0] != -1:
                        # Click rest.png if found
                        find_and_click_in_window(None, os.path.join(pictures_dir, rest_img), safe_img_path=os.path.join(pictures_dir, safe_img))
                        time.sleep(0.05)
                        break
                    if options_pos[0] != -1:
                        pos = options_pos
                        break
                    if time.time() - start_time > wait_timeout:
                        print("Timeout waiting for encounter or rest to appear.")
                        pos = (-1, -1)
                        break
                    time.sleep(0.05)

                if encounter_pos[0] == -1:
                    # Wait for either encounter or options to appear
                    wait_timeout = 5  # seconds
                    start_time = time.time()
                    while True:
                        left, top, right, bottom = window_region()
                        encounter_pos = imagesearcharea(os.path.join(pictures_dir, encounter_img), left, top, right, bottom)
                        options_pos = imagesearcharea(os.path.join(pictures_dir, options_img), left, top, right, bottom)
                        if encounter_pos[0] != -1 or options_pos[0] != -1:
                            pos = encounter_pos if encounter_pos[0] != -1 else options_pos
                            break
                        if time.time() - start_time > wait_timeout:
                            print("Timeout waiting for encounter or options to appear.")
                            pos = (-1, -1)
                            break
                        time.sleep(0.05)

                # Check for encounter
                left, top, right, bottom = window_region()
                pos = imagesearcharea(os.path.join(pictures_dir, encounter_img), left, top, right, bottom)
                if pos[0] != -1:
                    print(f"Encounter found at {pos} after {attempt+1} rest(s)")
                    # Wait for monsters.png to appear (fight window)
                    print("Waiting for monsters.png to appear...")
                    wait_timeout = 10  # seconds
                    start_time = time.time()
                    while True:
                        left, top, right, bottom = window_region()
                        monsters_pos = imagesearcharea(os.path.join(pictures_dir, "monsters.png"), left, top, right, bottom)
                        if monsters_pos[0] != -1:
                            print("monsters.png detected.")
                            break
                        if time.time() - start_time > wait_timeout:
                            print("Timeout waiting for monsters.png after encounter.")
                            break
                        time.sleep(0.1)

                    # Check number of groups
                    num_groups = fight.get_number_of_groups(pictures_dir=pictures_dir)
                    print(f"Number of groups: {num_groups}")
                    if num_groups == 1:
                        fight.fight_one_group()
                    else:
                        fight.fight_many_groups()
                    # Wait for options menu to reappear for up to 300s, then continue outer loop
                    print("Waiting for options menu to reappear (up to 300s)...")
                    wait_timeout = 300
                    start_time = time.time()
                    while True:
                        left, top, right, bottom = window_region()
                        options_pos = imagesearcharea(os.path.join(pictures_dir, options_img), left, top, right, bottom)
                        if options_pos[0] != -1:
                            print("Options menu detected, continuing to next outer iteration.")
                            break
                        game_over_pos = imagesearcharea(os.path.join(pictures_dir, "gameover.png"), left, top, right, bottom)
                        if game_over_pos[0] != -1:
                            print("Game over image found, exiting...")
                            break
                        if time.time() - start_time > wait_timeout:
                            print("Timeout waiting for options menu after encounter.")
                            break
                        time.sleep(0.1)
                    break  # Break inner loop, continue outer
                time.sleep(0.1)
            else:
                print("Max rest attempts reached without finding an encounter.")
    except Exception as e:
        print(f"Error during rest/save loop: {e}")
        sys.exit(1)

    print("Done.")


if __name__ == "__main__":
    main()
