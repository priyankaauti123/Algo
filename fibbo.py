N=int(input("enter no:"))
list1=[1]
for i in range(N):
    if i==0:
        list1.append(list1[i-1])
    else:
        list1.append(list1[i-2]+list1[i-1])
print list1
