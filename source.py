import webbrowser
import time
import pyautogui as pag
from PIL import ImageGrab

dinoAction = "run" # States: run, duck, jump, high jump
dinoAction = "duck"

def timedPress(key,seconds=.8):
    pag.keyDown(key)
    pag.sleep(seconds)
    pag.keyUp(key)

targetsY = 0 # Y position of detected color(maybe relative to dino?)
targetsColor = "gray" # Replace gray with whatever hexadecimal or color code matches dino
nightMode = False # Night/Inverted modes

# Dinosaur movement controling function (pass in the vision state command)
def executeAction(dinoAction):
    if dinoAction == "duck":
        timedPress("down")
        dinoAction = "run"
    elif dinoAction == "jump":
        timedPress("up",.1)
        dinoAction = "run"
    elif dinoAction == "high jump":
        timedPress("up",.8)
        dinoAction = "run"

# Sets the direction path for opening the chrome browser based on the typical location
chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

# Opens the above browser to https://trex-runner.com/, which has to be used instead of
# chrome://dino/ because something gets confused when opening that tab :(
webbrowser.get('chrome').open_new("https://trex-runner.com/")

time.sleep(0.5)
pag.click(1275, 450)
pag.click(1275, 450)
pag.click(1275, 500)
time.sleep(0.5)

# short hops need to be an early thing and big jumps need to be in the middle and ducks are last minute
short_x = 550 #B
short_y = 680 #B
tall_x = 650 #g
tall_y = 680 #g
duck_x = 550 #G
duck_y = 650 #G
pag.click(duck_x, duck_y)

# IMPORTANT: The White Background is (247, 247, 247) and the contrasting color is (83, 83, 83)
screen_capture = ImageGrab.grab()
short_y
pixel_rgb = screen_capture.getpixel((short_x, short_y))

print(f"The RGB color of the pixel at ({short_x}, {short_y}) is: {pixel_rgb}")