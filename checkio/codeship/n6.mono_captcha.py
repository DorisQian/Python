'''
Let's teach Stephan to recognize simple numbers. The Robots use monospaced fonts with low resolution. You can see the font on the picture below. This font has noise immunity to one-pixel error.

font
Your program should read the number shown in an image encoded as a binary matrix. Each digit can contain a wrong pixel, but no more than one for each digit. The space between digits is equal to one pixel (just think about "1" which is narrower than other letters, but has a width of 3 pixels).

captcha
Input: An image as a list of lists with 1 or 0.

Output: The number as an integer.

Example:

checkio([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
         [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
         [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
         [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
         [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394
checkio([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0],
         [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
         [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
         [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
         [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394
    

How it is used: This task will show you how optical character recognition works and will familiarize you with low-resolution fonts requiring noise-immunity. This can be useful for the systems that required the reliability.

Precondition: matrix_rows == 5
5 ≤ matrix_columns < 30
∀ x ∈ matrix : x == 0 or x == 1
digit_width == 3
Each digit contains no more than one wrong pixel.
digits_space == 1
'''