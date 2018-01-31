input_str=str(input("Enter input letter:="))
pattern=str(input("Enter pattern:="))

transition_table=[[0 for i in range(len(input_str))]for j in range(len(pattern)+1)]
print pattern
print input_str
print transition_table



def put_into_transition_table1(transition_table1,i1,j1):
    transition_table1[j1]=i1+1
    return transition_table1

def suffix_prefix(str1,str2):
    if len(str1)==0 or str1==[]:
        return 0
    else:
        n1=len(str1)
        if str1[n1-1]==str2[n1-1]:
            return n1-1
        else:
            if n1%2==0:
                str1=[str1[x] for x in range(len(str1)-1)]
                str2=[str2[x] for x in range(len(str2)-1)]
                print str1,str2,len(str1)
                suffix_prefix(str1,str2)

def finite_automata_transition_table(input_str,pattern,transition_table):
    str1=""
    str2=""
    transition_tab=transition_table
    for i in range(len(transition_table)):
        '''
        if i==0:
            for j in range(len(input_str)):
                if input_str[j]==pattern[i]:
                    transition_table[i]=put_into_transition_table1(transition_table[i],i,j)
                    pass
        else:'''
        if i>=0 and i<len(pattern):
            for j in range(len(input_str)):
                if input_str[j]==pattern[i]:
                    str2+=pattern[i-1]
                    str1+=pattern[i]
                    transition_table[i]=put_into_transition_table1(transition_table[i],i,j)
                else:
                    print str2,str1
                    num=suffix_prefix(str2,str1)
                    print num,str2,str1
        else:
            for j in range(len(input_str)):
                if pattern[0]==pattern[len(pattern)-1]==input_str[j]:
                    transition_table[i]=put_into_transition_table1(transition_table[i],0,j)
                else:
                    pass
    print transition_table


finite_automata_transition_table(input_str,pattern,transition_table)


