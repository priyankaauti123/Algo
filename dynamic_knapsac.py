w=[1,3,4,5]
v=[1,4,5,7]
c=7
matrix=[[0 for i in range((c+1))]for j in range(len(w))]
def knapsack(w,v,c,matrix):
    for i in range(len(v)):
        for j in range((c+1)):
            if j==0:
                if w[i]>j:
                    matrix[i][j]=0
                else:
                    matrix[i][j]=w[i]
            else:
                if w[i]>j:
                    matrix[i][j]=matrix[i-1][j]
                else:
                    max_val=(max(matrix[i-1][j],(matrix[i-1][j-w[i]])+v[i]))
                    print max_val
                    matrix[i][j]=max_val
    print matrix

knapsack(w,v,c,matrix)




