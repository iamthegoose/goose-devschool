def rearA(inpRear: int) -> str:
    if inpRear < 0:
        raise ValueError("Число не може бути від'ємним")
    rearList = list(str(inpRear))
    rearList.sort(reverse=True)
    res = ''.join(map(str, rearList))  
    return res
print(rearA(1215004))





