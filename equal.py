n1=input("no of colleagues:")
#n2=input("no of input:")

#arr=[1,3,3,9]

def equal_find(arr,cnt):
    min_val=min(arr)
    max_val=max(arr)
    diff=max_val-min_val
    if diff==0:
        print cnt
        return
    if diff==1:
        cnt+=1
        for i in range(len(arr)):
            if max_val==arr[i]:
                pass
            else:
                arr[i]+=1
        equal_find(arr,cnt)
    if diff<5 and diff>1:
        cnt+=1
        for i in range(len(arr)):
            if max_val==arr[i]:
                pass
            else:
                arr[i]+=2
        equal_find(arr,cnt)
    if diff>=5:
        cnt+=1
        for i in range(len(arr)):
            if max_val==arr[i]:
                pass
            else:
                arr[i]+=5
        equal_find(arr,cnt)

for i in range(n1):
    n2=input("enter no:")
    arr=list(map(lambda x:input("Enter arr:="),range(n2)))
    cnt=0
    equal_find(arr,cnt)

