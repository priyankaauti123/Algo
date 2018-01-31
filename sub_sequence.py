import numpy as np
list1=[19,9,7,5,13,5,17,2,8,10,19]
list2=[1,1,1,1,1,1,1,1,1,1,1]
N=len(list1)
for i in range(1,N,1):
    arr2=[0]
    for j in range(i-1,0,-1):
        if list1[i]>list1[j]:
            arr2.append(list2[j])
        else:
            pass

    max_value=max(arr2);
    list2[i]=max_value+1
    print arr2
print list2
