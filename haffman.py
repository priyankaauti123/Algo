list_data1=[5,9,12,13,16,45,4]
print list_data1
list_data=list_data1
list_0=[]
list_1=[]
list_0r=[]
list_1l=[]
list3=[]

def huffman_coding(list_data1):
    list1=list_data1
    while(len(list1)!=1):
        list1.sort()
        val=list1[0]+list1[1]
        list3.append(val)
        list_0.append(0)
        list_1.append(1)
        list_0r.append(list1[0])
        list_1l.append(list1[1])
        list1=list1[1:]
        list1[0]=val
        print list1
#    print list_0
#    print list_1
#    print list_0r
#    print list_1l
#    print list3

def string_search_huffman(list_data):
    list2=[]
    #list1=list_data
    for i in range(len(list_data)):
        string=""
        val=list_data[i]
        val1=0
#        print val
        for j in range(len(list_0r)):
            if val==list3[len(list3)-1]:
                break
            if val==list_0r[j]:
                string+=str(list_0[j])
                val=list3[j]
            else:
                if val==list_1l[j]:
                    string+=str(list_1[j])
                    val=list3[j]
        list2.append(string[::-1])
    print list2


huffman_coding(list_data1)
print list_data1
print list_data
#print list_0
#print list_1
#print list_0r
#print list_1l
#print list3
string_search_huffman(list_data1)




