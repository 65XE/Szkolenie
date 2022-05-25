class Point:
    def __init__(self, x, y, z, xx, yy):
        self.move(x, y, z, xx, yy)

    def move(self, x, y, z, xx, yy):
        self.x = x
        self.y = y
        self.z = z
        self.xx = xx
        self.yy = yy


    def reset(self):
        self.move(0, 0)


    def calculate_distance(self):
        return self.x + self.y + self.z + self.xx + self.yy

if __name__ == '__main__':
    print("Point!")

    point = Point(3, 5, 7, 9, 2)
    print(point.x, point.y, point.z, point.xx, point.yy)
    print(point.calculate_distance())