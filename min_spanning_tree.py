import itertools as it
vertex=int(input("accept vertex:="))
#adj_matrix=list(it.repeat(list(it.repeat(0,vertex)))
adj_matrix=[[0 for i in range(vertex)]for j in range(vertex)]
print(adj_matrix)


def add_edge(vertex1,vertex2,adj_matrix,weight):
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
        weight=int(input("enter weight for vertex {} to vertex {}".format(ver1,ver2)))
        adj_matrix=add_edge(ver1,ver2,adj_matrix,weight)
    return adj_matrix


def check_reached_vertex(vertex1,min_val_weight,matrix1,rem_vertex):
    for i in range(len(matrix1)):
        if matrix1[i]==min_val_weight:
            matrix1[i]=0
            rem_vertex[i]=-1
            return i

def count(arr1):
    cnt=0
    for i in arr1:
        cnt+=1
    return cnt

def find_min_val(matrix,rem_vertex,min_vertex,matrix_span_tree):
    min_val=0
    min_val1=[]
    for i in range(len(min_vertex)):
        for j in range(len(rem_vertex)):
            if matrix[min_vertex[i]][rem_vertex[j]]!=0:
                min_val1.append(matrix[min_vertex[i]][rem_vertex[j]])
    #print min(min_val1)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j]==min(min_val1):
                matrix[i][j]=0
                matrix[j][i]=0
                if matrix[i][j]==0:
                    matrix_span_tree[i][j]=min(min_val1)
                    matrix_span_tree[j][i]=min(min_val1)
                    return min(min_val1)
    return min(min_val1)



def minimum_spanning_tree(matrix):
    matrix_span_tree=[[0 for i in range(len(matrix))]for j in range(len(matrix))]
    #print matrix_span_tree
    min_weight=[]
    min_vertex=[]
    rem_vertex=[]
    for i in range(len(matrix)):
        rem_vertex.append(i)
    min_vertex.append(0)
    rem_vertex[0]=-1
    for i in range(len(rem_vertex)):
        if rem_vertex[i]!=-1:
            min_val=find_min_val(matrix,rem_vertex,min_vertex,matrix_span_tree)
            if min_val!=0:
                min_weight.append(min_val)
                min_vertex.append(rem_vertex[i])
                rem_vertex[i]=-1
    print matrix_span_tree
    #print rem_vertex
    #print min_vertex
    print min_weight





no_of_edges=int(input("how many edges u want:="))
matrix=create_matrix(no_of_edges,adj_matrix)
print matrix
minimum_spanning_tree(matrix)
