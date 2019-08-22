class Robot:
    def __init__(self):
        self.a=10
        self._a=20
        self.__a=30

obj=Robot()
print(obj.a)
print(obj._a)
print(obj.__a) #here through error bcz ypu cant access privte variable outside
#of class so use getter and setter then access this
