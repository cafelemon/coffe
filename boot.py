from main import*
# from dcmotor import*
from machine import Pin,PWM
from time import sleep
forward = Pin(12,Pin.OUT)
backwards = Pin(14,Pin.OUT)
servo = Servo(18,50)
forward.value(0)
backwards.value(0)
while True:
#     motor = DCMotor (13,15,1000)
#     motor.forward(10)
    forward.value(1)
    backwards.value(0)
    print("前进")
    sleep(2)
    backwards.value(1)
    forward.value(0)
#     motor.backwards(10)
    print("后退")
    sleep(2)
#     motor.stop()

    servo.turn(00)
    print("左转圈")
    sleep(2)
    servo.turn(180)
    print("右转")
    sleep(2)
    servo.turn(90)
    sleep(2)
    print("回正")