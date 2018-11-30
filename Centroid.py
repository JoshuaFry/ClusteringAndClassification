class Centroid:
    data = []

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_new_center(self):
        for pt in self.data:
            print()