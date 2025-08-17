import os
import time

from python_imagesearch.imagesearch import imagesearcharea
from PIL import Image
import pyautogui


def get_number_of_groups(pictures_dir="pictures"):
    # Find the "monsters.png" header
    screen_w, screen_h = pyautogui.size()
    monsters_path = os.path.join(pictures_dir, "monsters.png")
    groupleft_path = os.path.join(pictures_dir, "groupleft.png")

    # Find monsters.png (header)
    monsters_pos = imagesearcharea(monsters_path, 0, 0, screen_w, screen_h)
    if monsters_pos[0] == -1:
        print("monsters.png not found")
        return 0

    # Find groupleft.png (left marker for group lines)
    groupleft_pos = imagesearcharea(groupleft_path, 0, monsters_pos[1], screen_w, screen_h)
    if groupleft_pos[0] == -1:
        print("groupleft.png not found")
        return 0

    groupleft_pos = (groupleft_pos[0] + 0, groupleft_pos[1] + monsters_pos[1])

    # Get height of groupleft.png (line height)
    groupleft_img = Image.open(groupleft_path)
    monsters_img = Image.open(monsters_path)

    bottom = groupleft_pos[1] + groupleft_img.height

    # Define scan area: under monsters.png, to the right of groupleft.png, for N lines
    scan_x = monsters_pos[0]
    scan_y = monsters_pos[1] + monsters_img.height
    scan_w = monsters_img.width
    scan_h = groupleft_pos[1] + groupleft_img.height - scan_y
    line_height = scan_h // 6

    print(f"Bottom of groupleft: {bottom}")
    print(f"Scan area: x={scan_x}, y={scan_y}, w={scan_w}, h={scan_h}")
    print(f"Line height: {line_height}")

    # Take screenshot of the area under the header
    screenshot = pyautogui.screenshot(region=(scan_x, scan_y, scan_w, scan_h))

    # Count non-empty lines by checking for non-black pixels in each line area
    num_groups = 0
    for i in range(5):  # Assume max 10 groups
        y1 = i * line_height
        y2 = y1 + line_height
        line_crop = screenshot.crop((0, y1, scan_w, y2))
        # Check if line is not all black (or all the same color)
        if not is_line_empty(line_crop):
            num_groups += 1
        else:
            break  # Stop at first empty line

    return num_groups


def is_line_empty(line_img):
    # Returns True if the line is all black or all the same color
    colors = line_img.getcolors(maxcolors=256)
    if not colors:
        return True
    if len(colors) == 1:
        return True
    # If more than one color, assume not empty
    return False


def run_away(pictures_dir="pictures", precision=0.95):
    run_path = os.path.join(pictures_dir, "run.png")
    screen_w, screen_h = pyautogui.size()
    run_pos = imagesearcharea(run_path, 0, 0, screen_w, screen_h, precision=precision)
    safe_img = "safe.png"
    img = Image.open(run_path)
    w, h = img.size
    center_x = run_pos[0] + w // 2
    center_y = run_pos[1] + h // 2
    print(f"RIP detected, clicking run.png at {center_x}, {center_y}")
    pyautogui.moveTo(center_x, center_y, duration=0.05)
    time.sleep(0.05)
    pyautogui.click(center_x, center_y)
    time.sleep(0.1)
    # Move mouse to safe spot after click
    safe_path = os.path.join(pictures_dir, safe_img)
    safe_pos = imagesearcharea(safe_path, 0, 0, screen_w, screen_h, precision=precision)
    if safe_pos[0] != -1:
        safe_img_obj = Image.open(safe_path)
        safe_w, safe_h = safe_img_obj.size
        safe_center_x = safe_pos[0] + safe_w // 2
        safe_center_y = safe_pos[1] + safe_h // 2
        pyautogui.moveTo(safe_center_x, safe_center_y, duration=0.05)


def fight_one_group(pictures_dir="pictures", precision=0.95):
    fight_imgs = [
        "bash.png",
        "startfighting.png",
        "fight.png",
    ]
    end_imgs = [
        "gameover.png",
        "victory.png",
        "options.png",
    ]
    safe_img = "safe.png"
    screen_w, screen_h = pyautogui.size()
    while True:
        # If rip.png is found, click run.png and continue
        rip_path = os.path.join(pictures_dir, "rip.png")
        rip_pos = imagesearcharea(rip_path, 0, 0, screen_w, screen_h, precision=precision)
        if rip_pos[0] != -1:
            run_path = os.path.join(pictures_dir, "run.png")
            run_pos = imagesearcharea(run_path, 0, 0, screen_w, screen_h, precision=precision)
            if run_pos[0] != -1:
                run_away(pictures_dir=pictures_dir, precision=precision)
                continue  # Skip the rest of the loop and check again
            else:
                print("RIP detected, but run.png not found.")

        # Check for end conditions
        for end_img in end_imgs:
            end_path = os.path.join(pictures_dir, end_img)
            pos = imagesearcharea(end_path, 0, 0, screen_w, screen_h, precision=precision)
            if pos[0] != -1:
                print(f"{end_img} detected, ending fight_one_group loop.")
                if end_img == "victory.png":
                    after_fight(precision=precision)
                break
        if pos[0] != -1:
            break

        # Check for fight actions and click if found
        for action_img in fight_imgs:
            action_path = os.path.join(pictures_dir, action_img)
            pos = imagesearcharea(action_path, 0, 0, screen_w, screen_h, precision=precision)
            if pos[0] != -1:
                img = Image.open(action_path)
                w, h = img.size
                center_x = pos[0] + w // 2
                center_y = pos[1] + h // 2
                print(f"Clicking {action_img} at {center_x}, {center_y}")
                pyautogui.moveTo(center_x, center_y, duration=0.05)
                time.sleep(0.05)
                pyautogui.click(center_x, center_y)
                time.sleep(0.1)
                # Move mouse to safe spot after click
                safe_path = os.path.join(pictures_dir, safe_img)
                safe_pos = imagesearcharea(safe_path, 0, 0, screen_w, screen_h, precision=precision)
                if safe_pos[0] != -1:
                    safe_img_obj = Image.open(safe_path)
                    safe_w, safe_h = safe_img_obj.size
                    safe_center_x = safe_pos[0] + safe_w // 2
                    safe_center_y = safe_pos[1] + safe_h // 2
                    pyautogui.moveTo(safe_center_x, safe_center_y, duration=0.05)
                break  # Only click one action per loop

        time.sleep(0.1)


def fight_many_groups(pictures_dir="pictures", precision=0.95):
    fight_imgs = [
        "bash.png",
        "startfighting.png",
        "fight.png",
    ]
    end_imgs = [
        "gameover.png",
        "victory.png",
        "options.png",
    ]
    safe_img = "safe.png"
    screen_w, screen_h = pyautogui.size()
    while True:
        # If rip.png is found, click run.png and continue
        rip_path = os.path.join(pictures_dir, "rip.png")
        rip_pos = imagesearcharea(rip_path, 0, 0, screen_w, screen_h, precision=precision)
        if rip_pos[0] != -1:
            run_path = os.path.join(pictures_dir, "run.png")
            run_pos = imagesearcharea(run_path, 0, 0, screen_w, screen_h, precision=precision)
            if run_pos[0] != -1:
                run_away(pictures_dir=pictures_dir, precision=precision)
                continue  # Skip the rest of the loop and check again
            else:
                print("RIP detected, but run.png not found.")

        # Check for end conditions
        for end_img in end_imgs:
            end_path = os.path.join(pictures_dir, end_img)
            pos = imagesearcharea(end_path, 0, 0, screen_w, screen_h, precision=precision)
            if pos[0] != -1:
                print(f"{end_img} detected, ending fight_many_groups loop.")
                if end_img == "victory.png":
                    after_fight(precision=precision)
                break
        if pos[0] != -1:
            break

        fightgroup_pos = imagesearcharea(os.path.join(pictures_dir, "fightgroup.png"), 0, 0, screen_w, screen_h, precision=precision)
        if fightgroup_pos[0] != -1:
            print("fightgroup.png detected, clicking first group...")
            # Calculate coordinates for first group (reuse logic from get_number_of_groups)
            monsters_path = os.path.join(pictures_dir, "monsters.png")
            groupleft_path = os.path.join(pictures_dir, "groupleft.png")
            monsters_pos = imagesearcharea(monsters_path, 0, 0, screen_w, screen_h)
            groupleft_pos = imagesearcharea(groupleft_path, 0, monsters_pos[1], screen_w, screen_h)
            groupleft_img = Image.open(groupleft_path)
            scan_x = groupleft_pos[0] + groupleft_img.width
            scan_y = monsters_pos[1] + Image.open(monsters_path).height
            # First group y is scan_y + 0 * line_height (so just scan_y)
            # We'll click near the left of the group area
            click_x = scan_x + 40  # 40 px to the right of marker, adjust as needed
            click_y = scan_y + 10  # 10 px below header, adjust as needed
            pyautogui.moveTo(click_x, click_y, duration=0.05)
            time.sleep(0.05)
            pyautogui.click(click_x, click_y)
            time.sleep(0.1)
            # Move mouse to safe spot after click
            safe_path = os.path.join(pictures_dir, safe_img)
            safe_pos = imagesearcharea(safe_path, 0, 0, screen_w, screen_h, precision=precision)
            if safe_pos[0] != -1:
                safe_img_obj = Image.open(safe_path)
                safe_w, safe_h = safe_img_obj.size
                safe_center_x = safe_pos[0] + safe_w // 2
                safe_center_y = safe_pos[1] + safe_h // 2
                pyautogui.moveTo(safe_center_x, safe_center_y, duration=0.05)

        # Check for fight actions and click if found
        for action_img in fight_imgs:
            action_path = os.path.join(pictures_dir, action_img)
            pos = imagesearcharea(action_path, 0, 0, screen_w, screen_h, precision=precision)
            if pos[0] != -1:
                img = Image.open(action_path)
                w, h = img.size
                center_x = pos[0] + w // 2
                center_y = pos[1] + h // 2
                print(f"Clicking {action_img} at {center_x}, {center_y}")
                pyautogui.moveTo(center_x, center_y, duration=0.05)
                time.sleep(0.05)
                pyautogui.click(center_x, center_y)
                time.sleep(0.05)
                # Move mouse to safe spot after click
                safe_path = os.path.join(pictures_dir, safe_img)
                safe_pos = imagesearcharea(safe_path, 0, 0, screen_w, screen_h, precision=precision)
                if safe_pos[0] != -1:
                    safe_img_obj = Image.open(safe_path)
                    safe_w, safe_h = safe_img_obj.size
                    safe_center_x = safe_pos[0] + safe_w // 2
                    safe_center_y = safe_pos[1] + safe_h // 2
                    pyautogui.moveTo(safe_center_x, safe_center_y, duration=0.05)
                break  # Only click one action per loop

        time.sleep(0.1)


def after_fight(pictures_dir="pictures", precision=0.95):
    safe_img = "safe.png"
    screen_w, screen_h = pyautogui.size()
    while True:
        # Wait for options.png to appear
        options_path = os.path.join(pictures_dir, "options.png")
        options_pos = imagesearcharea(options_path, 0, 0, screen_w, screen_h, precision=precision)
        if options_pos[0] != -1:
            print("options.png detected, exiting after_fight loop.")
            break

        # Check for takenone.png and click it if present
        takenone_path = os.path.join(pictures_dir, "takenone.png")
        takenone_pos = imagesearcharea(takenone_path, 0, 0, screen_w, screen_h, precision=precision)
        if takenone_pos[0] != -1:
            img = Image.open(takenone_path)
            w, h = img.size
            center_x = takenone_pos[0] + w // 2
            center_y = takenone_pos[1] + h // 2
            print(f"Clicking takenone.png at {center_x}, {center_y}")
            pyautogui.moveTo(center_x, center_y, duration=0.05)
            time.sleep(0.05)
            pyautogui.click(center_x, center_y)
            time.sleep(0.1)
            # Move mouse to safe spot after click
            safe_path = os.path.join(pictures_dir, safe_img)
            safe_pos = imagesearcharea(safe_path, 0, 0, screen_w, screen_h, precision=precision)
            if safe_pos[0] != -1:
                safe_img_obj = Image.open(safe_path)
                safe_w, safe_h = safe_img_obj.size
                safe_center_x = safe_pos[0] + safe_w // 2
                safe_center_y = safe_pos[1] + safe_h // 2
                pyautogui.moveTo(safe_center_x, safe_center_y, duration=0.05)
            break  # Exit after clicking takenone.png

        time.sleep(0.2)
