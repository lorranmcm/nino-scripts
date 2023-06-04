import pyautogui
import time
import keyboard


PIXEL_COLOR_FILENAME = "pixel_color.txt"
COORDINATES_FILENAME = "coordinates.txt"
PIXEL_POSITION_FILENAME = "pixel_position.txt"


def click_coordinates(coordinates):
    for coordinate in coordinates:
        x, y = coordinate["x"], coordinate["y"]
        pyautogui.click(x, y)
        time.sleep(3)


def save_pixel_color(pixel_color, filename):
    r, g, b = pixel_color
    with open(filename, "w") as file:
        file.write(f"R = {r}\n")
        file.write(f"G = {g}\n")
        file.write(f"B = {b}\n")
    print(f"Pixel color is {r} {g} {b}")


def read_pixel_color(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        if len(lines) >= 3:
            r = int(lines[0].split("=")[1].strip())
            g = int(lines[1].split("=")[1].strip())
            b = int(lines[2].split("=")[1].strip())
            return r, g, b
        else:
            print("Invalid pixel color file format")
            return None


def save_coordinates(coordinates, filename):
    with open(filename, "w") as file:
        for coordinate in coordinates:
            x, y = coordinate["x"], coordinate["y"]
            file.write(f"x = {x}, y = {y}\n")
            print(f"Coordinate x = {x}, y = {y} saved!")


def read_coordinates(filename):
    coordinates = []
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            if line.strip():
                parts = line.split(",")
                if len(parts) == 2:
                    x = parts[0].strip().split("=")[1].strip()
                    y = parts[1].strip().split("=")[1].strip()
                    coordinates.append({"x": int(x), "y": int(y)})
    return coordinates


def save_pixel_to_monitor(coordinates, filename):
    x, y = coordinates["x"], coordinates["y"]
    with open(filename, "w") as file:
        file.write(f"x = {x}, y = {y}\n")
        print(f"Pixel position x = {x}, y = {y} saved!")


def perform_actions():
    # Clicks
    pyautogui.click(x=2536, y=42)
    time.sleep(1)
    pyautogui.click(x=2512, y=387)
    time.sleep(1)
    pyautogui.click(x=2427, y=453)
    time.sleep(1)
    pyautogui.click(x=1709, y=535)
    time.sleep(1)
    pyautogui.click(x=2001, y=618)
    time.sleep(10)
    pyautogui.press("f")
    time.sleep(1)
    pyautogui.click(x=2518, y=331)
    time.sleep(1)
    pyautogui.click(x=2233, y=998)


def main_loop():
    pixel_to_monitor = read_coordinates(PIXEL_POSITION_FILENAME)[0]

    while True:
        pixel_color = pyautogui.pixel(pixel_to_monitor["x"], pixel_to_monitor["y"])
        target_color = read_pixel_color(PIXEL_COLOR_FILENAME)

        if pixel_color == target_color:
            coordinates = read_coordinates(COORDINATES_FILENAME)
            if coordinates:
                click_coordinates(coordinates)

        if keyboard.is_pressed("f5"):
            new_pixel_to_monitor = pyautogui.position()
            new_pixel_color = pyautogui.pixel(
                new_pixel_to_monitor[0], new_pixel_to_monitor[1]
            )
            save_pixel_color(new_pixel_color, PIXEL_COLOR_FILENAME)
            save_pixel_to_monitor(
                {"x": new_pixel_to_monitor[0], "y": new_pixel_to_monitor[1]},
                PIXEL_POSITION_FILENAME,
            )
            break

        if keyboard.is_pressed("f6"):
            coordinates = read_coordinates(COORDINATES_FILENAME)
            if coordinates:
                click_coordinates(coordinates)
            break

        if keyboard.is_pressed("f7"):
            position = pyautogui.position()
            coordinates = read_coordinates(COORDINATES_FILENAME)
            coordinates.append({"x": position.x, "y": position.y})
            save_coordinates(coordinates, COORDINATES_FILENAME)
            time.sleep(0.2)

        if keyboard.is_pressed("f8"):
            break

        if keyboard.is_pressed("f9"):
            perform_actions()


# Main program
while True:
    main_loop()
    if keyboard.is_pressed("f8"):
        break
