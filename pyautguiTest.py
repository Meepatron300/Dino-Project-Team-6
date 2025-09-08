import pyautogui as pag;
import os;
import keyboard;

pag.FAILSAFE = True;

currMouseXY = pag.position()
screenWidth, screenHeight = pag.size()
dinoImage = "Images\\ChromeDino.png" 
cactusImage = "Images\\DinoCactus.png"

pag.hotkey("ctrl + r")
# Attempt to fetch reference images
try:
    dinoLeft, dinoTop, dinoWidth, dinoHeight = pag.locateOnScreen(dinoImage, confidence=0.4)
except pag.ImageNotFoundException:
    dinoLeft= "Dino not found"
    dinTop = "Dino not found"
    dinoWidth = "no dino"
    dinoHeight = "no dino"
    print("Failed to find dino images")    
    os._exit(0)
    print("see this and exit did not work")
except FileNotFoundError or OSError:
    print("File not found")
    os._exit(0)


# Move the mouse to located dino
if (not(isinstance(dinoLeft,str))):

    pag.moveTo(dinoLeft,dinoTop,1)
    print(dinoLeft,dinoTop)
    pag.leftClick()

pag.sleep(1)
pag.press("SPACE")

while True:
    try:
        singleCacti = pag.locateAllOnScreen(cactusImage,confidence=0.2)
    except pag.ImageNotFoundException:
        singleCacti = []
    except FileNotFoundError or OSError:
        print("cactus file not found")
        break

    for cactus in singleCacti:
        cactusLeft, cactuTop = cactus[0],cactus[1]
        cactusWidth, cactusHeight = cactus[2], cactus[3]
        if cactusLeft - dinoLeft== (cactusWidth/2) + (dinoWidth/2):
            pag.press("SPACE")




