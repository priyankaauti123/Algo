
AT=[10,11,10.15,10.10]
DT=[10.30,12,11.15,12.30]
AT.sort()
DT.sort()
AT_DT=AT+DT
print AT_DT
AT_DT.sort()
print AT_DT


def count_platform(AT,AT_DT,DT):
    AT1=AT
    cnt1=0
    cnt2=0
    print AT1
    j=0
    k=0
    for i in range(len(AT_DT)):
        if AT1==[]:
            return(len(DT))
        else:
            print AT1,AT_DT,DT
            if AT_DT[i] in AT1:
                j+=1
                AT1=AT1[j:]
            else:
                if AT_DT[i] in DT:
                    k+=1
                    DT=DT[k:]

no=count_platform(AT,AT_DT,DT)
print no


