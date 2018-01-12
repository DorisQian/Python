'''
This mission uses a 4x4 grid. Each square is numbered from 1 to 16 in row-major order.
You are given 4 numbers (set of integer). These numbers represent the position of the square on the grid and one block if all the squares are adjacent.

You have to identify the kind of block. (Refer to the following image or comment of initial code for the kind of block).
The answer is an upper case alphabet ('I', 'J', 'L', 'O', 'S', 'T' or 'Z'). If it isn't a block then return None.

The block is placed anywhere on the grid and can be rotated (0, 90, 180 or 270 degrees).



Input: 4 numbers (set of integer)

Output: kind of the block (an alphabet or None )

Example:

identify_block({1, 2, 3, 4}) == 'I'
identify_block({1, 2, 3, 6}) == 'T'
identify_block({1, 5, 6, 10}) == 'S'


How it is used:
Creating a tetromino puzzle.

Precondition:
len(input) == 4
all(1 <= num <= 16 for num in input)
output in ('I', 'J', 'L', 'O', 'S', 'T', 'Z', None )
'''
