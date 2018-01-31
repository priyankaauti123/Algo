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
    return adj_matrix
def create_matrix(edges,adj_matrix):
    for i in range(edges):
        ver1=int(input("enter 1st vertex:="))
        ver2=int(input("enter 2nd vertex:="))
        adj_matrix=add_edge(ver1,ver2,adj_matrix)
    return adj_matrix

def find_actors_from_party(matrix,stack_arr,j):
    if j==(len(stack_arr)):
        return
    else:
        #print stack_arr[j]
        filter_data=[]
        filter_data=filter(lambda x:x!=0,matrix[stack_arr[j]][0:len(matrix)])
        #print filter_data
        if filter_data==[]:
            print stack_arr[j]
            find_actors_from_party(matrix,stack_arr,j+1)
        else:
            find_actors_from_party(matrix,stack_arr,j+1)
        #print stack_arr[j]
        #find_actors_from_party(matrix,stack_arr,j+1)

#stack_arr=[i for i in range(len(matrix))]
no_of_edges=int(input("how many edges u want:="))
matrix=create_matrix(no_of_edges,adj_matrix)
print matrix

stack_arr=[i for i in range(len(matrix))]
find_actors_from_party(matrix,stack_arr,0)



