#sort weight according to finish time
#1 select 1st activity
#2 check start time of next activity is greater than selected previous finish time then print this activity again process





weight=[4,5,10,1,6,9,11,2,3,7,8]
start_finish=[(2.3,3),(3.2,4),(4.3,5),(0,2),(2.3,3.8),(4,4.6),(4.6,6),(0,1),(1.5,3),(3,3.8),(4,5)]
start_time=[2.3,3.2,4.3,0,2.3,4,4.6,0,1.5,3,4]
finish_time=[3,4,5,2,3.8,4.6,6,1,3,3.8,5]
#print len(weight),len(finish_time)


def sort_activities_according_to_finish_time(weight,finish_time,start_time):
    for i in range(len(finish_time)):
        for j in range(0,len(finish_time)-1):
            if finish_time[j]>finish_time[j+1]:
                temp=finish_time[j]
                finish_time[j]=finish_time[j+1]
                finish_time[j+1]=temp

                temp=weight[j]
                weight[j]=weight[j+1]
                weight[j+1]=temp

                temp=start_time[j]
                start_time[j]=start_time[j+1]
                start_time[j+1]=temp
            else:
                pass


def find_more_selection_activities(weight,finish_time,start_time):
    selected_activities=[]
    val=weight[0]
    selected_activities.append(val)
    f_time=finish_time[0]
    print val
    for i in range(1,len(start_time)):
        if start_time[i]>f_time:
            print weight[i]
            selected_activities.append(weight[i])
            f_time=finish_time[i]
        else:
            pass
    print selected_activities
    #return selected_activities



activity=[]
sort_activities_according_to_finish_time(weight,finish_time,start_time)
actvity=find_more_selection_activities(weight,finish_time,start_time)
#print activity






