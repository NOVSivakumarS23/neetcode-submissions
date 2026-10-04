class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res = []
        board = [["."] * n for _ in range(n)]

        def backtrack(row: int, cols: int, pos_diag: int, neg_diag: int):
            if row == n:
                res.append(["".join(r) for r in board])
                return

            for col in range(n):
                c_bit = 1 << col
                p_bit = 1 << (row + col)
                # Offset by (n - 1) so indices range from 0 to 2n - 2
                n_bit = 1 << (row - col + n - 1)

                if not (cols & c_bit or pos_diag & p_bit or neg_diag & n_bit):
                    board[row][col] = "Q"
                    backtrack(row + 1, cols | c_bit, pos_diag | p_bit, neg_diag | n_bit)
                    board[row][col] = "."

        def get_mirror(solution: list[str]) -> list[str]:
            return [row[::-1] for row in solution]

        # 1. Process left half of Row 0
        for c in range(n // 2):
            board[0][c] = "Q"
            start_len = len(res)
            
            # Row 0: row=0, col=c => pos_diag bit = c, neg_diag bit = (0 - c + n - 1)
            backtrack(1, 1 << c, 1 << c, 1 << (n - 1 - c))
            board[0][c] = "."
            
            end_len = len(res)
            for i in range(start_len, end_len):
                res.append(get_mirror(res[i]))

        # 2. Process exact middle column if N is odd
        if n % 2 != 0:
            mid = n // 2
            board[0][mid] = "Q"
            backtrack(1, 1 << mid, 1 << mid, 1 << (n - 1 - mid))
            board[0][mid] = "."

        return res