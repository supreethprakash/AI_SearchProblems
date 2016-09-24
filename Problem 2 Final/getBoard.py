#This File uses functions to read the input text and returns the board

def readContents(fn):
    file = open(fn, mode='r')
    content = [int(i) for i in file.read().replace('\n', ' ').split()]
    return content, len(content)


def getBoardPlacements():
    from tiles import getFileName
    contents = readContents(getFileName())
    return [contents[0][i:i + 4] for i in range(0, len(contents[0]), 4)]
