from Robot import Robot

class Stutter(Robot):
    def __init__(self, name=None, times=1):
        super().__init__(name=name)
        self.__times = times

    def say_hi(self):
        print('Hi! ' * self.__times, end="")
        print("Said " + super().name)

    def say_goodbye(self):
        print('goodbye! ' * self.__times, end="")
        print("Said " + super().name)
