import time
import keyboard
import mouse
import threading
import os

if os.name == 'nt':
    os.system('')

RESET = '\033[0m'
BOLD = '\033[1m'
ITALIC = '\033[3m'
UNDERLINE = '\033[4m'

def print_colored_text(text, color='', background='', style=''):
    formatted_text = f"{style}{color}{background}{text}{RESET}"
    print(formatted_text, end='', flush=True)
    
def Clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def main():
    logo = """
                    \033[38;5;196m (       )     )       (       )    )  \033[0m
                    \033[38;5;202m )\ ) ( /(  ( /(  *   ))\ ) ( /( ( /(  \033[0m
                    \033[38;5;202m(()/( )\()) )\()` )  /(()/( )\()))\()) \033[0m
                    \033[38;5;208m /(_)((_)\ ((_)\ ( )(_)/(_)((_)\((_)\  \033[0m
                    \033[38;5;208m(_))   ((_)  ((_(_(_()(_))  _((___((_) \033[0m
                    \033[38;5;214m| _ \ / _ \ / _ |_   _/ __|| || \ \/ / \033[0m
                    \033[38;5;214m|   /| (_) | (_) || | \__ \| __ |>  <  \033[0m
                    \033[38;5;220m|_|_\ \___/ \___/ |_| |___/|_||_/_/\_\ \033[0m

                                   \033[38;5;220mHORSEDASH\033[0m
                          \033[38;5;220mgithub.com/rootshx/horsedash\033[0m

"""
    Clear()
    print(logo)

if __name__ == "__main__":
    main()


def firstjump():
    mouse.press(button='right')
    time.sleep(0.1)
    mouse.release(button='right')

def adjustcar():
    keyboard.press('w')
    time.sleep(0.05)
    keyboard.release('w')
    keyboard.press('e')
    time.sleep(0.05)
    keyboard.release('e')
    time.sleep(1)

def jump_backwards():
    keyboard.press('s')
    mouse.press(button='right')
    time.sleep(0.064)
    keyboard.release('s')
    mouse.release(button='right')
    time.sleep(0.064)

def jump_forwards():
    keyboard.press('w')
    mouse.press(button='right')
    time.sleep(0.064)
    keyboard.release('w')
    mouse.release(button='right')
    time.sleep(0.064)

def HorseDash():
    firstjump()
    adjustcar()
    print("Horse Dash loop started. Press 'H' again to stop.")
    while horse_dash_active:  # Continues until the flag is set to False
        jump_backwards()
        jump_forwards()
        time.sleep(0.01)
    print("Horse Dash loop stopped.")

# Flag to control HorseDash loop
horse_dash_active = False

# Function to toggle HorseDash on/off
def toggle_horse_dash():
    global horse_dash_active
    horse_dash_active = not horse_dash_active
    if horse_dash_active:
        # Run HorseDash in a separate thread so we can control it asynchronously
        threading.Thread(target=HorseDash).start()

# Bind the toggle function to 'h' key press
keyboard.on_press_key("h", lambda _: toggle_horse_dash())

print("Press 'H' to start or stop Horse Dash.")
keyboard.wait("esc")  # Keep the script running until 'esc' is pressed
