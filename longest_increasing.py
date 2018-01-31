arr=[10,22,9,33,21,50,41,60]
longest_inc=[1 for i in range(len(arr))]
longest_dec=[1 for i in range(len(arr))]
print arr
def longest_increasing(arr,longest_inc):
    for i in range(len(arr)):
        for j in range(0,i):
            if arr[i]>arr[j] and longest_inc[i]<longest_inc[j]+1:
                longest_inc[i]=longest_inc[j]+1
            else:
                pass
    print longest_inc

def longest_decreasing(arr,longest_dec):
    for i in range(len(arr)):
        for j in range(0,i):
            if arr[i]<arr[j] and longest_dec[i]<longest_dec[j]+1:
                longest_dec[i]=longest_dec[j]+1
                print arr[i],arr[j]
            else:
                pass
    print longest_dec


longest_increasing(arr,longest_inc)
longest_decreasing(arr,longest_dec)

