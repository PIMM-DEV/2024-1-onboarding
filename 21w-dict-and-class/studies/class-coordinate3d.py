class Coordinate3D:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
    
    def to_string(self):
        return f'({self.x}, {self.y}, {self.z})'

a = Coordinate3D()
a.x = 7

b =  Coordinate3D()
b.y = 6

print(a.to_string())
print(b.to_string())