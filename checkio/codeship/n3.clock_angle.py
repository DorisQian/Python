'''
Analog clocks display time with an analog clock face, which consists of a round dial with the numbers 1 through 12, the hours in the day, around the outside. The hours are indicated with an hour hand, which makes two revolutions in a day, while the minutes are indicated by a minute hand, which makes one revolution per hour. In this mission we will use a clock without second hand. The hour hand moves smoothly and the minute hand moves step by step.

You are given a time in 24-hour format and you should calculate a lesser angle between the hour and minute hands in degrees. Don't forget that clock has numbers from 1 to 12, so 23 == 11. The time is given as a string with the follow format "HH:MM", where HH is hours and MM is minutes. Hours and minutes are given in two digits format, so "1" will be writen as "01". The result should be given in degrees with precision ±0.1.

clocks

For example, on the given image we see "02:30" or "14:30" at the left part and "01:42" or "13:42" at the right part. We need to find the lesser angle.

Input: A time as a string.

Output: The lesser angle as an integer or a float.

Example:

clock_angle("02:30") == 105
clock_angle("13:42") == 159
clock_angle("01:43") == 153.5

How it is used: Simple mathematics and skill to built a model for various things from real world.

Precondition:
re.match("\A((2[0-3])|([0-1][0-9])):[0-5][0-9]\Z", time)

模拟时钟用一个模拟时钟面显示时间，模拟时钟面包括一个数字1到12的圆形表盘，白天的时间，外部的时间。时针以时针表示，一天两次旋转，分针以分针表示，每分钟旋转一次。在这个任务中，我们将使用一个没有秒针的时钟。时针平稳移动，分针一步一步移动。

给你一个24小时制的时间，你应该计算小时和分钟之间的小角度（度）。不要忘记时钟的数字从1到12，因此23 == 11.时间以字符串形式给出，格式为“HH：MM”，其中HH表示小时，MM表示分钟。小时和分钟以两位数字格式给出，所以“1”将写为“01”。结果应以±0.1的精度以度数给出。

时钟

例如，在给定的图像上，我们在左侧看到“02:30”或“14:30”，在右侧看到“01:42”或“13:42”。我们需要找到较小的角度。

输入：一个时间作为一个字符串。
输出：作为整数或浮点的较小角度。

它是如何使用的：简单的数学和技巧为现实世界中的各种事物建立模型。
'''