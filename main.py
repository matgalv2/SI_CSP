import time
from functools import partial
import binary
import futoshiki
from csp import *

time1 = time.time()
c2, additionalCons = getFutoshikiBoardFromFile("./data/futoshiki_5x5")

constraintGraterLower = partial(futoshiki.constraint_greater_lower)
constraintGraterLower.keywords["constraints"] = additionalCons
cons = [futoshiki.constraint_different_numbers_in_col_row, constraintGraterLower]

case2 = Puzzle(c2, [1, 2, 3, 4, 5], cons)

getNextVar_lazy_ev = partial(futoshiki.getNextVar)
getNextVar_lazy_ev.keywords["constraints"] = additionalCons

# getVarDomain_lazy_ev = partial(futoshiki.getVarDomain)
# getVarDomain_lazy_ev.keywords["domain"] = case2.domain

# case2.solveForwardChecking(getVarDomainFunction=getVarDomain_lazy_ev,
#                            getNextVarFunction=getNextVar_lazy_ev,
#                            getNextValFunction=futoshiki.getNextVal)

# case2.solveBackTracking()

print(case2.solveForwardChecking(getNextVar_lazy_ev, futoshiki.getFirstValFromDomain, futoshiki.impose_constraints))

c3, additionalCons = getFutoshikiBoardFromFile("./data/futoshiki_5x5")
case2 = Puzzle(c3, [1, 2, 3, 4, 5], cons)
print(case2.solveBackTracking(getNextVar_lazy_ev, futoshiki.getFirstValFromDomain))
# print(str(time.time() - time1)[:5] + "s - Futoshiki")

# c1 = getBinaryBoardFromFile("./data/binary_10x10")
#
# cons = [binary.constraint_no_3_in_a_row, binary.constraint_unique_row_column, binary.constraint_equal_number_of_0_1]
# case = Puzzle(c1, [0, 1], cons)
#
# # getNextVariable_lazy_ev = partial(binary.getNextVar)
#
#
#
# print(case.solveForwardChecking(getNextVarFunction=binary.getNextVar,
#                                 getNextValFunction=binary.getNextVal,
#                                 imposeConstraintsFunction=binary.impose_constraints))

# Todo:
'''
    1. zmienić ograniczenia, żeby przekładały się na dziedziny zmiennych i wtedy w fc będzie sprawdzanie w przód
'''
