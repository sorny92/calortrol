#import wiringpi

class HeaterController:
    #Let's set a delay to give time the servo to react
    delay_period = 0.1

    def __init__(self):
        #Configure the 18th pin in PWM out with miliseconds counting
#        wiringpi.wiringPiSetupGpio()
#        wiringpi.pinMode(17, wiringpi.GPIO.PWM_OUTPUT)
#        wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

        #Set clock of the pwm out
#        wiringpi.pwmSetClock(192)
#        wiringpi.pwmSetRange(2000)

        # Once initilized, switchOff automatically, for security
        self.switchOff()

    def switchOn(self):
        print('on')
    def switchOff(self):
        print('off')