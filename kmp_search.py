text="abxabcabcaby"
pattern1="abcaby"
pattern2="aabaabaaa"
pattern3="cabc"


def prefix(pattern):
    prefix_arr=[0 for i in range(len(pattern))]
    prefix_arr[0]=0
    i=0
    j=1
    while(j>=i and j<len(pattern)):
        if pattern[i]==pattern[j]:
            prefix_arr[j]=i+1
            j+=1
            i+=1
        else:
            if i==0:
                i=0
                j+=1
            else:
                i=prefix_arr[i-1]
    return prefix_arr


def kmp_search(text,pattern,prefix_arr):
    i=0
    j=0
    while(j<=i):
        if pattern[j]==text[i]:
            if j==len(pattern)-1:
                print "found"
                return 0
            else:
                i+=1
                j+=1
        else:
            if len(pattern[j:])>len(text[i:]):
                print "not found"
                return 1
            if j==0:
                j=0
                i+=1
            else:
                j=prefix_arr[j-1]



prefix_arr=prefix(pattern3)
print prefix_arr
val=kmp_search(text,pattern3,prefix_arr)

