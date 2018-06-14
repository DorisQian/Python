'''
At your work there is a place for the lunch where are 5 microwave ovens (М1, М2, М3, М4, М5). Every microwave could be controlled by remote control with the next commands:

set_time("xx:xx"), where "xx:xx" - time in the minutes and seconds, which shows, how long the eat will be warm up. For example: set_time("05:30")
add_time("+Ns"), add_time("+Nm"), where N - the amount of the seconds("s") or minutes("m"), which should be added to the current time.
del_time("-Ns"), del_time("-Nm"), where N - the amount of the seconds("s") or minutes("m"), which should be subtracted from the current time.
show_time(), shows current time for the microwave.

The default time is 00:00. The time is couldn't be less than 00:00 or greater than 90:00, even if add_time or del_time make this happens. 

Your task is to create 5 classes - one for the each microwave remote control: RemoteControlM1, RemoteControlM2, RemoteControlM3, RemoteControlM4, RemoteControlM5. Only fifth oven is works properly and shows the full time. The other four have some problems with their displays. They are show time like this:
RemoteControlM1.show_time() == "_0:00"
RemoteControlM2.show_time() == "0_:00"
RemoteControlM3.show_time() == "00:_0"
RemoteControlM4.show_time() == "00:0_"
RemoteControlM5.show_time() == "00:00"
So the 1st microwave doesn't show the 1st time symbol, the 2nd - 2nd symbol and so on. 
In this mission you could use Bridge design pattern. Its main task is - to decouple an abstraction from its implementation so that the two can vary independently.

Example:

remote_control_1 = RemoteControlM1()
remote_control_1.set_time("01:00")
    
remote_control_2 = RemoteControlM5()
remote_control_2.del_time("-300s")
remote_control_2.add_time("+100s")
    
remote_control_1.show_time() == "_1:00"
remote_control_2.show_time() == "01:40"

Input: methods of the 5 RemoteControl classes.
Output: time on the display of the microwave.

How it is used: For work with time.

Precondition: 00:00 <= time <= 90:00

在你的工作中，有一个午餐的地方有5个微波炉（М1，М2，М3，М4，М5）。每个微波炉都可以通过下一个命令通过遥控进行控制：

set_time（“xx：xx”），其中“xx：xx” - 分钟和秒钟的时间，表示吃多久会变热。例如：set_time（“05:30”）
add_time（“+ Ns”），add_time（“+ Nm”），其中N - 秒数（“s”）或分钟数（“m”），应添加到当前时间。
del_time（“ - Ns”），del_time（“ - Nm”），其中N - 秒数（“s”）或分钟数（“m”），应从当前时间中减去。
show_time（）显示微波的当前时间。

默认时间是00:00。时间不能小于00:00或大于90:00，即使add_time或del_time发生这种情况。

你的任务是创建5个类 - 每个微波遥控器一个：RemoteControlM1，RemoteControlM2，RemoteControlM3，RemoteControlM4，RemoteControlM5。只有第五个烤箱工作正常，并显示全职。其他四台显示器出现问题。他们展示的时间是这样的：
RemoteControlM1.show_time（）==“_0：00”
RemoteControlM2.show_time（）==“0_：00”
RemoteControlM3.show_time（）==“00：_0”
RemoteControlM4.show_time（）==“00：0_”
RemoteControlM5.show_time（）==“00:00”
所以第一台微波炉不显示第一次符号，第二个 - 第二个符号等等。
在这个任务中你可以使用Bridge设计模式。其主要任务是 - 将抽象与其实现分离开来，以使两者可以独立变化。

输入：5个远程控制类的方法。
输出：显示微波的时间。
它如何使用：适合与时间一起工作。
'''

class RemoteControlBase(object):
    def __init__(self):
        pass

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    remote_control_1 = RemoteControlM1()
    remote_control_1.set_time("01:00")
    
    remote_control_2 = RemoteControlM5()
    remote_control_2.del_time("-300s")
    remote_control_2.add_time("+100s")
    
    assert remote_control_1.show_time() == "_1:00"
    assert remote_control_2.show_time() == "01:40"
