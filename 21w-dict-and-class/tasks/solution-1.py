'''
직접 해보기

종현(Umnik)과 종현의 친구(Omull)는 마인크래프트를 하고 있다.
종현과 종현의 친구까지의 직선 거리를 구하려고 하는데, 결과가 제대로 나타나지 않는다.

아래 코드를 적절하게 수정하여 제대로 작동하게 만들어보자.

* 아래 Coordinate3D 클래스는 3차원 세상에서 좌표를 표현하는 클래스이다.
'''

class Coordinate3D:
    x: int = 0
    y: int = 0
    z: int = 0

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def distance(self, other) -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2) **.5

Umnik_position = Coordinate3D(100, 350, 330)
Omull_position = Coordinate3D(-100, 0, 900)

print(Umnik_position.distance(Omull_position))
