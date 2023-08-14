import ctypes
import inspect
import sys
import tkinter as tk
#
import matplotlib.pyplot as plt
import numpy as np
import pyautogui

#
import pyautogui as pag
from numpy import random
import plotly.express as px
#
from random_walk import RandomWalk
from die import Die


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
    :returns dots per inch (DPI)
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


def display_random_walk():
    fn = f"\n{inspect.getframeinfo(inspect.currentframe()).function}"
    print(fn)
    # Keep making new walks, as long as the program is active.
    while True:
        # Make a random walk.
        rw = RandomWalk(50_000)
        rw.fill_walk()

        # Plot the points in the walk.
        plt.style.use("classic")
        fig, ax = plt.subplots()
        scale_plot()
        point_numbers = range(rw.num_points)
        ax.scatter(
            rw.x_values,
            rw.y_values,
            c=point_numbers,
            cmap=plt.cm.Blues,
            edgecolors="none",
            s=1,
        )
        ax.set_aspect("equal")

        # Emphasize the first and last points.
        ax.scatter(0, 0, c="green", edgecolors="none", s=100)
        ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)

        # Remove the axes.
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        plt.grid()
        plt.title(f"{fn}")
        plt.show()

        # keep_running = input("Make another walk? (y/n): ")
        keep_running = pag.confirm(
            "Make another walk?", "Keep Running?", buttons=["Yes", "No"]
        )
        if keep_running.lower()[:1] == "n":
            break


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


def display_squares():
    """Python Crash Course, Chapter 15, Plot Squares"""
    fn = f"\n{inspect.getframeinfo(inspect.currentframe()).function}"
    print(fn)
    input_values = [1, 2, 3, 4, 5]
    squares = [1, 4, 9, 16, 25]

    # plt.style.use("seaborn-v0_8")
    fig, ax = plt.subplots()
    scale_plot()
    # avoid PyPlot's default assumption that x values start at zero by explicitly specifying the x and y values.
    ax.plot(input_values, squares, linewidth=3)

    # Set chart title and label axes.
    ax.set_title(f"{fn} - Square Numbers", fontsize=24)
    ax.set_xlabel("Value", fontsize=14)
    ax.set_ylabel("Square of Value", fontsize=14)

    # Set size of tick labels.
    ax.tick_params(labelsize=14)
    plt.grid()
    plt.show()


def display_squares_scatter():
    """Python Crash Course, Chapter 15, Plot Scattered Squares"""
    fn = f"\n{inspect.getframeinfo(inspect.currentframe()).function}"
    print(fn)

    x_values = range(1, 1001)
    y_values = [x**2 for x in x_values]

    # plt.style.use("seaborn-v0_8")
    fig, ax = plt.subplots()
    scale_plot()
    # fade in the plot line from very faint blue to dart blue
    ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

    # Set chart title and label axes.
    ax.set_title(f"{fn} - Square Numbers", fontsize=24)
    ax.set_xlabel("Value", fontsize=14)
    ax.set_ylabel("Square of Value", fontsize=14)

    # Set size of tick labels.
    ax.tick_params(labelsize=14)

    # Set the range for each axis.
    ax.axis([0, 1100, 0, 1_100_000])
    ax.ticklabel_format(style="plain")
    plt.grid()
    plt.show()


def display_transposed_multi_line_plots():
    fn = f"\n{inspect.getframeinfo(inspect.currentframe()).function}"
    print(fn)

    scale_plot()

    # 5 rows, 4 columns in each row
    points = np.arange(1, 21).reshape(5, 4)
    print(f"points:\n{points}")
    points_transposed = points.transpose()
    print(f"points transposed:\n{points_transposed}")
    plt.plot(points_transposed, "g-o")
    plt.title(f"{fn}")
    plt.grid()
    plt.show()


def display_w_plot():
    fn = f"\n{inspect.getframeinfo(inspect.currentframe()).function}"
    print(fn)
    scale_plot()
    xs = [1, 2, 3, 4, 5]
    ys = [3, -1, 4, 0, 6]
    plt.plot(xs, ys)
    plt.title(f"{fn}")
    plt.grid()
    plt.show()


def roll_die():
    fn = f"\n{inspect.getframeinfo(inspect.currentframe()).function}"
    print(fn)

    die = Die()
    results = []
    for roll_num in range(1_000):
        result = die.roll()
        results.append(result)
    # print(results)
    frequencies = []
    poss_results = range(1, die.num_sides+1) # instead of 0-to-5, we want 1-to-6
    for value in poss_results:
        frequency = results.count(value)
        frequencies.append(frequency)

    # print(frequencies)
    # visualize
    title = f"{fn} - Results of Rolling One D6 1,000 Times"
    labels = {'x': 'Result', 'y': 'Frequency of Result'}
    # Reference: https://plotly.com/python-api-reference/generated/plotly.express.bar.html
    fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
    # fig.print_grid()
    fig.show()


def tutorial_random_dot_plot():
    fn = f"\n{inspect.getframeinfo(inspect.currentframe()).function}"
    print(fn)

    np.random.seed(19680801)  # seed the random number generator.
    data = {
        "a": np.arange(50),
        "c": np.random.randint(0, 50, 50),
        "d": np.random.randn(50),
    }
    data["b"] = data["a"] + 10 * np.random.randn(50)
    data["d"] = np.abs(data["d"]) * 100

    plt.style.use("fivethirtyeight")
    fig, ax = plt.subplots(layout="constrained")
    scale_plot()
    ax.scatter("a", "b", c="c", s="d", data=data)
    ax.set_xlabel("entry a")
    ax.set_ylabel("entry b")

    plt.title(fn)
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


if __name__ == "__main__":
    print(f"Python version: {get_python_version()}")
    print(f"NumPy version: {np.version.full_version}")
    print(f"PyAutoGUI version: {pyautogui.getInfo()[2]}")

    # uncomment one of the following at a time to see its plot displayed:
    # display_bar_chart()
    # display_bar_chart_from_dictionary()
    # display_colored_line_plot()
    # display_histogram()
    # display_labeled_plot()
    # display_multi_line_numpy_plots()
    # display_multiple_plots()
    # display_random_walk()
    # display_simple_numpy_plot()
    # display_simple_plot()
    # display_squares()
    # display_squares_scatter()
    # display_transposed_multi_line_plots()
    # display_w_plot()
    roll_die()
    # tutorial_random_dot_plot()
    # tutorial_simple()
