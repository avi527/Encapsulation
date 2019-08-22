#in an object oriented python program you can restrict access to methods
#and variables.this can prevent the data from being modified by accident
#and is know as encapsulation

class Car:
    def __init__(self,speed,color):
        self.speed=speed
        self.color=color

    def set_speed(self,value):
        self.speed=value

    def get_speed(self):
        return self.speed

ford=Car(200,'red')
honda=Car(250,'blue')
audi=Car(300,'black')
ford.speed=500
print(ford.speed)
print(ford.color)

