from machine import Pin,PWM
class Servo:
    def __init__(self,pin,freq):#构造函数
        self.pin =PWM(Pin(pin,Pin.OUT),freq)
        self.turn(90)#初始化角度设置
    def turn(self,angle):
        value = int(500+(angle/180)*(2500 - 500))
        self.pin.duty_ns(value * 1000)#微妙转换成纳秒
