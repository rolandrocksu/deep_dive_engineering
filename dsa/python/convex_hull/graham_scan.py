from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int


points = [
    Point(1, 2),
    Point(2, 3),
    Point(4, 5),
    Point(6, 7),
    Point(8, 9),
    Point(9, 4),
    Point(3, 1),
    Point(7, 6),
]

def graham_scan():
    global points
    bottom_point = min(points, key=lambda point: point.y)

    sorted_points = []
    for point in points:
        tanges_alpha = (point.y - bottom_point.y) / (point.x - bottom_point.x)

    print(bottom_point)
    

graham_scan()
