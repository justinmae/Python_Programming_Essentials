class Robot:
    """
       This is the third class
    """
    count = 0
    def __init__(self, name = None):
        self.name = name
        type(self).count += 1
    def __del__(self):
        type(self).count -= 1
