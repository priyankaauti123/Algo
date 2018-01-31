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
    return adj_matrix
def create_matrix(edges,adj_matrix):
    for i in range(edges):
        ver1=int(input("enter 1st vertex:="))
        ver2=int(input("enter 2nd vertex:="))
        weight=int(input("enter weight:="))
        adj_matrix=add_edge(ver1,ver2,weight,adj_matrix)
    return adj_matrix


def relax(v1,v2,w,d,p):
    if d[v2]>d[v1]+w:
        d[v2]=d[v1]+w
        p[v2]=v1


def seperate_edges_start_end(matrix,v1,v2,w):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j]!=0:
                v1.append(i)
                v2.append(j)
                w.append(matrix[i][j])
    print v1
    print v2
    print w


def bellman_food(d,p,v1,v2,w):
    d[0]=0
    for i in range(len(d)):
        for j in range(len(v1)):
            relax(v1[j],v2[j],w[j],d,p)
    print d
    print p


def create_shortest_graph(d,p):
    bellman_food=[[-1 for i in range(len(d))]for j in range(len(d))]
    for i in range(len(p)):
        if p[i]!=-1:
            bellman_food[p[i]][i]=d[i]
        else:
            pass
    print bellman_food

no_of_edges=int(input("how many edges u want:="))
matrix=create_matrix(no_of_edges,adj_matrix)
print matrix

d=[len(matrix)+100 for i in range(len(matrix))]
p=[-1 for i in range(len(matrix))]
v1=[]
v2=[]
w=[]
seperate_edges_start_end(matrix,v1,v2,w)
bellman_food(d,p,v1,v2,w)
create_shortest_graph(d,p)



