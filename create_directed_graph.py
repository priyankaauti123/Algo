import itertools as it
vertex=int(input("accept vertex:="))
#adj_matrix=list(it.repeat(list(it.repeat(0,vertex)))
adj_matrix=[[0 for i in range(vertex)]for j in range(vertex)]
print(adj_matrix)


def add_edge(vertex1,vertex2,adj_matrix):
    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix)):
            if i==vertex1 and j==vertex2:
                adj_matrix[j][i]=1
    return adj_matrix
def create_matrix(edges,adj_matrix):
    for i in range(edges):
        ver1=int(input("enter 1st vertex:="))
        ver2=int(input("enter 2nd vertex:="))
        adj_matrix=add_edge(ver1,ver2,adj_matrix)
    return adj_matrix

def check_outgoing(matr):
    for i in range(len(matr)):
        if matr[i]==0:
            pass
        else:
            return -1
    return matr

def put_into_0_all(adj_matrix,val):
    for mat in adj_matrix:
        for i in range(len(mat)):
            if i==val:
                mat[i]=0
            else:
                pass
    return adj_matrix

def check_outgoing_edge(adj_matrix):
    for mat in range(len(adj_matrix)):
        val=check_outgoing(adj_matrix[mat])
        if val!=-1:
            adj_matrix[mat]=map(lambda x:-1,adj_matrix[mat])
            adj_matrix=put_into_0_all(adj_matrix,mat)
            return mat

def topological_sort(adj_matrix,topological):
    for i in range(len(topological)):
        val=check_outgoing_edge(adj_matrix)
        topological[i]=val

no_of_edges=int(input("how many edges u want:="))
matrix=create_matrix(no_of_edges,adj_matrix)
print matrix

topological=[0 for i in range(vertex)]
print topological
#sort=[]
topological_sort(matrix,topological)
print topological


