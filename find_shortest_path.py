import itertools as it
vertex=int(input("accept vertex:="))
#adj_matrix=list(it.repeat(list(it.repeat(0,vertex)))
adj_matrix=[[0 for i in range(vertex)]for j in range(vertex)]
print(adj_matrix)


def add_edge(vertex1,vertex2,weight,adj_matrix):
    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix)):
            if i==vertex1 and j==vertex2:
                adj_matrix[i][j]=weight
                adj_matrix[j][i]=weight
    return adj_matrix
def create_matrix(edges,adj_matrix):
    for i in range(edges):
        ver1=int(input("enter 1st vertex:="))
        ver2=int(input("enter 2nd vertex:="))
        weight=int(input("Enter weight:="))
        adj_matrix=add_edge(ver1,ver2,weight,adj_matrix)
    return adj_matrix

def check_spanning(val,mat1):
    for i in range(len(mat1)):
        if val==mat1[i]:
            pass
        else:
            mat1[i]=0
    return mat1



def find_min_spanning_tree(adj_matrix):
    mat=[]
    min_mat=[]
    for mat1 in adj_matrix:
        mat=filter(lambda x:x!=0,mat1)
        val=min(mat)
        mat1=check_spanning(val,mat1)
        min_mat.append(mat1)
    return min_mat




no_of_edges=int(input("how many edges u want:="))
matrix=create_matrix(no_of_edges,adj_matrix)
print matrix
min_matrix=find_min_spanning_tree(matrix)
print min_matrix





