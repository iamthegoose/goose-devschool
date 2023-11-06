def towerOfHanoi(a:int) -> int:
    moves = 1
    for i in range(1,a):
       moves = moves * 2 + 1
    return moves
# print(towerOfHanoi(400))