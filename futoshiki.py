import random

import utils
from utils import getColumn, isWithoutNone




def constraint_different_numbers_in_col_row(board):
    length = len(board)
    # numbers = set([x + 1 for x in range(length)])
    # for i in range(length):
    #     row = board[i]
    #     col = getColumn(board, i)
    #     if isWithoutNone(row) and numbers != set(row):
    #         return False
    #     if isWithoutNone(col) and numbers != set(col):
    #         return False

    for i in range(length):
        for j in range(length):
            for k in range(length):
                if board[i][j] is not None:
                    if k != i and board[i][j] == board[k][j]:
                        return False
                    if k != j and board[i][j] == board[i][k]:
                        return False


    return True




def constraint_greater_lower(board, constraints):
    for constraint in constraints:
        loc1 = constraint[0]
        loc2 = constraint[1]
        if board[loc1[0]][loc1[1]] is not None and board[loc2[0]][loc2[1]] is not None:
            if board[loc1[0]][loc1[1]] <= board[loc2[0]][loc2[1]]:
                return False
    return True



def getNextVar(variables, constraints):
    # print(constraints)
    cons = (item for sublist in constraints for item in sublist)
    for x,y in cons:
        if variables[x][y] is None:
            return x,y
    else:
        return utils.getNextVariableByPosition(variables, 0, -1)



def getNextVal(variables, i, j, domain: set):
    # sprawdzić po przekątnych, wybrać tę której jest najwięcej
    closestValues = utils.getClosestValuesCrossWay(variables, i, j)
    correctValues = []
    for x in range(len(closestValues)):
        if closestValues[x] in domain:
            correctValues.append(closestValues[x])

    if len(correctValues) > 0:
        return correctValues[random.randint(0,len(correctValues)-1)]
    else:
        return random.sample(domain,1).pop()


def getVarDomain(variables, i, j, domain: set):
    varDomain = domain.copy()
    for x in range(len(variables)):
        if x != i and variables[x][j] in varDomain:
            varDomain.remove(variables[x][j])
        if x != j and variables[i][x] in varDomain:
            varDomain.remove(variables[i][x])
    return varDomain


def impose_constraints(domains, variables, i, j):
    valToBeRemoved = variables[i][j]
    # column
    for x in range(len(variables)):
        if valToBeRemoved in domains[x][j] and x != i:
            domains[x][j].remove(valToBeRemoved)
    # row
    for x in range(len(variables)):
        if valToBeRemoved in domains[i][x] and x != j:
            domains[i][x].remove(valToBeRemoved)




# default heuristics

def getNextVarInNormalOrder(variables):
    return utils.getNextVariableByPosition(variables, 0, -1)


def getFirstValFromDomain(variables,x,y, domain):
    return domain[0] if domain else None