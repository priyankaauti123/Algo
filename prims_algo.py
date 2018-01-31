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
        weight=int(input("enter weight:="))
        adj_matrix=add_edge(ver1,ver2,weight,adj_matrix)
    return adj_matrix


def remove_selfloop(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i==j:
                if matrix[i][j]!=0:
                    matrix[i][j]=0
                    matrix[j][i]=0


def find_min_val(min_val,v1,v2,matrix,matrix1):
    arr1=filter(lambda x:x!=0 and x!=min_val,matrix[v2][0:len(matrix)])
    print arr1
    min_val=min(arr1)
    print min_val
    for j in range(len(matrix)):
        if matrix[v2][j]==min_val:
            print min_val,v1,v2
            v1=v2
            v2=j
            matrix1[v1][v2]=min_val

def add_into_matrix1(matrix1,v1,v2,min_val):
    matrix1[v1][v2]=min_val

def prims_algo(matrix):
    remove_selfloop(matrix)
    matrix1=[[0 for i in range(len(matrix))]for j in range(len(matrix))]
    arr1=filter(lambda x:x!=0,matrix[0][0:len(matrix)])
    min_val=min(arr1)
    for i in range(len(matrix)):
        if matrix[0][i]==min_val:
            v1=0
            v2=i
            matrix1[v1][v2]=min_val
    for i in range(1,len(matrix)):
        arr1=filter(lambda x:x!=0 and x!=min_val,matrix[v2][0:len(matrix)])
        min_val=min(arr1)
        for j in range(len(matrix)):
            if matrix[v2][j]==min_val:
                v1=v2
                v2=j
                matrix1[v1][v2]=min_val
    print matrix1



no_of_edges=int(input("how many edges u want:="))
matrix=create_matrix(no_of_edges,adj_matrix)
print matrix

prims_algo(matrix)




