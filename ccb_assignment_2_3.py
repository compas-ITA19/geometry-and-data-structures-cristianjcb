
# Task 3: Define a function for computing the cross products of two arrays of vector

__author__ = "Cristián Calvo Barentin"
__email__ = "calvo@arch.ethz.ch"
__date__ = "30.10.2019"

def cross_vectors(u,v):

    """
    The cross product between two given vectors

    Paremeters
        u (list) - first vector
        v (list) - second vector

    Returns
        3-tuple - The cross product
    """

    c = (u[1] * v[2] - u[2] * v[1],
         u[2] * v[0] - u[0] * v[2],
         u[0] * v[1] - u[1] * v[0])

    return c

def cross_two_arrays(U, V):

    """
    the cross products of two arrays of vector if they have the same length

    Paremeters
        U (list) - first array
        V (list) - second array

    Returns
        list - The cross products
    """

    if len(U) != len(V):
        raise Exception("Arrays don't have the same length")
    
    return [cross_vectors(U[i],V[i]) for i in range(len(U))]



def cross_two_arrays_np(U, V):

        """
    the cross products of two arrays of vector if they have the same length

    Paremeters
        U (list) - first array
        V (list) - second array

    Returns
        numpy array - The cross products
    """

    #transform lists into numpy arrays

    U_np = np.array(U)
    V_np = np.array(V)

    if len(U_np) != len(V_np):
        raise Exception("Arrays don't have the same length")

    return np.cross(U_np, V_np)



if __name__ == '__main__':

    import numpy as np

    a = [
    [0.1, 0.0, 0.1],
    [0.0, 0.0, 0.1],
    [1.0, 0.0, 0.0],
    [1.0, 1.0, 0.0]
    ]

    b =[
    [2.0, 0.3, 0.0],
    [1.0, 0.36, -0.3],
    [1.25, 15.0, 3.0],
    [0.0, -4.0, 7.41]
    ]

    print(cross_two_arrays(a, b))
    print(cross_two_arrays_np(a,b))