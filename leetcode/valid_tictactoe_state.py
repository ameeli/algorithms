import unittest

"""
A Tic-Tac-Toe board is given as a string array board. Return True if and only
if it is possible to reach this board position during the course of a valid
tic-tac-toe game.

The board is a 3 x 3 array, and consists of characters " ", "X", and "O".  The
" " character represents an empty square.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player always places "X" characters, while the second player always
places "O" characters.
"X" and "O" characters are always placed into empty squares, never filled ones.
The game ends when there are 3 of the same (non-empty) character filling any
row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Example 1:
Input: board = ["O  ", "   ", "   "]
Output: false
Explanation: The first player always plays "X".

Example 2:
Input: board = ["XOX", " X ", "   "]
Output: false
Explanation: Players take turns making moves.

Example 3:
Input: board = ["XXX", "   ", "OOO"]
Output: false

Example 4:
Input: board = ["XOX", "O O", "XOX"]
Output: true
Note:

board is a length-3 array of strings, where each string board[i] has length 3.
Each board[i][j] is a character in the set {" ", "X", "O"}.
"""


def check_winner(board, player):
    """
    Check board to see if player has winning position.
    """
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True

    for i in range(len(board)):
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True

    if board[0][0] == board[1][1] == board[2][2] == player or \
            board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


def valid_tic_tac_toe(board):
    total_x = 0
    total_o = 0

    for row in board:
        for space in row:
            if space == 'X':
                total_x += 1
            if space == 'O':
                total_o += 1

    if total_x < total_o or total_x > total_o + 1:
        return False

    if check_winner(board, 'O'):
        if check_winner(board, 'X'):
            return False
        return total_o == total_x

    if check_winner(board, 'X') and total_x != total_o + 1:
        return False

    return True
