
# Task 2: Use the cross product to compute the area of a convex, 2D polygon.

__author__ = "Cristián Calvo Barentin"
__email__ = "calvo@arch.ethz.ch"
__date__ = "30.10.2019"


def area_polygon(polygon):

    """
    Compute the area of a convex polygon

    Parameters
        polygon (compas.geometry.polygon) - 2D polygon

    Returns
        float - area of the polygon
    """
    if not polygon.is_convex():
        raise ValueError("Polygon is not convex")

    c = polygon.centroid
    area = 0
    vertices = list(polygon)

    # area of the polygon is the sum of all triangles form by two consecutive vertices and centroid
    
    for i in range(len(vertices)):
        u = polygon[i-1] 
        v = polygon[i] 
        area = area + (c - u).cross(c - v).length/2

    return area



if __name__ == '__main__':

    from compas.geometry import Polygon

    polygon = Polygon([
    [0.0, 0.0, 0.0],
    [1.0, 0.0, 0.0],
    [1.0, 1.0, 0.0],
    [0.0, 1.0, 0.0]
    ])

    print(area_polygon(polygon))