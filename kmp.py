text="abxabcabcaby"
pattern1="abcaby"
pattern2="aabaabaaa"
pattern3="cabc"


def prefix(pattern):
    arr1=[0 for i in range(len(pattern))]
    j=1
    i=0
    while(i<j):
        if j>=len(pattern):
            return arr1
        if pattern[i]==pattern[j]:
            arr1[j]=i+1
            i+=1
            j+=1
        else:
            if i==0:
                arr1[j]=0
                i=0
                j+=1
            else:
                i=arr1[i-1]


def kmp(text,pattern,arr1):
    i=0
    j=0
    while(j<=i):
        if text[i]==pattern[j]:
            if j==(len(pattern)-1):
                print "found",pattern[j],text[i]
                return 1
            else:
                i+=1
                j+=1
        else:
            if len(text[i:len(text)])<len(pattern[arr1[j-1]:len(pattern)]):
                print "not found"
                return 0
            else:
                if j==0:
                    j=0
                    i+=1
                else:
                    j=arr1[j-1]

arr1=[]
arr1=prefix(pattern1)
print arr1

val=kmp(text,pattern3,prefix(pattern3))






