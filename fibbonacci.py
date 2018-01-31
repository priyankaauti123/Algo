t1=0
t2=1
n=9
result=[0 for i in range(n)]
print(result)
result[0]+=t1
result[1]+=t2
for i in range(2,len(result)):
    t3=t1+(t2*t2)
    result[i]+=t3
    t1=result[i-1]
    t2=result[i]
print result
print(result[n-1])


