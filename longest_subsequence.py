import numpy as np
list2=[]

list2=[input("enter no:") for i in range(8)]
print list2
#longest_subseq=[1 for i in range]


def longest_subsequence(input_data,ans_arr):
    for i in range(1,len(input_data)):
        val=1
        for j in range(0,i):
            if input_data[i]>input_data[j]:
                if ans_arr[i]<ans_arr[j]:
                    val=ans_arr[j]
                    val+=1
                else:
                    if val==ans_arr[j]:
                        val+=1
            else:
                pass
        val-=1
        ans_arr[i]+=val
    print ans_arr


def longest_decreasing(input_data,ans_arr):
    for i in range(1,len(input_data)):
        val=1
        for j in range(0,i):
            if input_data[i]<input_data[j]:
                if val<ans_arr[j]:
                    val=ans_arr[j]
                    val+=1
                else:
                    if val==ans_arr[j]:
                        val+=1
            else:
                pass
        val-=1
        ans_arr[i]+=val
    print ans_arr


def bitonic_subsequence(longest_inc,list2,val):
    for i in range(len(longest_inc)):
        if longest_inc[i]==val:
            k=i
    print k
    print list2[k:]
    data=[1 for i in range(len(list2[k:]))]
    longest_decreasing(list2[k:],data)


longest_subseq=[1 for i in range(len(list2))]
longest_dec=[1 for i in range(len(list2))]
longest_subsequence(list2,longest_subseq)
longest_decreasing(list2,longest_dec)
max_val=max(longest_subseq)
bitonic_seq=bitonic_subsequence(longest_subseq,list2,max_val)



