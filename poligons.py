import math

def shape_poligon(sides, center_x, center_y, radius):
    vertices = []
    for i in range(sides):
         angle = (2 * math.pi / sides) * i - math.pi/2
         x = center_x + radius * math.cos(angle)
         y = center_y + radius * math.sin(angle)
         vertices.append((x, y))
    return vertices