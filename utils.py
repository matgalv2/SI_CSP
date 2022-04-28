from random import *


def sumNumbers(iterable):
    newIterable = []
    for x in iterable:
        if x is not None:
            newIterable.append(x)
    return sum(newIterable)


def isWithoutNone(iterable):
    return None not in iterable


def getColumn(board, columnNo):
    return list(map(lambda x: x[columnNo], board))


def hasUnassignedVariables(board):
    for y in board:
        if None in y:
            return True


def getRandomVariable(board):
    emptyCells = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] is None:
                emptyCells.append((i, j))
    return emptyCells[randint(0, len(emptyCells) - 1)]


def getNextVariableByPosition(board, y, x):
    """
    :param board: 2-d list
    :param y: first index
    :param x: second index
    :return:
    """

    if hasUnassignedVariables(board):
        nextPosition = y * len(board[y]) + x + 1
        indices = nextPosition // len(board), nextPosition % len(board[y])
        if board[indices[0]][indices[1]] is not None:
            return getNextVariableByPosition(board, indices[0], indices[1])
        else:
            return indices
    else:
        return None


def getBinaryBoardFromFile(filename):
    with open(filename, 'r') as file:
        newBoard = []
        for line in file:
            row = []
            for i in line:
                if str(i) != '\n':
                    if str(i).isdigit():
                        row.append(int(i))
                    else:
                        row.append(None)
            newBoard.append(row)
        return newBoard


def getFutoshikiBoardFromFile(filename):
    with open(filename, 'r') as file:
        newBoard = []
        constraints = []
        i = 0
        k = 0
        for line in file:
            row = []
            l = 0
            for j in range(len(line)):
                if i % 2 == 0:
                    if line[j] == 'x':
                        row.append(None)
                    elif line[j].isdigit():
                        row.append(int(line[j]))
                    elif line[j] == '>':
                        constraints.append(((k, l - 1), (k, l)))
                    elif line[j] == '<':
                        constraints.append(((k, l), (k, l - 1)))
                    if j % 2 == 0:
                        l += 1

                else:
                    if line[j] == '>':
                        constraints.append(((k - 1, l), (k, l)))
                    elif line[j] == '<':
                        constraints.append(((k, l), (k - 1, l)))
                    l += 1

            if i % 2 == 0:
                newBoard.append(row)
                k += 1
            i += 1
    return newBoard, constraints


def getClosestValuesPlusWay(variables, i, j):
    values = set()
    if i -1 >= 0 and variables[i-1][j] is not None:
        values.add(variables[i-1][j])
    if i+1 < len(variables) and variables[i+1][j] is not None:
        values.add(variables[i+1][j])
    if j -1 >= 0 and variables[i][j-1] is not None:
        values.add(variables[i][j-1])
    if j+1 < len(variables) and variables[i][j+1] is not None:
        values.add(variables[i][j+1])

    return values


def getClosestValuesCrossWay(variables, i, j):
    values = []
    if i -1 >= 0 and j - 1 and variables[i-1][j-1] is not None:
        values.append(variables[i-1][j-1])
    if i+1 < len(variables) and j+1 < len(variables) and variables[i+1][j] is not None:
        values.append(variables[i+1][j+1])
    if j -1 >= 0 and i+1 < len(variables) and variables[i+1][j-1] is not None:
        values.append(variables[i+1][j-1])
    if j+1 < len(variables) and i-1 >= 0 and variables[i-1][j+1] is not None:
        values.append(variables[i-1][j+1])

    return values



def saveResults(filename, *args):
    with open(filename, 'a') as file:
        for arg in args:
            file.write(str(arg) + '\t')
        file.write("\n")



