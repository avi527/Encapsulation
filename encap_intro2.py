class Person:
    def __init__(self,name,salary):
        self.__name=name
        self.__salary=salary
p=Person('avinash',5000)
p.salary=6000
print(p.salary)
