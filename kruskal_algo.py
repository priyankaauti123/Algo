no=input("no of vertex:=")
start=[]
end=[]
weight=[]

def matrix(start,end,weight,n):
    for i in range(n):
        start.append(input("vertex1:="))
        end.append(input("vertex2:="))
        weight.append(input("weight:="))

def sort_according_weight(start,end,weight):
    for i in range(len(start)):
        temp=0
        for j in range(0,i):
            if weight[i]<weight[j]:
                temp=weight[i]
                weight[i]=weight[j]
                weight[j]=temp

                temp=start[i]
                start[i]=start[j]
                start[j]=temp

                temp=end[i]
                end[i]=end[j]
                end[j]=temp


def kruskal(start,end,weight):
    matrix=[[0 for i in range(len(start))]for j in range(len(start))]
    list1=[]
    list1.append(start[0])
    list1.append(end[1])
    matrix[list1[0]][list1[1]]=weight[0]
    matrix[list1[1]][list1[0]]=weight[0]
    start=start[1:]
    end=end[1:]
    weight=weight[1:]
    for i in range(len(weight)):
        if (start[i] in list1) and (end[i] in list1):
            pass
        else:
            matrix[start[i]][end[i]]=weight[i]
            matrix[end[i]][start[i]]=weight[i]
            list1.append(start[i])
            list1.append(end[i])
    return matrix

matrix(start,end,weight,no)
print start
print end

sort_according_weight(start,end,weight)
print weight

matrix=kruskal(start,end,weight)
print matrix


