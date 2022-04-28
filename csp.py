import time

from utils import *
from copy import deepcopy

class Puzzle:
    def __init__(self, variables, domain, constraints):
        self.variables = variables
        self.domain = domain
        self.constraints = constraints
        self.solutions = []
        self.isSolved = False

    def __repr__(self):
        representation = ""
        for y in self.variables:
            representation += str(y) + '\n'
        return representation


    def constraintsPropagation(self, variables):
        for constraint in self.constraints:
            if not constraint(variables):
                return False
        return True


    def solveBackTracking(self, getNextVarFunction, getNextValFunction):
        def solveHelper(variables, i, j, v, counter):
            variables[i][j] = v
            counter[0] += 1
            if not self.constraintsPropagation(variables):
                return
            else:
                if not hasUnassignedVariables(variables):
                    self.solutions.append(deepcopy(variables))
                    return
                else:
                    # x, y = getNextVariableByPosition(variables, i, j)
                    x, y = getNextVarFunction(variables)
                    vars_clone = deepcopy(variables)
                    domain_copy = deepcopy(self.domain)

                    while len(domain_copy) > 0:
                        val = getNextValFunction(variables,x,y, domain_copy)
                        domain_copy.remove(val)
                        solveHelper(vars_clone,x,y,val, counter)

                    # for val in self.domain:
                    #     solveHelper(vars_clone, x, y, val)

        start = time.time()
        if self.isSolved:
            return
        else:
            cases = [0]
            firstIndex, secondIndex = getNextVarFunction(self.variables)
            var_domain_copy = deepcopy(self.domain)

            while len(var_domain_copy) > 0:
                val = getNextValFunction(self.variables, firstIndex, secondIndex, var_domain_copy)
                var_domain_copy.remove(val)
                solveHelper(self.variables, firstIndex, secondIndex, val, cases)


            # for value in self.domain:
            #     cases[0] += 1
            #     solveHelper(self.variables, firstIndex, secondIndex, value, cases)
            print("Found " + str(len(self.solutions)) + " solutions.")
            print("checked cases: " + str(cases))
            print(self.solutions)

            duration = time.time() - start

            return str(round(duration, 2)) + " s", cases[0]




    def generateDomains(self):
        return [[deepcopy(self.domain) for _ in range(len(self.variables))] for _ in range(len(self.variables))]


    @staticmethod
    def findAnyIsEmpty(domains):
        for row in domains:
            for column in row:
                if not column:
                    return True
        else:
            return False


    def solveForwardChecking(self, getNextVarFunction, getNextValFunction, imposeConstraintsFunction):
        def solveHelper(variables_domains, variables, i, j, v, counter):
            variables[i][j] = v
            imposeConstraintsFunction(variables_domains, variables, i,j)
            counter[0] += 1
            if not self.constraintsPropagation(variables) or Puzzle.findAnyIsEmpty(variables_domains):
                return

            else:
                if not hasUnassignedVariables(variables):
                    self.solutions.append(deepcopy(variables))
                    self.isSolved = True
                    return
                else:
                    # domain check
                    x, y = getNextVarFunction(variables)
                    vars_clone = deepcopy(variables)
                    var_domain = deepcopy(variables_domains[x][y])
                    # domains_copy = deepcopy(variables_domains)

                    while len(var_domain) > 0:
                        val = getNextValFunction(variables,x,y, var_domain)
                        var_domain.remove(val)
                        solveHelper(deepcopy(variables_domains) ,vars_clone, x, y, val, counter)

        start = time.time()
        if self.isSolved:
            return
        else:

            cases = [0]
            firstIndex, secondIndex = getNextVarFunction(self.variables)
            domains = self.generateDomains()


            for n in range(len(self.variables)):
                for m in range(len(self.variables)):
                    imposeConstraintsFunction(domains, self.variables, n, m)

            variableDomain = deepcopy(domains[firstIndex][secondIndex])
            while len(variableDomain) > 0:
                cases[0] += 1
                value = getNextValFunction(self.variables, firstIndex, secondIndex, variableDomain)
                variableDomain.remove(value)
                solveHelper(deepcopy(domains), self.variables, firstIndex, secondIndex, value, cases)

            # for value in self.domain:
            #     solveHelper(self.variables, firstIndex, secondIndex, value)
            duration = time.time() - start
            print("Found " + str(len(self.solutions)) + " solutions.")
            print("checked cases: " + str(cases))
            print(self.solutions)

            return str(round(duration,2)) + " s", cases[0]





    # backup


    # def solveBackTracking(self, getNextVarFunction, getNextValFunction):
    #     def solveHelper(variables, i, j, v):
    #         variables[i][j] = v
    #         if not self.constraintsPropagation(variables):
    #             return
    #         else:
    #             if not hasUnassignedVariables(variables):
    #                 self.solutions.append(deepcopy(variables))
    #                 return
    #             else:
    #                 x, y = getNextVariableByPosition(variables, i, j)
    #                 vars_clone = deepcopy(variables)
    #                 for val in self.domain:
    #                     solveHelper(vars_clone, x, y, val)
    #                     # solveHelper(variables, x, y, val)
    #
    #     if self.isSolved:
    #         return
    #     else:
    #         firstIndex, secondIndex = getNextVariableByPosition(self.variables, 0, -1)
    #         for value in self.domain:
    #             solveHelper(self.variables, firstIndex, secondIndex, value)
    #         print("Found " + str(len(self.solutions)) + " solutions.")
    #         print(self.solutions)

