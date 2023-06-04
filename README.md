# Python Code Execution Guide

This guide provides instructions on how to successfully run the provided Python code. The code utilizes the `pyautogui` and `keyboard` libraries to automate mouse and keyboard actions.

## Prerequisites
Before running the code, ensure that you have the following prerequisites installed:

- Python 3.x: Visit the official Python website ([https://www.python.org](https://www.python.org)) to download and install Python.

## Installation
Follow the steps below to set up the code:

1. Download the Python code file and save it on your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory where you saved the Python code file.

## Dependencies Installation
You need to install the necessary libraries to execute the code. Run the following command in the terminal or command prompt:

```pip install pyautogui keyboard```

## Running the Code
To run the code, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory where you saved the Python code file.
3. Run the following command:

```python reviveNino.py```


Replace `<filename>` with the name of the Python code file.

## Usage Instructions

The code provides various functionalities and can be controlled using keyboard shortcuts. The following keyboard shortcuts are available:

- **F5**: Capture a new pixel color and position to monitor.
- **F6**: Execute the stored mouse click actions.
- **F7**: Save the current mouse position as a click coordinate.
- **F8**: Stop the program execution.
- **F9**: Execute predefined mouse click actions.

**Note:** The F-keys mentioned above are typically located at the top of the keyboard and may require pressing the "Fn" (Function) key on some laptops.

When the program starts, it enters the main loop, which continuously monitors the pixel color at the specified position. If the pixel color matches the target color stored in the `pixel_color.txt` file, it executes the stored mouse click actions.

You can customize the click coordinates and target pixel color by modifying the respective text files (`coordinates.txt` and `pixel_color.txt`). Each click coordinate should be listed as `x = <x-coordinate>, y = <y-coordinate>` on a separate line. The target pixel color should be specified as `R = <red-value>`, `G = <green-value>`, and `B = <blue-value>` on separate lines.

To add click coordinates, press **F7** while the program is running, and the current mouse position will be saved as a coordinate.

To capture a new pixel color and position to monitor, press **F5**. The program will prompt you to click on the desired pixel location on the screen. The pixel color at that location will be saved, along with its coordinates.

To execute the stored mouse click actions, press **F6**.

To stop the program execution, press **F8**.

To execute predefined mouse click actions, press **F9**.

## Important Note
Ensure that the Python code window is active when pressing the function keys to trigger the corresponding actions.

Feel free to modify the code to meet your specific requirements.

**Disclaimer**: This code may perform automated actions on your system. Use it responsibly and at your own risk.