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

executeAction(dinoAction)