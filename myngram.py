def ngram_hemal1(s1):  
    s3 = s1.lower()
    s2 = s3.split()
    len1 = len(s2)
    list4= []
    print s2
    print s3
    list3 = ['python', 'java','c#', 'c++', 'angularjs', 'object oriented']
    i=0
    #list4 = [i for i, j in zip(s2, list3) if i == j]
    for i in range(1, len1):
            if len1>=0:
                s4 = s2[i -1 ]+' '+ s2[i]
                s2.append(s4)
                #print s2
                  
    print len(s2)
    for j in range(len(s2)):
        if s2[j] in list3 and s2[j] not in list4:
            list4.append(s2[j])
        
    return '\n '.join(list4)  #return list4

  