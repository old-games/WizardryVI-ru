import pygetwindow
import python_imagesearch.imagesearch


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
