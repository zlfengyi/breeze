import RPi.GPIO as GPIO
import time

red_led = 0
green_led = 0
blue_led = 0

def init():
    global red_led
    global green_led
    global blue_led
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(17, GPIO.OUT)
    red_led = GPIO.PWM(17, 100)
    red_led.start(0)

    GPIO.setup(27, GPIO.OUT)
    green_led = GPIO.PWM(27, 100)
    green_led.start(0)

    GPIO.setup(22, GPIO.OUT)
    blue_led = GPIO.PWM(22, 100)
    blue_led.start(0)

    print("GPIO Initialize finish.")

def set_red(value):
    global red_led
    red_led.ChangeDutyCycle(value*100/256)
def set_green(value):
    global green_led
    green_led.ChangeDutyCycle(value*100/256)
def set_blue(value):
    global blue_led
    blue_led.ChangeDutyCycle(value*100/256)

def set_color(r, g, b):
    set_red(r)
    set_green(g)
    set_blue(b)

def clean():
    global blue_led
    global green_led
    global red_led

    red_led.stop()
    green_led.stop()
    blue_led.stop()
    GPIO.cleanup()
    print("GPIO clean up!")

if __name__ == "__main__":
    init()
    for i in xrange(10):
        set_blue(i*10)
        time.sleep(0.1)
    clean()
