'''
 Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.
'''


def exist(board, word):
    flag_board = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]

    def nextnode(i, j, board):
        nextij = []
        # print "i is "+str(i) + " j is " + str(j)

        if (i < len(board) - 1) and (flag_board[i + 1][j] != 1):
            nextij.append([i + 1, j])
        if (i > 0) and (flag_board[i - 1][j] != 1):
            nextij.append([i - 1, j])

        if (j < len(board[0]) - 1) and (flag_board[i][j + 1] != 1):
            nextij.append([i, j + 1])
        if (j > 0) and (flag_board[i][j - 1] != 1):
            nextij.append([i, j - 1])

        return nextij

    def dfs(currentij, leftlist, board):
        # print "current_ij is:" + str(currentij)
        flag_board[currentij[0]][currentij[1]] = 1
        if len(leftlist) == 0:
            return True
        i, j = currentij

        nextij_list = nextnode(i, j, board)
        if len(nextij_list) != 0:
            for ij in nextij_list:
                # print "next board is " + str(board[ij[0]][ij[1]]) + "left is: " + str(leftlist)
                if board[ij[0]][ij[1]] == leftlist[0]:
                    if dfs(ij, leftlist[1:], board):
                        return True
        flag_board[currentij[0]][currentij[1]] = 0
        return False

    def find_fist_nodes(board, word):
        first_list = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    first_list.append([i, j])
        if len(first_list) == 0:
            return False
        for ij in first_list:
            if dfs(ij, word[1:], board):
                return True
        return False

    return find_fist_nodes(board, word)


board = [['A', 'B', 'C', 'E'],['S', 'F', 'C', 'S'],['A', 'D', 'E', 'E']]
word = "ABCCED"

exist(board, word)
exist(board, "SEE")
exist(board, "ABCB")

board = [["C","A","A"],["A","A","A"],["B","C","D"]]
exist(board, "AAB")
