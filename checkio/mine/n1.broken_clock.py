'''
We have a broken clock. We know how quickly it runs or lags over a specific 
period of time. At first, the clock is set to the correct time, but after a 
while it begins to display an incorrect time... But instead of correcting the 
clock each time, we will use an algorithm to calculate the correct time by 
accounting for the difference compared to the actual current time. Of course 
we will have access to the correct time for each day. In addition, you can be 
certain that the correct starting time and current actual time fall on the same 
day. For this mission, time is measured in a 24 hour format.

You are given three values. The first is the correct starting time. The second 
is the current time displayed on the broken clock (which is incorrect). Time is 
given as strings in the format "hh:mm:ss" (Examples: "01:16:59" and "23:00:13"). 
The third value is a description of the clock error in the format "+(-)N [second, 
minute, hour](s) at M [second, minute, hour](s)". For Example "+1 second at 10 
seconds" -- the clock is 1 second fast for every 10 seconds of actual time and "-5 
minutes at 5 hours" -- the clock lags 5 minutes for every 5 hours of actual time.

You should calculate the real time with the given values. The result should be 
rounded down to the nearest second (use floor or int).

Let's examine one example -- '00:00:00', '00:00:30', '+2 seconds at 6 seconds'.
0th step: The real and fake time is "00:00:00".
When the real time is "00:00:06", the fake time is "00:00:08".
At real "00:00:18", fake is "00:00:24".
At real "00:00:21", fake is "00:00:28".
At real "00:00:22", fake is "00:00:29.333...".
At real "00:00:22.5", fake is "00:00:30".
So answer is "00:00:22.5" after rounding down "00:00:22"

Input: Three arguments. Correct starting time, current wrong time and broken clock 
descriptions as strings.

Output: The real time as a string.

Example:
broken_clock('00:00:00', '00:00:15', '+5 seconds at 10 seconds') ==  '00:00:10'
broken_clock('06:10:00', '06:10:15', '-5 seconds at 10 seconds') ==  '06:10:30'
broken_clock('13:00:00', '14:01:00', '+1 second at 1 minute') ==  '14:00:00'
broken_clock('01:05:05', '04:05:05', '-1 hour at 2 hours') ==  '07:05:05'
broken_clock('00:00:00', '00:00:30', '+2 seconds at 6 seconds') ==  '00:00:22'

How it is used: Believe it or not, this mission is teaching you some of the 
same principles used in GPS tracking. Because the satellites in orbit are moving 
so fast, we need to account for relativity. So, when we factor in the speed of 
the satellite, we can figure out the difference from the time on the ground and 
write a program to compensate.

Precondition:
"wrong_time" is later than "starting_time".

我们有一个坏的时钟。我们知道它运行得有多快，或者滞后于某个具体的
一段的时间。首先，时钟被设置为正确的时间，但是之后
而它开始显示一个不正确的时间...但不是纠正每次计时，我们将用一个算法来计算正确的时间
占当前实际时间的差值。当然
我们将有机会获得每一天的正确时间。另外，你可以
确定正确的开始时间和当前实际时间落在同一时间
天。对于这个任务，时间是以24小时的格式来衡量的。

你有三个价值观。首先是正确的开始时间。第二
是当前时间显示在损坏的时钟（这是不正确的）。时间是
格式为“hh：mm：ss”（例如：“01:16:59”和“23:00:13”）。
第三个值是以“+（ - ）N [second，
分钟，小时]（s）在M [秒，分，小时]（s）“例如”+1秒在10
秒“ - 时钟每10秒实际时间快1秒，”-5“分钟在5小时“ - 时钟滞后5分钟每5小时的实际时间。

你应该用给定的值来计算实时。结果应该是向下舍入到最接近的秒（使用floor或int）。
输入：三个参数。 正确的开始时间，当前的错误时间和损坏的时钟
描述为字符串。
输出：实时的字符串。

它是如何使用的：信不信由你，这个任务是教你一些GPS跟踪中使用的相同的原则。 
由于轨道上的卫星移动得太快，我们需要考虑相对性。 所以，当我们考虑卫星的速度时，
我们可以计算出与地面时间的差异，并编写一个程序来进行补偿。

前提：
“wrong_time”晚于“starting_time”。
'''