import collections
import itertools as it
str1="aaadabcdcbabdcdttt"

def check_palindrome(string):
   # print string
    i=0
    j=len(string)-1
    while(i<j+1):
        if string[i]==string[j]:
            i+=1
            j-=1
            pass
        else:
            return 1
    return 0


def longest_palindrome(str1):
    list1=[]
    list2=[]
    string1=""
    for i in range(0,len(str1),1):
        for j in range(i+2,len(str1)+1,1):
            #print str1[i:j]
            string1=""
            val1=0
            val1=check_palindrome(str1[i:j])
            if val1!=1:
                #print str1[i:j]+"####"+string1
                string1+=str1[i:j]
                list1.append(string1)
                list2.append(len(string1))
                #print str1[i:j]+"####"+string1
                #list1[len(string1)]=string1
                #list1.append(string1)
    print list1
    max_val=max(list2)
    print max_val
    list2=list(it.takewhile(lambda x:x!=max_val,list2))
    #print list2
    print list1[max(list2)+1]
    #print list1[max(list1)]
    #list1=collections.OrderedDict(sorted(list1.items()))
    #print dict(list1)



#print check_palindrome("abc")
longest_palindrome(str1)

