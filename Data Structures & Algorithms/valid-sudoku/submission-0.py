class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create tracker for 1-9 for each row, column, and box
        # DS where you can check for duplicates. Array of booleans.
        boxes = [[False] * 9 for _ in range(9)]
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue # Skip .
                num = int(val)

                # Check if duplicate in rows
                if rows[i][num-1]:
                    # print(f"Row duplicate found at {i},{j} for num {val}")
                    # print("rows\n",rows)
                    return False # Short circuit. Duplicate found
                rows[i][num-1] = True

                # Check if duplicate in cols
                if cols[j][num-1]:
                    # print(f"Col duplicate found at {i},{j} for num {val}")
                    # print("cols\n",cols)
                    return False # Short circuit. Duplicate found
                cols[j][num-1] = True

                # Check if duplicate in box
                
                # Examples
                # i,j -> box_idx
                # 4,1 -> 3
                # 6,3 -> 7

                # Simpler Example with 3x3 grid
                # (row*3) + col = box_idx

                # Now replace row and column with equivalents (i // 3) and (j // 3), respectively
                # (i // 3 * 3) + (j // 3) = box_idx

                box_idx = (i // 3 * 3) + (j // 3)
                if boxes[box_idx][num-1]:
                    # print(f"Box duplicate found at {i},{j} for num {val} in box {box_idx}")
                    # print("boxes\n",boxes)
                    return False # Short circuit. Duplicate found
                boxes[box_idx][num-1] = True
        
        return True # Successfully detected no duplicates
                

