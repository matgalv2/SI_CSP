# import copy
# from utils import *
#
#
# # class BinaryPuzzle:
# #     def __init__(self, N):
# #         # N must be even!!!
# #         self.N = N
# #         self.board = [[None for _ in range(N)] for _ in range(N)]
# #
# #     def __repr__(self):
# #         representation = ""
# #         for y in self.board:
# #             representation += str(y) + '\n'
# #
# #         return representation
# #
# #     def getBoardFromFile(self, filename):
# #         with open(filename, 'r') as file:
# #             newBoard = []
# #             for line in file:
# #                 row = []
# #                 for i in line:
# #                     if str(i) != '\n':
# #                         if str(i).isdigit():
# #                             row.append(int(i))
# #                         else:
# #                             row.append(None)
# #                 newBoard.append(row)
# #
# #         self.board = newBoard
# #
# #
# #
# #     @staticmethod
# #     def constraint_no_3_in_a_row(board):
# #         length = len(board)
# #         if length < 3:
# #             return True
# #
# #         for y in range(length):
# #             for x in range(length):
# #                 row = board[y][x:x + 3]
# #                 if y < length - 2:
# #                     column = [board[y][x], board[y + 1][x], board[y + 2][x]]
# #                     if column == [0, 0, 0] or column == [1, 1, 1]:
# #                         return False
# #                 if row == [0, 0, 0] or row == [1, 1, 1]:
# #                     return False
# #
# #         return True
# #
# #         #
# #         # summedRow = sum(self.board[y][x:x+3])
# #         # summedColumn = sum(self.board[x][y:y+3])
# #         # if summedRow in [0,3] or summedColumn in [0,3]:
# #         #     return False
# #
# #     @staticmethod
# #     def constraint_unique_row_column(board):
# #         length = len(board)
# #         for i in range(length):
# #             for j in range(i + 1, length):
# #                 if isWithoutNone(board[i]) and isWithoutNone(board[j]):
# #                     if board[i] == board[j]:
# #                         return False
# #         # columns
# #         for i in range(length):
# #             for j in range(i + 1, length):
# #                 col1 = getColumn(board, i)
# #                 col2 = getColumn(board, j)
# #                 if isWithoutNone(col1) and isWithoutNone(col2):
# #                     if col1 == col2:
# #                         return False
# #
# #         return True
# #
# #     @staticmethod
# #     def constraint_equal_number_of_0_1(board):
# #         length = len(board)
# #         for i in range(length):
# #             col = getColumn(board, i)
# #             row = board[i]
# #             if isWithoutNone(col) and isWithoutNone(row):
# #                 if sum(col) != length / 2 or sum(row) != length / 2:
# #                     return False
# #         return True
# #
# #     @staticmethod
# #     def constraintPropagation(board):
# #         return BinaryPuzzle.constraint_no_3_in_a_row(board) \
# #                and BinaryPuzzle.constraint_equal_number_of_0_1(board) \
# #                and BinaryPuzzle.constraint_unique_row_column(board)
# #
# #     @staticmethod
# #     def solve(B, i, j, v, solutions):
# #         B[i][j] = v
# #         if not BinaryPuzzle.constraintPropagation(B):
# #             return
# #         else:
# #             if not hasUnassignedVariables(B) and BinaryPuzzle.constraintPropagation(B):
# #                 solutions.append(B)
# #                 print(B)
# #                 return
# #             else:
# #                 # x, y = getRandomEmptyCell(variables)
# #                 x, y = getNextVariable(B, i, j)
# #                 # deep copy
# #                 B_clone = copy.deepcopy(B)
# #                 BinaryPuzzle.solve(B_clone, x, y, 0, solutions)
# #                 BinaryPuzzle.solve(B_clone, x, y, 1, solutions)
# #
# #
# # b = BinaryPuzzle(6)
# # b.getBoardFromFile("./data/binary_8x8")
# #
# # g = []
# # BinaryPuzzle.solve(b.board, 0, 0, 1, g)
# # BinaryPuzzle.solve(b.board, 0, 0, 0, g)
# #
# # print(len(g))
#
#
# class Futoshiki:
#     # constraint its a tuple where first location must be grater than second
#     def __init__(self, N):
#         self.N = N
#         self.board = [[None for _ in range(N)] for _ in range(N)]
#
#     def __repr__(self):
#         representation = ""
#         for y in self.board:
#             representation += str(y) + '\n'
#         return representation
#
#     def getBoardFromFile(self, filename):
#         with open(filename, 'r') as file:
#             newBoard = []
#             i = 0
#             for line in file:
#                 if i % 2 != 0:
#                     row = []
#                     j = 0
#                     for char in line:
#                         if j% 2 != 0:
#                             if char != '\n':
#                                 if str(char).isdigit():
#                                     row.append(int(char))
#                                 else:
#                                     row.append(None)
#                             j += 1
#                     newBoard.append(row)
#                 i += 1
#
#
#
#
#
#     @staticmethod
#     def constraint_different_numbers_in_col_row(board):
#         length = len(board)
#         numbers = set([x + 1 for x in range(length)])
#         for i in range(length):
#             row = board[i]
#             col = getColumn(board, i)
#             if isWithoutNone(row) and numbers != set(row):
#                 return False
#             if isWithoutNone(col) and numbers != set(col):
#                 return False
#
#         return True
#
#     @staticmethod
#     def constraint_greater_lower(board, constraints):
#         for constraint in constraints:
#             loc1 = constraint[0]
#             loc2 = constraint[1]
#             if board[loc1[0]][loc1[1]] is not None and board[loc2[0]][loc2[1]] is not None:
#                 if board[loc1[0]][loc1[1]] <= board[loc2[0]][loc2[1]]:
#                     return False
#         return True
#
#     @staticmethod
#     def constraintPropagation(board, constraints):
#         fulfillmentOfConstraints = Futoshiki.constraint_greater_lower(board, constraints) \
#                                    and Futoshiki.constraint_different_numbers_in_col_row(board)
#
#         return fulfillmentOfConstraints
#
#     @staticmethod
#     def solve(B, i, j, v, N, solutions, constraints):
#         B[i][j] = v
#         if not Futoshiki.constraintPropagation(B, constraints):
#             return
#         else:
#             if not hasUnassignedVariables(B) and Futoshiki.constraintPropagation(B, constraints):
#                 solutions.append(B)
#                 print(B)
#                 return
#             else:
#                 # x, y = getRandomEmptyCell(variables)
#                 x, y = getNextVariable(B, i, j)
#                 # deep copy
#                 for i in range(N):
#                     B_clone = copy.deepcopy(B)
#                     Futoshiki.solve(B_clone, x, y, i + 1, N, solutions, constraints)
#                 # Futoshiki.solve(B_clone, x, y, 0, solutions)
#                 # Futoshiki.solve(B_clone, x, y, 1, solutions)
#
#
# cons = [((1, 0), (2, 0)), ((2, 1), (1, 1)), ((1, 2), (2, 2)), ((2, 0), (3, 0)), ((3, 0), (3, 1)), ((3, 2), (3, 3))]
#
# # correct = [[1,2,3,4],[4,3,2,1],[3,4,1,2],[2,1,4,3]]
# f = Futoshiki(4)
# f.board[0][2] = 3
# f.board[1][1] = 3
# f.board[3][3] = 3
#
# sols = []
# #
# x1,y1 = getRandomVariable(f.board)
# Futoshiki.solve(f.board,0,0,1,4,sols,cons)
# Futoshiki.solve(f.board,0,0,2,4,sols,cons)
# Futoshiki.solve(f.board,0,0,3,4,sols,cons)
# Futoshiki.solve(f.board,0,0,4,4,sols,cons)
#
# print(len(sols))
# # print(sols[0])
#
