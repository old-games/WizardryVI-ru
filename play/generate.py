import collections
import itertools
import os
import time

import cv2
import numpy
import PIL.Image
import pyautogui

import controller
import definition


name = "test"
race = definition.Race.LIZARDMAN
sex_path = "pictures/malewithpartoffemale.png"
pictures_dir = "pictures"

points = collections.Counter()

required_points = 100

bonus_img = PIL.Image.open("pictures/bonus.png")
bonus_width = bonus_img.size[0] // 5 * 3
bonus_height = bonus_img.size[1]
start_time = time.monotonic()

races_paths = {
    definition.Race.HUMAN: "pictures/human.png",
    definition.Race.LIZARDMAN: "pictures/lizardman.png",
    definition.Race.RAWULF: "pictures/rawulf.png",
    definition.Race.FELPURR: "pictures/felpurr.png",
}
race_path = races_paths[race]

for _ in itertools.count():
    clicked = controller.click_image("pictures/createpc.png")
    time.sleep(0.1)
    if not clicked or controller.find_image("pictures/createpc.png")[0] != -1:
        continue

    pyautogui.write(f"{name}\n")
    time.sleep(0.1)

    if not controller.click_image(race_path):
        break
    time.sleep(0.1)
    if not controller.click_image("pictures/safegen.png"):
        break
    time.sleep(0.1)
    if not controller.click_image(sex_path):
        break
    time.sleep(0.1)

    left, top, right, bottom = controller.window_region()
    bonus_pos = controller.find_image("pictures/bonus.png")
    if bonus_pos[0] == -1:
        break
    bonus_left = bonus_pos[0] + bonus_img.size[0]
    bonus_top = bonus_pos[1]
    bonus_points = pyautogui.screenshot(region=(bonus_left, bonus_top, bonus_width, bonus_height))

    bonus_points_number = ""
    col_width = bonus_width // 3
    for i in range(3):
        x1 = i * col_width
        x2 = x1 + col_width
        digit_img = bonus_points.crop((x1, 0, x2, bonus_height))

        # Pad digit_img with 10% space on each side
        pad_w = int(0.1 * digit_img.width)
        pad_h = int(0.1 * digit_img.height)
        new_w = digit_img.width + 2 * pad_w
        new_h = digit_img.height + 2 * pad_h
        digit_img_padded = PIL.Image.new("RGB", (new_w, new_h), (0, 0, 0))
        digit_img_padded.paste(digit_img, (pad_w, pad_h))
        digit_img = digit_img_padded

        # Check if column is not empty (not all white)
        if digit_img.getbbox() is not None:
            best_digit = None
            best_score = None
            digit_img_cv = numpy.array(digit_img.convert("L"))
            for d in range(10):
                digit_name = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"][d]
                digit_path = os.path.join(pictures_dir, "digit", f"{digit_name}.png")
                if not os.path.exists(digit_path):
                    continue
                template = PIL.Image.open(digit_path).convert("L")
                template_cv = numpy.array(template)
                img_cv = numpy.array(digit_img.convert("L"))

                # Use normalized cross-correlation for location
                res = cv2.matchTemplate(img_cv, template_cv, cv2.TM_CCOEFF_NORMED)
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
                top_left = max_loc
                score = max_val

                # print(f"Score for {d} ({digit_name}): {score}")
                if best_score is None or score > best_score:
                    best_score = score
                    best_digit = str(d)
            if best_digit is not None:
                bonus_points_number += best_digit

    bonus_points_number = int(bonus_points_number)
    points[bonus_points_number] += 1
    print(bonus_points_number)
    combined = points.copy()
    for x, y in definition.POINTS_PROBABILITIES.get(race, []):
        combined[x] += y
    print(sorted(combined.most_common(), key=lambda x: (-x[1], x[0])))
    print(sum(points.values()), f"{time.monotonic() - start_time:.2f} s", f"{(sum(points.values())-1)/(time.monotonic() - start_time)*3600:.2f} rerolls/hour")

    if bonus_points_number >= required_points:
        break

    if not controller.click_image("pictures/safegen.png"):
        break
    time.sleep(0.1)
    if not controller.click_image("pictures/fighter.png"):
        break
    time.sleep(0.1)

    while controller.find_image("pictures/bonus0.png", precision=0.98)[0] == -1:
        pyautogui.press('right')
        pyautogui.press('down')
        time.sleep(0.1)

    pyautogui.write('\n')
    time.sleep(0.1)

    pyautogui.write('\n') # Karma.
    time.sleep(0.1)

    pyautogui.write('\n') # Avatar.
    time.sleep(0.1)

    while controller.find_image("pictures/skillpoints0.png", precision=0.98)[0] == -1:
        pyautogui.press('right')
        pyautogui.press('down')
        time.sleep(0.1)

    pyautogui.write('\n')
    time.sleep(0.1)

    if not controller.click_image("pictures/saveno.png"):
        break
    time.sleep(0.1)
