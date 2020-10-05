from sense_emu import SenseHat
import time
import keyboard

s = SenseHat()
s.low_light = True


green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

def d():
    G = green
    Y = yellow
    B = blue
    O = nothing
    logo = [
    O, O, G, G, O, O, O, O,
    O, O, G, O, G, O, O, O,
    O, O, G, O, O, G, O, O,
    O, O, G, O, O, G, O, O,
    O, O, G, O, O, G, O, O,
    O, O, G, O, O, G, O, O,
    O, O, G, O, G, O, O, O,
    O, O, G, G, O, O, O, O,
    ]
    return logo

def g():
    G = green
    Y = yellow
    B = blue
    O = nothing
    logo = [
    O, O, B, B, B, B, O, O,
    O, O, B, O, O, O, O, O,
    O, O, B, O, O, O, O, O,
    O, O, B, O, O, O, O, O,
    O, O, B, O, B, B, O, O,
    O, O, B, O, O, B, O, O,
    O, O, B, O, O, B, O, O,
    O, O, B, B, B, B, O, O,
    ]
    return logo


images = [d,g]
count = 0


while True:
    if keyboard.press('up arrow'):
        s.set_pixels(images[count % len(images)]())
        time.sleep(1)
    elif keyboard.press('down arrow'):
        s.set_pixels(images[count % len(images)]())
        time.sleep(1)
    elif keyboard.press('left arrow'):
        s.set_pixels(images[count % len(images)]())
        time.sleep(1)
    elif keyboard.press('right arrow'):
        s.set_pixels(images[count % len(images)]())
        time.sleep(1)
    else:
        print('waiting')
        time.sleep(1)
    count += 1
