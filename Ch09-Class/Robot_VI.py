class Robot:
    """
       This is the fifth class
    """
    count = 0
    def __init__(self, name = None):
        self.__set_name(name)
        type(self).count += 1
    def __del__(self):
        type(self).count -= 1
    def say_hi(self):
        print(self.name, ', says "hi!"')
    def __set_name(self, name):
        if name:
            self.__name = name
        else:
            self.__name = "Name not Given"
    def __get_name(self):
        return self.__name
    name = property(__get_name, __set_name)
