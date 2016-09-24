def findPermuatationInv(puzzleBoard):
    sum = 1
    singleList = []

    #Find Zero first
    for row in range(len(puzzleBoard)):
        for col in range(len(puzzleBoard)):
            singleList.append(puzzleBoard[row][col])
            if puzzleBoard[row][col] == 0:
                sum += row

    for i in range(len(singleList)):
        if singleList[i] != 0:
            element = singleList[i]
            for j in range(i+1, len(singleList)):
                if singleList[j] < element and singleList[j] != 0:
                    sum += 1

    return sum % 2
