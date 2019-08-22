class Robot:
    def __init__(self):
        self.__version=2019
    def getVersion(self):
        print(self.__version)
    def setVersion(self,version):
        self.__version=version

obj = Robot()
obj.setVersion(23)
obj.getVersion()




