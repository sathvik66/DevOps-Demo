def merge_sort(l):
    if(len(l)==1):
        return
    m=len(l)//2
    l1=l[:m]
    l2=l[m:]
    merge_sort(l1)
    merge_sort(l2)
    i=j=k=0
    while(i<len(l1) and j<len(l2)):
        if(l1[i]<=l2[j]):
            l[k]=l1[i]
            i+=1
        else:
            l[k]=l2[j]
            j+=1
        k+=1
    while(i<len(l1)):
        l[k]=l1[i]
        i+=1
        k+=1
    while(j<len(l2)):
        l[k]=l2[j]
        j+=1
        k+=1

l=[9,83,76,61,52,41,3,2,1]
merge_sort(l)
print(l)
