input=str(input("Enter string:="))
print input
output=list(0 for i in range(len(input)))
print output

def length_longest_palindrome_sublist(input,output):
    for i in range(len(input)):
        cnt=1
        if len(input)==1:
            output[i]=1
            return
        else:
            #print input[i-1],input[i],input[i+1]
            if i+1!=len(input):
                if input[i-1]==input[i+1]:
                    cnt=1
                    j=i-1
                    k=i+1
                    while(j>=0 and k<len(input)):
                        if input[k]==input[j]:
                            cnt+=2
                            print "**"+input[k],input[j],cnt
                            j-=1
                            k+=1
                        else:
                            #cnt+=2
                            print output[i]
                            output[i]=cnt
                            j=-1
                            k=len(input)
                    output[i]=cnt
                else:
                    if input[i-1]==input[i]:
                        j=i-1
                        k=i
                        cnt=0
                        while(j>=0 and k<len(input)):
                            if input[j]==input[k]:
                                cnt+=2
                                print "++"+input[k],input[j],cnt
                                j-=1
                                k+=1
                            else:
                                print output[i]
                                output[i]=cnt
                                j=-1
                                k=len(input)
                        output[i]=cnt
                        print output[i]
                    else:
                        if input[i+1]==input[i]:
                            j=i+1
                            k=i
                            cnt=1
                            while(j<len(input)):
                                if input[j]==input[k]:
                                    cnt+=1
                                    print "+=+"+input[k],cnt
                                    j+=1
                                else:
                                    j=len(input)
                            output[i]=cnt
                        else:
                            output[i]=1
            else:
                output[i]=1
    print output

length_longest_palindrome_sublist(input,output)

