v1=[0,0,1,1,2,2,4,6]
v2=[1,2,7,3,3,5,3,5]
var=v1+v2
var=set(var)
print len(var)
matrix=[[0 for i in range(len(var))]for j in range(len(var))]
stack=[i for i in range(len(matrix))]
print stack
#vertex
def create_matrix(v1,v2,matrix):
    for i in range(len(v1)):
        matrix[v1[i]][v2[i]]=1
#        matrix[v2[i]][v1[i]]=1

def find_actor(matrix,stack):
    for i in range(len(stack)):
        val=[]
        val=list(filter(lambda x:x!=0,matrix[i]))
        if val==[]:
            print stack[i]

create_matrix(v1,v2,matrix)
print matrix

find_actor(matrix,stack)

