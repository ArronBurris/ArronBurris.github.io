#object based programing

#car class example

class Car:
    def __init__(self, carColor, carType, engineSize):
        self.carColor = carColor
        self.carType = carType
        self.engineSize = engineSize
        # self lines up with c1

    def revEngine(self):
        if (self.engineSize == "v6"):
            return "zoom zoom"
        elif (self.engineSize == "v8"):
            return "vroom vroom"


c1 = Car("blue", "coupe", "v6")

print(c1.carColor)

print(c1.carType)

print(c1.engineSize)

print(c1.revEngine())
