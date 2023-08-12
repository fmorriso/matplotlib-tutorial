import sys, ctypes
import inspect
import pyautogui
import tkinter as tk

# BAD from matplotlib import pyplot as plt
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from numpy import random


def get_python_version() -> str:
    return f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"


def scale_background(pct: float) -> tuple[int, int]:
    # find out the width and height of the device we are running on
    device_width, device_height = pyautogui.size()

    # scale width and height based on what percentage of device size user wants to use, rounded to
    # the nearest multiple of 100
    scaled_width: int = int((device_width * pct // 100) * 100)
    scaled_height: int = int((device_height * pct // 100) * 100)

    return scaled_width, scaled_height


def get_screen_dpi() -> float:
    """
    Calculates the dots per inch of the primary device on Microsoft Windows 10 or newer.
    :return: dots per inch (DPI)
    """
    root = tk.Tk()
    MM_TO_IN = 0.0393700787
    # Get a DC from the window's HWND
    dc = ctypes.windll.user32.GetDC(root.winfo_id())

    # The monitor phyical width
    # (returned in millimeters then converted to inches)
    mw = ctypes.windll.gdi32.GetDeviceCaps(dc, 4) * MM_TO_IN
    # The the monitor physical height
    mh = ctypes.windll.gdi32.GetDeviceCaps(dc, 6) * MM_TO_IN
    # Get the monitor horizontal resolution
    dw = ctypes.windll.gdi32.GetDeviceCaps(dc, 8)
    # Get the monitor vertical resolution
    dh = ctypes.windll.gdi32.GetDeviceCaps(dc, 10)
    # Destroy the window
    root.destroy()

    # calculate DPI for width and height
    dpi_w = dw / mw
    dpi_h = dh / mh
    # then take the larger of the two values
    return max(dpi_w, dpi_h)


# def scale_plot(fig):
def scale_plot():
    # get device width & height in pixels
    device_w, device_h = scale_background(0.85)
    # use device dots per inch to convert pixels to inches as required by MatPlotLib figsize
    dpi = get_screen_dpi()
    w = device_w / dpi
    h = device_h / dpi

    # make sure we don't accidentally create a small, blank Figure that hides behind the larger one.
    if plt.fignum_exists(1):
        print("already have figure #1")
        fig = plt.figure(1)
    else:
        print("creating new figure")
        fig = plt.figure()

    for i in plt.get_fignums():
        print(f"after: figure #{i}")

    # scale the one and only Figure in this plot
    fig.set_dpi(dpi)
    fig.set_figwidth(w)
    fig.set_figheight(h)


def display_bar_chart():
    fn = f"\n{inspect.getframeinfo(inspect.currentframe()).function}"
    print(fn)

    scale_plot()

    centers = np.arange(1, 6)
    tops = np.arange(2, 12, 2)
    y_ticks = np.arange(0, 12, 1)
    plt.xlabel("centers")
    plt.ylabel("tops")
    plt.yticks(y_ticks)
    plt.bar(centers, tops)
    plt.title(f"{fn}")
    plt.grid()
    plt.show()


def display_bar_chart_from_dictionary():
    fn = f"\n{inspect.getframeinfo(inspect.currentframe()).function}"
    print(fn)

    scale_plot()

    fruits = {"apples": 10, "oranges": 16, "bananas": 9, "pears": 4}
    print(f"keys: {fruits.keys()}")
    print(f"values: {fruits.values()}")
    plt.xlabel("fruit")
    plt.ylabel("count")
    plt.bar(fruits.keys(), fruits.values())
    """
    this part is not working:

    vals = np.array(fruits.values())
    print(type(vals))
    print(vals)    
    max_y = vals.max(axis=0)
    print(max_y)
    # y_ticks = np.arange(0, len(fruits.keys()), 1)
    # plt.yticks(y_ticks)
    """
    plt.title(f"{fn}")
    plt.grid()
    plt.show()


def display_colored_line_plot():
    fn = f"\n{inspect.getframeinfo(inspect.currentframe()).function}"
    print(fn)

    scale_plot()

    # g = green, "-" = line, o = circles at each point on the line
    plt.plot([2, 4, 6, 8, 10], "g-o")
    plt.title(f"{fn}")
    plt.grid()
    plt.show()


def display_histogram():
    fn = f"\n{inspect.getframeinfo(inspect.currentframe()).function}"
    print(fn)

    scale_plot()

    plt.hist(random.randn(10000), 20)
    plt.title(f"{fn}")
    plt.grid()
    plt.show()


def display_labeled_plot():
    fn = f"\n{inspect.getframeinfo(inspect.currentframe()).function}"
    print(fn)

    scale_plot()

    xs = [1, 2, 3, 4, 5]
    ys = [2, 4, 6, 8, 10]
    plt.plot(xs, ys)
    plt.title(f"{fn}")
    plt.grid()
    plt.show()


def display_multi_line_numpy_plots():
    fn = f"\n{inspect.getframeinfo(inspect.currentframe()).function}"
    print(fn)

    scale_plot()

    # 5 rows, 4 columns in each row
    points = np.arange(1, 21).reshape(5, 4)
    print(f"points:\n{points}")
    plt.plot(points, "g-o")
    plt.title(f"{fn}")
    plt.grid()
    plt.show()


def display_multiple_plots():
    fn = f"\n{inspect.getframeinfo(inspect.currentframe()).function}"
    print(fn)

    scale_plot()

    plt.plot([1, 2, 3, 4, 5], "g-o")
    plt.plot([1, 2, 4, 8, 16], "b-^")
    plt.title(f"{fn}")
    plt.grid()
    plt.show()


def display_simple_numpy_plot():
    fn = f"\n{inspect.getframeinfo(inspect.currentframe()).function}"
    print(fn)

    scale_plot()

    points = np.arange(1, 6)
    print(f"points: {points}")
    plt.plot(points, "r-o")
    plt.title(f"{fn}")
    plt.grid()
    plt.show()


def display_simple_plot():
    fn = f"\n{inspect.getframeinfo(inspect.currentframe()).function}"
    print(fn)

    scale_plot()

    plt.plot([1, 2, 3, 4, 5])
    plt.title(f"{fn}")
    plt.grid()
    plt.show()


def tutorial_simple():
    fn = f"\n{inspect.getframeinfo(inspect.currentframe()).function}"
    print(fn)

    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    scale_plot()
    ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
    plt.title(f"{fn}")
    plt.grid()
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print(f"Python version: {get_python_version()}")
    print(f"NumPy version: {np.version.full_version}")
    # tutorial_simple()
    # display_bar_chart()
    # display_bar_chart_from_dictionary()
    # display_colored_line_plot()
    # display_histogram()
    # display_labeled_plot()
    # display_multi_line_numpy_plots()
    # display_multiple_plots()
    # display_simple_numpy_plot()
    display_simple_plot()