def highAndLow(inpStr:str):
    hllist = inpStr.split()
    hllist = [int(x) for x in hllist]
    hllist.sort()
    res = str(hllist[-1]) + " " + str(hllist[0])
    return res

# print(highAndLow("8 4 2 1 5"))

