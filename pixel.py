class Pixel:
        def __init__(self, x, y, value):
            self.x = x
            self.y = y
            self.value = value

        def __eq__(self, other):
            if isinstance(other, Pixel):
                return other.x == self.x and other.y == self.y and other.value == self.value
            
            return False