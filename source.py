import webbrowser
import time
import keyboard
import pyautogui as pag
from PIL import ImageGrab

dinoAction = "run" # States: run, duck, jump, high jump
dinoAction = "duck"

def timedPress(key, seconds=.8):
    pag.keyDown(key)
    pag.sleep(seconds)
    pag.keyUp(key)

targetsY = 0 # Y position of detected color(maybe relative to dino?)
targetsColor = "gray" # Replace gray with whatever hexadecimal or color code matches dino
nightMode = False # Night/Inverted modes

# Dinosaur movement controling function (pass in the vision state command)
def executeAction(dinoAction):
    if dinoAction == "duck":
        timedPress("down", 1)
        dinoAction = "run"
    elif dinoAction == "jump":
        timedPress("up", .1)
        dinoAction = "run"
    elif dinoAction == "high jump":
        timedPress("up", .8)
        dinoAction = "run"

# Sets the direction path for opening the chrome browser based on the typical location
chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

# Opens the above browser to https://trex-runner.com/, which has to be used instead of
# chrome://dino/ because something gets confused when opening that tab :(
webbrowser.get('chrome').open_new("https://trex-runner.com/")

time.sleep(1.5)
pag.click(1275, 450)
pag.click(1275, 450)
pag.click(1275, 500)
time.sleep(0.5)

# Use pag.click(target_x, target_y) to test where the coords actually are
# Key: G - good; B - bad; Uppercase - high confidence; Lowercase - low confidence.
# Trigger coords:
sky_sensor = [400,500] #G
jump_trig = [750,680] #g
high_jump_trig = [750,680] #g
duck_trig = [550,650] #g

# 0: bottom left sensor, 1: top left sensor, 2: bottom right sensor
type_sense = [[1000,690], [1000,640], [1060,690]]

# Expand the bounding box as needed (left, top, right, bottom)
bBox = (399, 499, 1071, 691)
action_queue = ["empty"]

# Game start
pag.keyDown("Space")
sens_cd_base = trig_cd_base = game_start = time.perf_counter()

# IMPORTANT: The White Background is (247, 247, 247) and the contrasting color is (83, 83, 83)
# Main sight logic, will run till the escape key is pressed
while not keyboard.is_pressed('Esc'):
    screen_capture = ImageGrab.grab(bbox=bBox)
    sky_color = screen_capture.getpixel((sky_sensor[0]-bBox[0], sky_sensor[1]-bBox[1]))
    sensor_1 = screen_capture.getpixel((type_sense[0][0]-bBox[0], type_sense[0][1]-bBox[1]))
    sensor_2 = screen_capture.getpixel((type_sense[1][0]-bBox[0], type_sense[1][1]-bBox[1]))
    sensor_3 = screen_capture.getpixel((type_sense[2][0]-bBox[0], type_sense[2][1]-bBox[1]))

    # Removes the empty list buffer for actual queue usage
    if action_queue[0] == "empty":
        action_queue.pop(0)

    # Is the sensor on cooldown?
    if time.perf_counter() > (sens_cd_base + 0.01):
        # What sensors are active?
        if sensor_1 != sky_color:
            if sensor_3 != sky_color or sensor_2 != sky_color:
                action_queue.append("high jump")
            else:
                action_queue.append("jump")
            sens_cd_base = time.perf_counter()
        elif sensor_2 != sky_color:
            action_queue.append("duck")
            sens_cd_base = time.perf_counter()
            

    # Protects the detector from an empty list should the action queue be cleared
    if len(action_queue) == 0:
        action_queue.append("empty")

    # Are the action triggers on cooldown?
    # Looks for the next trigger needed based on the action queue
    if time.perf_counter() > trig_cd_base + 0.1:
        if action_queue[0] == "jump":
            if screen_capture.getpixel((jump_trig[0]-bBox[0], jump_trig[1]-bBox[1])) != sky_color:
                trig_cd_base = time.perf_counter()
                executeAction(action_queue[0])
                action_queue.pop(0)
        elif action_queue[0] == "high jump":
            if screen_capture.getpixel((high_jump_trig[0]-bBox[0], high_jump_trig[1]-bBox[1])) != sky_color:
                trig_cd_base = time.perf_counter()
                executeAction(action_queue[0])
                action_queue.pop(0)
        elif action_queue[0] == "duck":
            if screen_capture.getpixel((duck_trig[0]-bBox[0], duck_trig[1]-bBox[1])) != sky_color:
                trig_cd_base = time.perf_counter()
                executeAction(action_queue[0])
                action_queue.pop(0)
    
    if screen_capture.getpixel((high_jump_trig[0]-bBox[0], high_jump_trig[1]-bBox[1])) != sky_color or screen_capture.getpixel((duck_trig[0]-bBox[0], high_jump_trig[1]-bBox[1])) != sky_color:
        executeAction("jump")
        screen_capture.getpixel((high_jump_trig[0]-bBox[0], high_jump_trig[1]-bBox[1])) != sky_color

    # Protects the empty list detector
    if len(action_queue) == 0:
        action_queue.append("empty")