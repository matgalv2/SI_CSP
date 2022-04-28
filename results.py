import binary
from functools import partial

import futoshiki
import utils
from csp import Puzzle
from utils import getBinaryBoardFromFile, getFutoshikiBoardFromFile



# part 1
# binary


getNextVarHeuristics = {binary.getNextVar : "Next var in normal order", binary.getRandomVar: "Random var"}
getNextValHeuristics = {binary.getNextVal : "By diagonal, get random", binary.getFirstValFromDomain: "First from domain"}

#
# binary_cons = [binary.constraint_no_3_in_a_row, binary.constraint_unique_row_column, binary.constraint_equal_number_of_0_1]
# for filename in ["binary_6x6", "binary_8x8", "binary_10x10"]:
#     for getNextVar in [binary.getNextVar, binary.getRandomVar]:
#         for getNextVal in [binary.getNextVal, binary.getFirstValFromDomain]:
#             c1 = getBinaryBoardFromFile("./data/" + filename)
#             case = Puzzle(c1, [0,1], binary_cons)
#             duration, cases = case.solveForwardChecking(getNextVar,getNextVal, binary.impose_constraints)
#             utils.saveResults("./results/part1_one_solution/" + filename, duration, cases, getNextVarHeuristics[getNextVar], getNextValHeuristics[getNextVal])

#
# lazy_getNextVar = partial(futoshiki.getNextVar)
#
# getNextVarHeuristics = {lazy_getNextVar : "First > || <", futoshiki.getNextVarInNormalOrder: "Normal order"}
# getNextValHeuristics = {futoshiki.getNextVal : "By diagonal, get random", futoshiki.getFirstValFromDomain: "First from domain"}
#
# lazy_cons = partial(futoshiki.constraint_greater_lower)
#
# futoshiki_cons = [futoshiki.constraint_different_numbers_in_col_row, lazy_cons]



# for filename in ["futoshiki_4x4", "futoshiki_5x5", "futoshiki_6x6"]:
#     c2, additionalCons = utils.getFutoshikiBoardFromFile("./data/" + filename)
#     lazy_getNextVar.keywords["constraints"] = additionalCons
#     lazy_cons.keywords["constraints"] = additionalCons
#     domain = []
#     if filename == "futoshiki_4x4":
#         domain = [1, 2, 3, 4]
#     if filename == "futoshiki_5x5":
#         domain = [1, 2, 3, 4, 5]
#     if filename == "futoshiki_6x6":
#         domain = [1, 2, 3, 4, 5, 6]
#
#     for getNextVar in [lazy_getNextVar, futoshiki.getNextVarInNormalOrder]:
#         for getNextVal in [futoshiki.getNextVal, futoshiki.getFirstValFromDomain]:
#
#             c2, _ = utils.getFutoshikiBoardFromFile("./data/" + filename)
#             case = Puzzle(c2, domain, futoshiki_cons)
#             duration, cases = case.solveForwardChecking(getNextVar, getNextVal, futoshiki.impose_constraints)
#             utils.saveResults("./results/part1_one_solution/" + filename, duration, cases, getNextVarHeuristics[getNextVar], getNextValHeuristics[getNextVal])

# domain = [1,2,3,4,5,6]
#
# filename = "./data/futoshiki_6x6"
# results_file = "./results/part1_one_solution/futoshiki_6x6"
#
# c1, additionalCons = utils.getFutoshikiBoardFromFile(filename)
# lazy_cons.keywords["constraints"] = additionalCons
# lazy_getNextVar.keywords["constraints"] = additionalCons
#
# case = Puzzle(c1, domain, futoshiki_cons)
# duration, cases = case.solveForwardChecking(lazy_getNextVar, futoshiki.getNextVal, futoshiki.impose_constraints)
# utils.saveResults(results_file, duration, cases, "First > || <", "By diagonal, get random")
#
# c2, _ = utils.getFutoshikiBoardFromFile(filename)
# case = Puzzle(c2, domain, futoshiki_cons)
# duration, cases = case.solveForwardChecking(lazy_getNextVar, futoshiki.getFirstValFromDomain, futoshiki.impose_constraints)
# utils.saveResults(results_file, duration, cases, "First > || <", "First from domain")
#
# c3, _ = utils.getFutoshikiBoardFromFile(filename)
# case = Puzzle(c3, domain, futoshiki_cons)
# duration, cases = case.solveForwardChecking(futoshiki.getNextVarInNormalOrder, futoshiki.getNextVal, futoshiki.impose_constraints)
# utils.saveResults(results_file, duration, cases, "Normal order", "By diagonal, get random")
#
# c4, _ = utils.getFutoshikiBoardFromFile(filename)
# case = Puzzle(c4, domain, futoshiki_cons)
# duration, cases = case.solveForwardChecking(futoshiki.getNextVarInNormalOrder, futoshiki.getFirstValFromDomain, futoshiki.impose_constraints)
# utils.saveResults(results_file, duration, cases, "Normal order", "First from domain")




binary_cons = [binary.constraint_no_3_in_a_row, binary.constraint_unique_row_column, binary.constraint_equal_number_of_0_1]
for filename in ["binary_6x6", "binary_8x8", "binary_10x10"]:
    c1 = getBinaryBoardFromFile("./data/" + filename)
    c2 = getBinaryBoardFromFile("./data/" + filename)
    case1 = Puzzle(c1, [0,1], binary_cons)
    case2 = Puzzle(c2, [0,1], binary_cons)
    duration, cases = case1.solveForwardChecking(binary.getNextVar,binary.getNextVal, binary.impose_constraints)
    utils.saveResults("./results/forward_checking/" + filename, duration, cases)

    duration, cases = case2.solveBackTracking(binary.getNextVar, binary.getNextVal)
    utils.saveResults("./results/backtracking/" + filename, duration, cases)




lazy_getNextVar = partial(futoshiki.getNextVar)
lazy_cons = partial(futoshiki.constraint_greater_lower)
futoshiki_cons = [futoshiki.constraint_different_numbers_in_col_row, lazy_cons]


for filename in ["futoshiki_4x4","futoshiki_5x5","futoshiki_6x6"]:
    domain = []
    if filename == "futoshiki_4x4":
        domain = [1, 2, 3, 4]
    if filename == "futoshiki_5x5":
        domain = [1, 2, 3, 4, 5]
    if filename == "futoshiki_6x6":
        domain = [1, 2, 3, 4, 5, 6]


    c1, additionalCons = getFutoshikiBoardFromFile("./data/" + filename)
    c2, _ = getFutoshikiBoardFromFile("./data/" + filename)

    lazy_getNextVar.keywords["constraints"] = additionalCons
    lazy_cons.keywords["constraints"] = additionalCons

    case1 = Puzzle(c1, domain, futoshiki_cons)
    case2 = Puzzle(c2, domain, futoshiki_cons)
    duration, cases = case1.solveForwardChecking(lazy_getNextVar,futoshiki.getNextVal, futoshiki.impose_constraints)
    utils.saveResults("./results/forward_checking/" + filename, duration, cases)

    duration, cases = case2.solveBackTracking(lazy_getNextVar, futoshiki.getNextVal)
    utils.saveResults("./results/backtracking/" + filename, duration, cases)

