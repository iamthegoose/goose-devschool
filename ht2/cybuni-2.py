def arrOfInt(arrOfInt:list) -> int:
    for i in range(len(arrOfInt)):
        left = sum(arrOfInt[:i])
        right = sum(arrOfInt[i+1:])
        if left == right:
            return i
    return -1
# print(arrOfInt([1,2,3,4,3,2,1]))