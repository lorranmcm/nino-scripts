import pyautogui
import keyboard
import time


def on_key_event(e):
    global key_pressed, start_time
    if e.event_type == keyboard.KEY_DOWN:
        key_pressed = e.name
        start_time = time.time()
    elif e.event_type == keyboard.KEY_UP and e.name == key_pressed:
        duration = time.time() - start_time
        print(f"Key '{key_pressed}' pressed for {duration:.2f} seconds")


# Set up the listener
keyboard.hook(on_key_event)

try:
    # Your main application loop
    while True:
        # Do other things if needed
        pass
except KeyboardInterrupt:
    pass
finally:
    # Unhook the listener when the script exits
    keyboard.unhook_all()
