input_data=["POON","PLEE","SAME","POLE","POIE","PLEA","PLIE","POIN"]
start="TOON"
target="ZZZZ"


def search_start_with_arr(start,target,input_data,count):
    j=0
    #print start
    for word in input_data:
        cnt=0
        j+=1
        for letter in range(len(word)):
            if word[letter]==start[letter]:
                cnt+=1
            else:
                pass
        if cnt>=3:
            count+=1
            start=word
            input_data[j-1]=""
            print start
            if start==target:
       #         count+=1
               # print start,target,count
                print count
                return
            search_start_with_arr(start,target,input_data,count)
        else:
            pass
    print "combination no"
    return

count=1
search_start_with_arr(start,target,input_data,count)
#print count

