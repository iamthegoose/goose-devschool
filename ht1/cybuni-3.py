def findNb(m:int) -> int:
    n = 0
    while m > 0:
        n+=1
        m-=n**3
    if m == 0:
        return n
    else:
        return -1
# print(findNb(1071225))