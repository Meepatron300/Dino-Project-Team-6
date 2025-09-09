import webbrowser
import pyautogui as pag
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
