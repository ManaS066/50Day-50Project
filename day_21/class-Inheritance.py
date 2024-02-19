class Animal:
    def __init__(self):
        self.num_eye = 2

    def breathe(self):
        print("breathing")


class Fish(Animal):
    def __init__(self):
        super().__init__()
    def swim(self):
        print("swiming")
    def breathe(self):
        #modify the super class 
        super().breathe()
        print("doing under water")


nimo=Fish()
print(nimo.num_eye)
nimo.breathe()
nimo.swim()
mimo=Animal()
mimo.breathe()

