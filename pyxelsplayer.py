import pyautogui
import time
import keyboard
import random

COORDINATES_FILENAME = "coordinates.txt"


def click_coordinates(coordinates):
    for coordinate in coordinates:
        x, y = coordinate["x"] + random.randint(-3, 3), coordinate[
            "y"
        ] + random.randint(-1, 1)
        pyautogui.click(x, y)
        time.sleep(0.2)


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


def main_loop():
    while True:
        if keyboard.is_pressed("q"):
            position = pyautogui.position()
            coordinates = read_coordinates(COORDINATES_FILENAME)
            coordinates.append({"x": position.x, "y": position.y})
            save_coordinates(coordinates, COORDINATES_FILENAME)
            time.sleep(0.2)

        if keyboard.is_pressed("e"):
            coordinates = read_coordinates(COORDINATES_FILENAME)
            if coordinates:
                for _ in range(4):
                    click_coordinates(coordinates)
                    time.sleep(1)
                    pyautogui.keyDown("up")
                    time.sleep(0.55)
                    pyautogui.keyUp("up")
                click_coordinates(coordinates)
            break

        if keyboard.is_pressed("f8"):
            break


# Main program
print("Bot inicializado!")
while True:
    main_loop()
    if keyboard.is_pressed("f8"):
        break
