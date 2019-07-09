# Solution of 8 queens. Iterative.
def clear(n, board):
    for i in range(n, 8):
        for j in range(8):
            board[i][j] = 0
    return board
board = [[0 for _ in range(8)] for _ in range(8)] #Initialize board
sol = 0
for r0 in range(8):
    #Clear board
    board = clear(0, board)
    #Start search
    board[0][r0] = 1; #0 if no queens and 1 if queens 
    for r1 in range(8):
        board = clear(1, board)
        if 1 not in [(board[0][r1-1] if r1-1 >= 0 else 0),
                     board[0][r1],
                     (board[0][r1+1] if r1+1 <= 7 else 0)]: #Check if placing the queen will make it under attack from previous queens
            board[1][r1] = 1
            for r2 in range(8):
                board = clear(2, board)
                if 1 not in [(board[0][r2-2] if r2-2 >= 0 else 0),
                             board[0][r2],
                             (board[0][r2+2] if r2+2 <= 7 else 0),
                             (board[1][r2-1] if r2-1 >= 0 else 0),
                             board[1][r2],
                             (board[1][r2+1] if r2+1 <= 7 else 0)]:
                    board[2][r2] = 1
                    for r3 in range(8):
                        board = clear(3, board)
                        if 1 not in [(board[0][r3-3] if r3-3 >= 0 else 0),
                                     board[0][r3],
                                     (board[0][r3+3] if r3+3 <= 7 else 0),
                                     (board[1][r3-2] if r3-2 >= 0 else 0),
                                     board[1][r3],
                                     (board[1][r3+2] if r3+2 <= 7 else 0),
                                     (board[2][r3-1] if r3-1 >= 0 else 0),
                                     board[2][r3],
                                     (board[2][r3+1] if r3+1 <= 7 else 0)]:
                            board[3][r3] = 1
                            for r4 in range(8):
                                board = clear(4, board)
                                if 1 not in [(board[0][r4-4] if r4-4 >= 0 else 0),
                                             board[0][r4],
                                             (board[0][r4+4] if r4+4 <= 7 else 0),
                                             (board[1][r4-3] if r4-3 >= 0 else 0),
                                             board[1][r4],
                                             (board[1][r4+3] if r4+3 <= 7 else 0),
                                             (board[2][r4-2] if r4-2 >= 0 else 0),
                                             board[2][r4],
                                             (board[2][r4+2] if r4+2 <= 7 else 0),
                                             (board[3][r4-1] if r4-1 >= 0 else 0),
                                             board[3][r4],
                                             (board[3][r4+1] if r4+1 <= 7 else 0)]:
                                    board[4][r4] = 1
                                    for r5 in range(8):
                                        board = clear(5, board)
                                        if 1 not in [(board[0][r5-5] if r5-5 >= 0 else 0),
                                                     board[0][r5],
                                                     (board[0][r5+5] if r5+5 <= 7 else 0),
                                                     (board[1][r5-4] if r5-4 >= 0 else 0),
                                                     board[1][r5],
                                                     (board[1][r5+4] if r5+4 <= 7 else 0),
                                                     (board[2][r5-3] if r5-3 >= 0 else 0),
                                                     board[2][r5],
                                                     (board[2][r5+3] if r5+3 <= 7 else 0),
                                                     (board[3][r5-2] if r5-2 >= 0 else 0),
                                                     board[3][r5],
                                                     (board[3][r5+2] if r5+2 <= 7 else 0),
                                                     (board[4][r5-1] if r5-1 >= 0 else 0),
                                                     board[4][r5],
                                                     (board[4][r5+1] if r5+1 <= 7 else 0)]:
                                            board[5][r5] = 1;
                                            
                                            for r6 in range(8):
                                                board = clear(6, board)
                                                if 1 not in [(board[0][r6-6] if r6-6 >= 0 else 0),
                                                             board[0][r6],
                                                             (board[0][r6+6] if r6+6 <= 7 else 0),
                                                             (board[1][r6-5] if r6-5 >= 0 else 0),
                                                             board[1][r6],
                                                             (board[1][r6+5] if r6+5 <= 7 else 0),
                                                             (board[2][r6-4] if r6-4 >= 0 else 0),
                                                             board[2][r6],
                                                             (board[2][r6+4] if r6+4 <= 7 else 0),
                                                             (board[3][r6-3] if r6-3 >= 0 else 0),
                                                             board[3][r6],
                                                             (board[3][r6+3] if r6+3 <= 7 else 0),
                                                             (board[4][r6-2] if r6-2 >= 0 else 0),
                                                             board[4][r6],
                                                             (board[4][r6+2] if r6+2 <= 7 else 0),
                                                             (board[5][r6-1] if r6-1 >= 0 else 0),
                                                             board[5][r6],
                                                             (board[5][r6+1] if r6+1 <= 7 else 0)]:
                                                    board[6][r6] = 1;
                                                
                                                    for r7 in range(8):
                                                        board = clear(7, board)
                                                        if 1 not in [(board[0][r7-7] if r7-7 >= 0 else 0),
                                                                     board[0][r7],
                                                                     (board[0][r7+7] if r7+7 <= 7 else 0),
                                                                     (board[1][r7-6] if r7-6 >= 0 else 0),
                                                                     board[1][r7],
                                                                     (board[1][r7+6] if r7+6 <= 7 else 0),
                                                                     (board[2][r7-5] if r7-5 >= 0 else 0),
                                                                     board[2][r7],
                                                                     (board[2][r7+5] if r7+5 <= 7 else 0),
                                                                     (board[3][r7-4] if r7-4 >= 0 else 0),
                                                                     board[3][r7],
                                                                     (board[3][r7+4] if r7+4 <= 7 else 0),
                                                                     (board[4][r7-3] if r7-3 >= 0 else 0),
                                                                     board[4][r7],
                                                                     (board[4][r7+3] if r7+3 <= 7 else 0),
                                                                     (board[5][r7-2] if r7-2 >= 0 else 0),
                                                                     board[5][r7],
                                                                     (board[5][r7+2] if r7+2 <= 7 else 0),
                                                                     (board[6][r7-1] if r7-1 >= 0 else 0),
                                                                     board[6][r7],
                                                                     (board[6][r7+1] if r7+1 <= 7 else 0)]:
                                                            board[7][r7] = 1;
                                                            # Print board
                                                            sol = sol + 1
                                                            print("Solution " + str(sol) + ":")
                                                            for i in range(8):
                                                                for j in range(8):
                                                                    print(board[i][j], end= '')
                                                                print()
                                                            print("--------")
                                                            
                                                                    

