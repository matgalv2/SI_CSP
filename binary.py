from random import random, randint, sample

import utils
from utils import isWithoutNone, getColumn, getNextVariableByPosition


def constraint_no_3_in_a_row(board):
    length = len(board)
    if length < 3:
        return True

    for y in range(length):
        for x in range(length):
            row = board[y][x:x + 3]
            if y < length - 2:
                column = [board[y][x], board[y + 1][x], board[y + 2][x]]
                if column == [0, 0, 0] or column == [1, 1, 1]:
                    return False
            if row == [0, 0, 0] or row == [1, 1, 1]:
                return False

    return True


def constraint_unique_row_column(board):
    length = len(board)
    for i in range(length):
        for j in range(i + 1, length):
            if isWithoutNone(board[i]) and isWithoutNone(board[j]):
                if board[i] == board[j]:
                    return False
    # columns
    for i in range(length):
        for j in range(i + 1, length):
            col1 = getColumn(board, i)
            col2 = getColumn(board, j)
            if isWithoutNone(col1) and isWithoutNone(col2):
                if col1 == col2:
                    return False

    return True


def constraint_equal_number_of_0_1(board):
    length = len(board)
    for i in range(length):
        col = getColumn(board, i)
        row = board[i]
        if isWithoutNone(col) and isWithoutNone(row):
            if sum(col) != length / 2 or sum(row) != length / 2:
                return False
    return True


def getNextVar(variables):
    return utils.getNextVariableByPosition(variables, 0, -1)


def getNextVal(variables, i, j, domain: set):
    # sprawdzić po przekątnych, wybrać tę której jest najwięcej
    closestValues = utils.getClosestValuesCrossWay(variables, i, j)
    correctValues = []
    for x in range(len(closestValues)):
        if closestValues[x] in domain:
            correctValues.append(closestValues[x])

    if len(correctValues) > 0:
        return correctValues[randint(0,len(correctValues)-1)]
    else:
        return sample(domain,1).pop()


def getVarDomain(variables, i, j, domain: set):
    varDomain = domain.copy()
    values = []
    if i - 2 >= 0:
        values.append([variables[i-2][j], variables[i-1][j]])
    if i + 2 <= len(variables) - 1:
        values.append([variables[i+1][j], variables[i+2][j]])
    if j - 2 >= 0:
        values.append(variables[i][j-2:j])
    if j + 2 <= len(variables) - 1:
        values.append(variables[i][j:j+2])

    for value in values:
        if value[0] == value[1] and value[0] in varDomain:
            varDomain.remove(value[0])

    return varDomain



def getClosestPositionsVertHori(variables, i, j):
    column = []
    for x in range(len(variables)):
        if i - 2 <= x <= i + 2:
            column.append((x,j))

    row = []
    for y in range(len(variables)):
        if j - 2 <= y <= j + 2:
            row.append((i,y))

    return column, row


def impose_constraints(domains, variables, i, j):
    column, row = getClosestPositionsVertHori(variables, i, j)

    for x in range(len(column)-2):
        index_fst = column[x][0]
        index_snd = column[x][1]

        first = variables[index_fst][index_snd]
        second = variables[index_fst+1][index_snd]
        third = variables[index_fst+2][index_snd]

        if first == second:
            if first in domains[index_fst+2][index_snd]:
                domains[index_fst + 2][index_snd].remove(first)
        elif first == third:
            if first in domains[index_fst+1][index_snd]:
                domains[index_fst + 1][index_snd].remove(first)
        elif second == third:
            if second in domains[index_fst][index_snd]:
                domains[index_fst][index_snd].remove(second)


    for x in range(len(row)-2):
        index_fst = row[x][0]
        index_snd = row[x][1]

        first = variables[index_fst][index_snd]
        second = variables[index_fst][index_snd+1]
        third = variables[index_fst][index_snd+2]

        if first == second:
            if first in domains[index_fst][index_snd+2]:
                domains[index_fst][index_snd+2].remove(first)
        elif first == third:
            if first in domains[index_fst][index_snd+1]:
                domains[index_fst][index_snd+1].remove(first)
        elif second == third:
            if second in domains[index_fst][index_snd]:
                domains[index_fst][index_snd].remove(second)





# default heuristics

def getRandomVar(variables, indexes=[]):
    # randomIndex = randint(0,len(variables)**2 - 1)
    if not indexes:
        indexes = [i for i in range(len(variables)**2)]
    randomIndex = indexes[randint(0,len(indexes)-1)]
    first = randomIndex // len(variables)
    second = randomIndex % len(variables)
    tmp = variables[first][second]

    indexes.remove(randomIndex)

    while tmp is not None:
        randomIndex = indexes[randint(0, len(indexes)-1)]
        first = randomIndex // len(variables)
        second = randomIndex % len(variables)
        tmp = variables[first][second]

        indexes.remove(randomIndex)

    return first, second



def getFirstValFromDomain(variables,x,y, domain):
    return domain[0] if domain else None