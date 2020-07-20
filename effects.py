import blinkt
import random
import time

blinkt.set_clear_on_exit(True)

def bright_math(wholenumber):
    return wholenumber/10

class effects:

    def stop(self):
        blinkt.clear()
        blinkt.show()

    def breathing(self):
        brightness = 0
        bright_low = 1
        bright_hi = 4
        bright_ramp = 0
        bright_sleep = 0.001
        inbetween = 1
        blinkt.set_all(255, 0, 0)
        blinkt.set_brightness(bright_math(brightness + 4))
        while brightness < bright_hi:
            time.sleep(bright_ramp)
            brightness += 2
            blinkt.set_brightness(bright_math(brightness))
            blinkt.show()
        time.sleep(2)
        while brightness > bright_low:
            time.sleep(bright_sleep)
            brightness -= 1
            blinkt.set_brightness(bright_math(brightness))
            blinkt.show()
        time.sleep(inbetween)

    def breathing_two(self):
        brightness = 0
        bright_low = 1
        bright_hi = 6
        bright_sleep = 0.03
        inbetween = 0.5
        blinkt.set_all(0, 255, 0)
        while brightness < bright_hi:
            time.sleep(bright_sleep)
            brightness += 1
            blinkt.set_brightness(bright_math(brightness))
            blinkt.show()
        while brightness > bright_low:
            time.sleep(bright_sleep)
            brightness -= 1
            blinkt.set_brightness(bright_math(brightness))
            blinkt.show()   
        time.sleep(inbetween)

    def processing(self):
        brightness = 1
        blinkt.set_brightness(bright_math(brightness))
        upper = random.randint(0, blinkt.NUM_PIXELS)
        pixels = [*range(0,upper)]
        blinkt.set_all(0, 0, 0)
        for pixel in pixels:
            blinkt.set_pixel(pixel,0,255,0)
            blinkt.show()
        blinkt.clear()

    def throbbing(self):
        brightness = 1
        blinkt.set_brightness(bright_math(brightness))
        pixels = [*range(0,blinkt.NUM_PIXELS)][-2:] + [*range(0,blinkt.NUM_PIXELS)][0:6]
        for pixel in pixels:
            blinkt.set_all(255, 0, 0)
            blinkt.set_pixel(pixel,0,0,0)
            if pixel == blinkt.NUM_PIXELS - 1:
                blinkt.set_pixel(0,0,0,0)
            else:
                blinkt.set_pixel(pixel+1,0,0,0)
            blinkt.show()
            time.sleep(0.5)
