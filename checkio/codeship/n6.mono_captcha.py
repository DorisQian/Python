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

让我们教Stephan识别简单的数字。 机器人使用低分辨率的等宽字体。 你可以在下面的图片上看到字体。 该字体对一个像素的错误具有抗噪声能力。

字形
你的程序应该读取编码为二进制矩阵的图像中显示的数字。 每个数字可以包含错误的像素，但每个数字不得超过一个。 数字之间的距离等于一个像素（只考虑比其他字母窄的“1”，但宽度为3像素）。

验证码
输入：图像作为列表1或0的列表。
输出：数字为整数。

使用方法：此任务将向您展示光学字符识别如何工作，并使您熟悉需要抗噪声的低分辨率字体。 这对需要可靠性的系统很有用。
'''

