import os
import sys
import time

import pyautogui
import python_imagesearch.imagesearch

import controller
import fight
import maze
import review


def move_mouse_to_safe(pictures_dir, safe_img):
    left, top, right, bottom = controller.window_region()
    safe_img_path = os.path.join(pictures_dir, safe_img)
    safe_pos = python_imagesearch.imagesearch.imagesearcharea(safe_img_path, left, top, right, bottom)
    if safe_pos[0] != -1:
        from PIL import Image
        safe_img_obj = Image.open(safe_img_path)
        safe_w, safe_h = safe_img_obj.size
        safe_center_x = safe_pos[0] + left + safe_w // 2
        safe_center_y = safe_pos[1] + top + safe_h // 2
        pyautogui.moveTo(safe_center_x, safe_center_y, duration=0.05)
        time.sleep(0.1)
    else:
        print("Warning: safe spot image not found, mouse will not be moved.")


def find_and_click_in_window(img_path: str, retries: int = 5, delay: float = 0.25, safe_img_path: str = None) -> None:
    left, top, right, bottom = controller.window_region()
    for _ in range(retries):
        pos = python_imagesearch.imagesearch.imagesearcharea(img_path, left, top, right, bottom)
        if pos[0] != -1:
            print(f"Found {img_path} at {pos}")
            # Click the center of the found image
            from PIL import Image
            img = Image.open(img_path)
            w, h = img.size
            center_x = pos[0] + left + w // 2
            center_y = pos[1] + top + h // 2
            time.sleep(0.05)
            pyautogui.moveTo(center_x, center_y, duration=0.05)
            time.sleep(0.05)
            pyautogui.click(center_x, center_y)
            time.sleep(delay)
            # Move mouse to safe spot if provided
            if safe_img_path:
                safe_pos = python_imagesearch.imagesearch.imagesearcharea(safe_img_path, left, top, right, bottom)
                if safe_pos[0] != -1:
                    safe_img = Image.open(safe_img_path)
                    safe_w, safe_h = safe_img.size
                    safe_center_x = safe_pos[0] + left + safe_w // 2
                    safe_center_y = safe_pos[1] + top + safe_h // 2
                    pyautogui.moveTo(safe_center_x, safe_center_y, duration=0.05)
            return
        time.sleep(delay)
    raise RuntimeError(f"Image not found in window region: {img_path}")


def save_via_options(pictures_dir: str,
                     options_img: str = "options.png",
                     disk_img: str = "disk.png",
                     save_img: str = "save.png",
                     safe_img: str = "safe.png") -> None:
    # window.activate()  # REMOVE THIS LINE
    time.sleep(0.1)
    find_and_click_in_window(os.path.join(pictures_dir, options_img), safe_img_path=os.path.join(pictures_dir, safe_img))
    time.sleep(0.1)
    find_and_click_in_window(os.path.join(pictures_dir, disk_img), safe_img_path=os.path.join(pictures_dir, safe_img))
    time.sleep(0.1)
    find_and_click_in_window(os.path.join(pictures_dir, save_img), safe_img_path=os.path.join(pictures_dir, safe_img))


def wait_for_images(pictures_dir, image_names, timeout=5):
    start_time = time.time()
    left, top, right, bottom = controller.window_region()
    while True:
        for img_name in image_names:
            pos = python_imagesearch.imagesearch.imagesearcharea(os.path.join(pictures_dir, img_name), left, top, right, bottom)
            if pos[0] != -1:
                return img_name, pos
        if time.time() - start_time > timeout:
            return None, (-1, -1)
        time.sleep(0.05)


def handle_game_over(pictures_dir, safe_img):
    left, top, right, bottom = controller.window_region()
    while True:
        game_over_pos = python_imagesearch.imagesearch.imagesearcharea(os.path.join(pictures_dir, "gameover.png"), left, top, right, bottom)
        if game_over_pos[0] == -1:
            break
        find_and_click_in_window(os.path.join(pictures_dir, "gameover.png"), safe_img_path=os.path.join(pictures_dir, safe_img))
        time.sleep(0.1)
    find_and_click_in_window(os.path.join(pictures_dir, "resume.png"), safe_img_path=os.path.join(pictures_dir, safe_img))
    time.sleep(0.1)


def handle_rip_or_poisoned(pictures_dir, options_img, disk_img, safe_img):
    find_and_click_in_window(os.path.join(pictures_dir, options_img), safe_img_path=os.path.join(pictures_dir, safe_img))
    time.sleep(0.2)
    find_and_click_in_window(os.path.join(pictures_dir, disk_img), safe_img_path=os.path.join(pictures_dir, safe_img))
    time.sleep(0.1)
    find_and_click_in_window(os.path.join(pictures_dir, "mainmenu.png"), safe_img_path=os.path.join(pictures_dir, safe_img))
    time.sleep(0.2)
    find_and_click_in_window(os.path.join(pictures_dir, "resume.png"), safe_img_path=os.path.join(pictures_dir, safe_img))
    time.sleep(0.2)


def wait_for_monsters(pictures_dir, timeout=10):
    start_time = time.time()
    left, top, right, bottom = controller.window_region()
    while True:
        monsters_pos = python_imagesearch.imagesearch.imagesearcharea(os.path.join(pictures_dir, "monsters.png"), left, top, right, bottom)
        if monsters_pos[0] != -1:
            return True
        if time.time() - start_time > timeout:
            return False
        time.sleep(0.1)


def wait_for_options_menu(pictures_dir, options_img, safe_img, timeout=300):
    start_time = time.time()
    left, top, right, bottom = controller.window_region()
    while True:
        options_pos = python_imagesearch.imagesearch.imagesearcharea(os.path.join(pictures_dir, options_img), left, top, right, bottom)
        if options_pos[0] != -1:
            print("Options menu detected, continuing to next outer iteration.")
            return True
        game_over_pos = python_imagesearch.imagesearch.imagesearcharea(os.path.join(pictures_dir, "gameover.png"), left, top, right, bottom)
        if game_over_pos[0] != -1:
            print("Game over image found, exiting...")
            return False
        if time.time() - start_time > timeout:
            print("Timeout waiting for options menu after encounter.")
            return False
        time.sleep(0.1)


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

    win_title = controller.find_dosbox_window()
    print(f"Found window: {win_title} at {controller.window_region()}")

    # Do NOT call win.activate() or use win as an object
    time.sleep(0.2)
    # Move mouse to safe spot before starting automation
    move_mouse_to_safe(pictures_dir, safe_img)

    fails = 0
    successes = 0

    print("Resting until enemy appears...")
    try:
        for outer in range(10000):  # Outer loop, adjust as needed
            """
            await options
            await encounter

            options:
              while ...
                check options
                await sleep(0)

            also, caching layer for screenshots

            also, can we cancel the other coroutine when first started?
            create_task(save() + review() + rest())
            create_task(process_encounter())

            wait_first
            cancel others
            we can even not cancel then, just run in loop, but that requires strict filters
            we can cancel them manually also

            also,
            get_screenshot must buffer all different screenshots and provide them
            to all waiting couroutines, and if nobody is waiting, wait.
            how to ensure all waits will be there at the same time?
            we need to make getting screenshot most low priority task
            once everything is waiting for screenshot, we can take it
            kinda barrier

            also, make if click does not pass, it would automatically repeated
            """

            for attempt in range(3):
                # Open options menu and click rest
                try:
                    find_and_click_in_window(os.path.join(pictures_dir, options_img), safe_img_path=os.path.join(pictures_dir, safe_img))
                except Exception as e:
                    print(f"Open options and click rest failed: {e}; falling back to Ctrl+S")

                # Wait for either encounter or rest to appear, click rest if found
                wait_timeout = 5  # seconds
                start_time = time.time()
                while True:
                    left, top, right, bottom = controller.window_region()
                    encounter_pos = python_imagesearch.imagesearch.imagesearcharea(os.path.join(pictures_dir, encounter_img), left, top, right, bottom)
                    rest_pos = python_imagesearch.imagesearch.imagesearcharea(os.path.join(pictures_dir, rest_img), left, top, right, bottom)
                    options_pos = python_imagesearch.imagesearch.imagesearcharea(os.path.join(pictures_dir, options_img), left, top, right, bottom)
                    if encounter_pos[0] != -1:
                        pos = encounter_pos
                        break
                    if rest_pos[0] != -1:
                        # Click rest.png if found
                        find_and_click_in_window(os.path.join(pictures_dir, rest_img), safe_img_path=os.path.join(pictures_dir, safe_img))
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

                # Wait for either encounter or options
                wait_timeout = 5  # seconds
                start_time = time.time()
                while True:
                    left, top, right, bottom = controller.window_region()
                    encounter_pos = python_imagesearch.imagesearch.imagesearcharea(os.path.join(pictures_dir, encounter_img), left, top, right, bottom)
                    options_pos = python_imagesearch.imagesearch.imagesearcharea(os.path.join(pictures_dir, options_img), left, top, right, bottom)
                    if encounter_pos[0] != -1:
                        pos = encounter_pos
                        break
                    if options_pos[0] != -1:
                        pos = options_pos
                        break
                    if time.time() - start_time > wait_timeout:
                        print("Timeout waiting for encounter or options to appear.")
                        pos = (-1, -1)
                        break
                    time.sleep(0.05)

                # Check for encounter
                left, top, right, bottom = controller.window_region()
                encounter_pos = python_imagesearch.imagesearch.imagesearcharea(os.path.join(pictures_dir, encounter_img), left, top, right, bottom)
                monsters_pos = python_imagesearch.imagesearch.imagesearcharea(os.path.join(pictures_dir, "monsters.png"), left, top, right, bottom)
                if encounter_pos[0] != -1 or monsters_pos[0] != -1:
                    print("Waiting for monsters.png to appear...")
                    if not wait_for_monsters(pictures_dir, timeout=10):
                        print("Timeout waiting for monsters.png after encounter.")
                        break

                    fight.fight()

                    # Wait for options menu to reappear for up to 300s, then continue outer loop
                    print("Waiting for options menu to reappear (up to 300s)...")
                    wait_for_options_menu(pictures_dir, options_img, safe_img, timeout=300)
                    successes += 1
                    print(f"Successes: {successes}, Fails: {fails}, Success rate: {successes / (successes + fails) * 100:.2f}%")
                    break  # Break inner loop, continue outer
                time.sleep(0.1)
            else:
                print("Max rest attempts reached without finding an encounter.")

            # FIXME activate window does not work here.
            left, top, right, bottom = controller.window_region()
            poisoned_pos = python_imagesearch.imagesearch.imagesearcharea(os.path.join(pictures_dir, "poisoned.png"), left, top, right, bottom)
            rip_pos = python_imagesearch.imagesearch.imagesearcharea(os.path.join(pictures_dir, "rip.png"), left, top, right, bottom)
            if rip_pos[0] != -1 or poisoned_pos[0] != -1:
                print("RIP or poisoned detected, going to main menu and resuming...")
                try:
                    handle_rip_or_poisoned(pictures_dir, options_img, disk_img, safe_img)
                    fails += 1
                    print(f"Successes: {successes}, Fails: {fails}, Success rate: {successes / (successes + fails) * 100:.2f}%")
                except Exception as e:
                    print(f"Error handling RIP or poisoned: {e}")
                continue  # Continue main outer loop

            game_over_pos = python_imagesearch.imagesearch.imagesearcharea(os.path.join(pictures_dir, "gameover.png"), left, top, right, bottom)
            if game_over_pos[0] != -1:
                print("Game over image found, handling game over...")
                handle_game_over(pictures_dir, safe_img)
                fails += 1
                print(f"Successes: {successes}, Fails: {fails}, Success rate: {successes / (successes + fails) * 100:.2f}%")
                continue  # Continue main outer loop

            # Save after each attempt
            try:
                save_via_options(pictures_dir, options_img, disk_img, save_img, safe_img)
            except Exception as e:
                print(f"Save via images failed: {e}; falling back to Ctrl+S")

            # Open options and click review
            try:
                for i in range(maze.get_number_of_characters(pictures_dir=pictures_dir)):
                    # Open options and click review, then run review.review
                    find_and_click_in_window(os.path.join(pictures_dir, options_img), safe_img_path=os.path.join(pictures_dir, safe_img))
                    time.sleep(0.1)
                    find_and_click_in_window(os.path.join(pictures_dir, "review.png"), safe_img_path=os.path.join(pictures_dir, safe_img))
                    time.sleep(0.2)
                    review.review(character_index=i, pictures_dir=pictures_dir)
            except Exception as e:
                print(f"Open options and click review failed: {e}; falling back to Ctrl+S")

    except Exception as e:
        print(f"Error during rest/save loop: {e}")
        sys.exit(1)

    print("Done.")


if __name__ == "__main__":
    main()
