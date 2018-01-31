input_array=[]
num=int(input("how many elements u want"))
input_array=[int(input("Enter no:=")) for i in range(num)]
print input_array


def check_last_occurence(input_array,m,k):
    for i in range(len(input_array)-1,m,-1):
        if input_array[i]==k:
            return i
    return 0

def check_first_occurence(input_array,m,k):
    for i in range(0,m,1):
        if input_array[i]==k:
            return i-1
    return 0

def count_k_value(input_array):
    n=len(input_array)
    cnt=0
    m=n//2
    print m
    k=3
    if input_array[m]==k:
        if input_array[m+1]==k:
            val1=check_last_occurence(input_array,m,k)
            val2=check_first_occurence(input_array,m,k)
            #print val1
            #print val2
            print int(val1)-int(val2)
        else:
            val1=check_first_occurence(input_array,m,k)
            print m-val1
    else:
        if input_array[m]>k:
            for j in range(0,m):
                if input_array[j]==k:
                    cnt+=1
            print cnt
        else:
            for j in range(m,len(input_array)):
                if input_array[j]==k:
                    cnt+=1
            print cnt

count_k_value(input_array)


