
# Task 1: Given two vectors, use the cross product to create a set of three orthonormal vectors.

__author__ = "Cristián Calvo Barentin"
__email__ = "calvo@arch.ethz.ch"
__date__ = "30.10.2019"


def orthonormal_vectors_from_two_vectors(u,v):
    
    """
    Generate three orthonormal vectors from two given vectors

    Parameters
        u (compas.geometry.Vector) - first vector
        v (compas.geometry.Vector) - second vector

    Returns
        3-tuple - three orthonormal Vectors as tuple
    """
    
    w = u.cross(v)

    return u.unitized(), u.cross(w).unitized(), w.unitized()


if __name__ == '__main__':
    from compas.geometry import Vector

    u = Vector(12.0, 3.0, -1.0)
    v = Vector(2.0, -9.0, 3.0)
        
    print(orthonormal_vectors_from_two_vectors(u,v))