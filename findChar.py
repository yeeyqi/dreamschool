def findNum(st,k):
    n=len(st)
    numNewList=''
    checkList=''
    for i in range(n):
        if st[i] in checkList:
            numNewList+="-"
        else:
            numNewList+=st[i]
        checkList+=st[i]
        if i>int(k):
            checkList=checkList[1:k+1]
        
    return numNewList
  
inputList,k=map(str,input().split(" "))
print(findNum(inputList,int(k)))