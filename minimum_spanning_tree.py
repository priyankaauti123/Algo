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



def find_min_val(matrix,rem_vertex,min_vertex,min_span_tree):
    min_val1=[]
    val1=[]
    val2=[]
    for i in range(len(min_vertex)):
        for j in range(len(rem_vertex)):
            if matrix[min_vertex[i]][rem_vertex[j]]!=0:
                min_val1.append(matrix[min_vertex[i]][rem_vertex[j]])
    print min_val1
    print min_vertex,rem_vertex
    if min_val1!=[]:
        for i in range(len(min_vertex)):
            for j in range(len(rem_vertex)):
                if rem_vertex[j]!=-1:
                    if matrix[min_vertex[i]][rem_vertex[j]]==min(min_val1):
                        matrix[min_vertex[i]][rem_vertex[j]]=0
                        matrix[rem_vertex[j]][min_vertex[i]]=0
                        min_vertex.append(rem_vertex[j])
                        min_span_tree[min_vertex[i]][rem_vertex[j]]=min(min_val1)
                        min_span_tree[rem_vertex[j]][min_vertex[i]]=min(min_val1)
                        rem_vertex[j]=-1
                        return min(min_val1)
    else:
        return 0

def minimum_spanning_tree(matrix):
    min_span_tree=[[0 for i in range(len(matrix))]for j in range(len(matrix))]
    min_weight=[]
    min_vertex=[]
    min_vertex.append(0)
    rem_vertex=[i for i in range(1,len(matrix))]
    #print rem_vertex
    for i in range(len((matrix))-1):
        min_val=find_min_val(matrix,rem_vertex,min_vertex,min_span_tree)
        if min_val!=0:
            min_weight.append(min_val)
        else:
            pass
    print min_weight
    print min_vertex
    print min_span_tree



no_of_edges=int(input("how many edges u want:="))
matrix=create_matrix(no_of_edges,adj_matrix)
print matrix
minimum_spanning_tree(matrix)
