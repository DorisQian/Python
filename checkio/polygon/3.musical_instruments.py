'''
You are the manager of the music band which uses the next musical instruments: Guitar, Drums, Piano, Flute, which make this sounds: ‘guitar music’, ‘drums music’, ‘piano music’, ‘flute music’. Sometimes the instrumets break down and you have to repair them, but the rehearsals must go on. That's why you have found the special Digital musical instrument which can play its own music ('digital music') and also can imitate the sound of the any other instrument.
Your task is to create classes for all of the instruments and the adapters which could help to play sounds of the instruments with Digital.
In this mission you could use this design pattern - Adapter.

Examples:

Guitar().play_guitar() == "guitar music"
Drums().play_drums() == "drums music"
Piano().play_piano() == "piano music"
Flute().play_flute() == "flute music"
Digital().play_digital() == "digital music"
GuitarAdapter().play_digital() == "guitar music"
DrumsAdapter().play_digital() == "drums music"
PianoAdapter().play_digital() == "piano music"
FluteAdapter().play_digital() == "flute music"

Input: methods of the classes of the musical instruments and the adapters.
Output: right music.

How it is used: Another one design pattern for more practice in the OOP.

Precondition: All data are correct.

您是使用下一个乐器的吉他，鼓，钢琴和长笛的音乐乐队的管理者，这使得这听起来像是：'吉他音乐'，'鼓音乐'，'钢琴音乐'，'长笛音乐'。 有时候这些工具会坏掉，你必须修理它们，但是排练必须继续。 这就是为什么你找到了可以播放自己的音乐（'数字音乐'）的特殊数字乐器，也可以模仿任何其他乐器的声音。
你的任务是为所有的乐器和适配器创建类，它们可以帮助用数字播放乐器的声音。
在这个任务中，你可以使用这种设计模式 - 适配器。

输入：乐器和适配器类的方法。
输出：正确的音乐。

它是如何使用的：另一种设计模式是在OOP中进行更多练习。
'''

class Guitar:
    def __init__(self):
        pass

class Drums:
    def __init__(self):
        pass

class Piano:
    def __init__(self):
        pass

class Flute:
    def __init__(self):
        pass

class Digital:
    def __init__(self):
        pass

if __name__ == '__main__':

    assert Guitar().play_guitar() == "guitar music"
    assert Drums().play_drums() == "drums music"
    assert Piano().play_piano() == "piano music"
    assert Flute().play_flute() == "flute music"
    assert Digital().play_digital() == "digital music"
    assert GuitarAdapter().play_digital() == "guitar music"
    assert DrumsAdapter().play_digital() == "drums music"
    assert PianoAdapter().play_digital() == "piano music"
    assert FluteAdapter().play_digital() == "flute music"

    print("Coding complete? Let's try tests!")