n=51

def count_coin(n):
    sol=0;
    if n==0:
        return 0
    sol1=1+count_coin(n-1)
    sol=sol1
    if n>=29:
        sol2=1+count_coin(n-29)
        sol=min(sol1,sol2)
    if n>=50:
        sol3=1+count_coin(n-50)
        sol=min(sol3,sol)
    #print sol1,sol2,sol3
    return sol

solution=count_coin(n)
print solution


