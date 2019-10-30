
# Task 4: Using faces.obj, Define a function for traversing the mesh from boundary to boundary in a "straight" line and Visualise the result   

__author__ = "Cristián Calvo Barentin"
__email__ = "calvo@arch.ethz.ch"
__date__ = "30.10.2019"

def get_traverse_path(start, mesh):
    
    """
    Traverse path in mesh from boundary to boundary

    Parameters
        start (integer) - starting vertex key
        mesh (compas.datastructure.Mesh) - Mesh

    Returns
        vertices - list of int, vertex keys for the traverse path
        edges - list of tuples, edge keys for the traverse path
    """
    #check if given starting vertex is in the boundary

    if start not in mesh.vertices_on_boundary(ordered=False):
       raise Exception("Vertex not in the boundary")
    
    vertices = [start]
    edges = []
    current_vertex = start

    #find neighbor vertex that is not in the boundary
    for vkey in mesh.vertex_neighbors(start):
        if mesh.is_vertex_on_boundary(vkey) == False:
            prev_vertex = current_vertex
            current_vertex = vkey
            edges.append([prev_vertex, current_vertex])

    #find neighbor vertex that is opposite to previous vertex
    while current_vertex not in mesh.vertices_on_boundary(ordered=False):
        vertices.append(current_vertex)
        nbrs_vertices = mesh.vertex_neighbors(current_vertex, ordered=True)
        prev_vert_i = nbrs_vertices.index(prev_vertex)
        prev_vertex = current_vertex
        current_vertex = nbrs_vertices[prev_vert_i - 2]
        edges.append([prev_vertex, current_vertex]) 

    #Append final boundary vertex    
    vertices.append(current_vertex)

    return vertices, edges




if __name__ == '__main__':

    import os
    from compas.datastructures import Mesh
    from compas_plotters import MeshPlotter


    HERE = os.path.dirname(__file__)
    HEAD = os.path.split(HERE)[0]
    DATA = os.path.join(HEAD, 'ITA19', 'modules', 'module0','02_datastructures_and_geometry','data')
    FILE = os.path.join(DATA, 'faces.obj')

    mesh = Mesh.from_obj(FILE)

    starting_vertex= 34

    path_v, path_e = get_traverse_path(starting_vertex, mesh)

    edges = []

    #check if edge key exist in datastructure, if not flip the order of vertex keys
    for e in path_e:
        if e not in mesh.edges():
            u,v = e[1], e[0]
        else:
            u,v = e[0], e[1]
        edges.append([u,v])

    plotter = MeshPlotter(mesh, figsize=(16, 10))

    plotter.draw_vertices(
        facecolor={key: (255, 0, 0) for key in path_v},
        text={key: str(key) for key in mesh.vertices()},
        radius=0.2)    
    plotter.draw_edges(
        color={(u,v):(255, 0, 0)  for u,v in edges},
    )
    plotter.draw_faces()
    plotter.show()
