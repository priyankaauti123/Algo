n1=3
arr=[8,3,1,2]
arr.sort()
#result=[0 for i in range(tot+1)]


def count_coin(coin,n):
    x=[[0 for x in range(n+1)]for x in range(len(coin))]
    for i in range(len(coin)):
        for j in range(n+1):
            x[i][0]=1
    for i in range(len(coin)):
        for j in range(1,n+1):
            if j>=coin[i]:
                x[i][j]=x[i-1][j]+x[i][j-coin[i]]
            else:
                x[i][j]+=x[i-1][j]
    print x
    print(x[len(coin)-1][n])


count_coin(arr,n1)







