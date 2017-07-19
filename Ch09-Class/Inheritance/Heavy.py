from Stutter import Stutter

class Heavy(Stutter):
    def __init__(self, name=None, times=3, weight=0):
        super().__init__(name=name, times=times)
        self.__set_weight(weight)

    def __set_weight(self, weight):
        if weight > 300:
            self.__weight = 300
        else:
            self.__weight = weight
    def __get_weight(self):
        return self.__weight
    weight = property(__get_weight, __set_weight)
