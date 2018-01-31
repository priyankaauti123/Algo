profit=[100,19,27,25,15]
deadline=[2,1,2,1,3]

def job_selection(profit,deadline,select):
    n=len(profit)
    for i in range(n):
        val=max(profit)
        print val
        dead_line=search_deadline(val,profit,deadline)
        select=put_into_select(dead_line,val,select)
        print select

def put_into_select(dead_line,val,select):
    for i in range(dead_line):
        if select[(dead_line-1)-i]==0:
            select[(dead_line-1)-i]=val
            return select
    return select

def search_deadline(val,profit,deadline):
    for i in range(len(profit)):
        if val==profit[i]:
            profit[i]=0
            return deadline[i]



max_deadline=max(deadline)
select=[0 for i in range(max_deadline)]
print select
job_selection(profit,deadline,select)
print sum(select)


