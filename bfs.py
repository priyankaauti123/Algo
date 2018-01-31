import itertools as it
vertex=int(input("accept vertex:="))
#adj_matrix=list(it.repeat(list(it.repeat(0,vertex)))
adj_matrix=[[0 for i in range(vertex)]for j in range(vertex)]
print(adj_matrix)


def add_edge(vertex1,vertex2,adj_matrix):
    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix)):
            if i==vertex1 and j==vertex2:
                adj_matrix[i][j]=1
                adj_matrix[j][i]=1
    return adj_matrix
def create_matrix(edges,adj_matrix):
    for i in range(edges):
        ver1=int(input("enter 1st vertex:="))
        ver2=int(input("enter 2nd vertex:="))
        adj_matrix=add_edge(ver1,ver2,adj_matrix)
    return adj_matrix

def check_queue(val,queue):
    for i in range(len(queue)):
        if val==queue[i]:
            return 0
    return 1

def BFS(matrix):
    queue=[]
    queue.append(0)
    for i in range(len(matrix)):
        print queue[i]
        for j in range(len(matrix)):
            if matrix[i][j]!=0:
                if check_queue(j,queue)==0:
                    pass
                else:
                    queue.append(j)

no_of_edges=int(input("how many edges u want:="))
matrix=create_matrix(no_of_edges,adj_matrix)
print matrix
BFS(matrix)

