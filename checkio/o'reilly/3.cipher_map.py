"""
"Nikola, A1213pokl, bAse730onE."

"Yes Sofia, what is it?"

"You tell me! Your torture device is singing my circuits with its new lexicon. There is 
no way I can remember these new passwords and the thing doesn't accept simple and easy ones!"

"Oh, those will be good passwords, you can use them."

"Why can’t you use them!?" Sofia asked almost hysterically. "I’ve already forgotten them! 
Do you want me locked out of my own house for eternity? Come up with something easier so 
I don’t have to keep all that randomized gobbledygook in my head." Sofia rarely acted so 
demanding but she had reached her boiling point. The stress of the past few days coupled 
with her exhaustion had brought her to the edge.

"Don’t worry, I was expecting something easier to remember. Why don’t you use the cipher 
map to help with your password. With it we can encrypt all the passwords and leave them 
right next to the door or in a special place that we all agree upon. You will only be able 
to read them with the use of the cipher map which we will take with us on our trip.

"So I don’t need to remember all of those passwords? All we have to do is make sure that we 
don't lose the cipher map." asked Sofia with hopefully.

"Yes, that is correct."

"Awesome. Show me the cipher map and explain how this works one more time."

Help Sofia write a decrypter for the passwords that Nikola will encrypt through the cipher 
map. A cipher grille is a 4×4 square of paper with four windows cut out. Placing the grille 
on a paper sheet of the same size, the encoder writes down the first four symbols of his 
password inside the windows (see fig. below). After that, the encoder turns the grille 90 
degrees clockwise. The symbols written earlier become hidden under the grille and clean paper 
appears inside the windows. The encoder then writes down the next four symbols of the password 
in the windows and turns the grille 90 degrees again. Then, they write down the following four 
symbols and turns the grille once more. Lastly, they write down the final four symbols of the 
password. Without the same cipher grille, it is difficult to discern the password from the 
resulting square comprised of 16 symbols. Thus, the encoder can be confident that no hooligan 
will easily gain access to the locked door.



Write a module that enables the robots to easily recall their passwords through codes when they 
return home.

The cipher grille and the ciphered password are represented as an array (tuple) of strings.

Input: A cipher grille and a ciphered password as a tuples of strings.

Output: The password as a string.

Example:

recall_password(
    ('X...',
     '..X.',
     'X..X',
     '....'),
    ('itdf',
     'gdce',
     'aton',
     'qrdi')) == 'icantforgetiddqd'

recall_password(
    ('....',
     'X..X',
     '.X..',
     '...X'),
    ('xhwc',
     'rsqx',
     'xqzz',
     'fyzr')) == 'rxqrwsfzxqxzhczy'

How it is used: Here you can learn how to work with 2D arrays. You also get to learn about the 
ancient Grille Cipher, a technique of encoding messages which has been used for half a millenium. 
The earliest known description of the grille cipher comes from the Italian mathematician, Girolamo 
Cardano in 1550.

Precondition: len(cipher_grille) == 4
len(ciphered_password) == 4
all(len(row) == 4 for row in ciphered_password)
all(len(row) == 4 for row in cipher_grille)
all(all(ch in string.ascii_lowercase for ch in row) for row in ciphered_password)
all(all(ch == "X" or ch == "." for ch in row) for row in cipher_grille)

尼古拉,A1213pokl bAse730onE。”
“是的，索菲亚，这是什么?”
“你告诉我!你的折磨设备用它的新词汇来唱我的电路。我不可能记住这些新的密码，而且这个东西不接受
简单易行的密码!”
“哦，这些密码都不错，你可以用。”
“你为什么不能用呢?”索菲亚几乎歇斯底里地问道。“我已经忘记他们!你想让我永远锁在我自己的房子里
吗?想出一些更简单的方法，这样我就不用把那些随机的官样文章放在脑子里了。索菲亚很少表现得如此
苛刻，但她已经达到了她的沸点。过去几天的压力加上她的疲惫，使她感到紧张不安。
“别担心，我想要更容易记住的东西。”你为什么不使用密码地图来帮助你的密码。用它我们可以加密所
有的密码，然后把它们放在门旁边或者我们都同意的特殊地方。你只能用我们在旅途中随身携带的密码地
图来阅读。“所以我不需要记住所有的密码?”我们所要做的就是确保我们不会丢失密码图。索菲亚满怀希
望地问道。“是的,这是正确的。”
“太棒了。给我看看密码图，再解释一下这是怎么回事。

帮助Sofia为Nikola通过密码映射加密的密码写一个解密。密码格栅是一个4×4平方的纸有四个窗户。
编码器将格栅放在相同大小的纸上，将其密码的前四个符号写在窗口内(见下图)。之后，编码器顺时
针旋转90度。之前写的符号被隐藏在格子里，干净的纸出现在窗户里面。然后，编码器将密码的下四
个符号写入窗口，并再次将格栅旋转90度。然后，他们写下以下四个符号并再次转动格栅。最后，他
们写下密码的最后四个符号。如果没有相同的密码格栅，就很难分辨出由16个符号组成的正方形的密
码。因此，编码器可以确信任何流氓都不会轻易进入锁着的门。
编写一个模块，使机器人能够在返回家中时通过代码轻松地记住密码。
密码格栅和密码密码被表示为字符串数组(tuple)。

输入:一个密码格栅和一个密码作为字符串的元组。
输出:作为字符串的密码。

如何使用:在这里您可以学习如何使用2D数组。你还可以了解古老的格栅密码，一种编码信息的技术，
它已经被使用了半个世纪。对格栅密码最早的描述来自于1550年意大利数学家Girolamo Cardano。
"""

def recall_password(cipher_grille, ciphered_password):
    grille = cipher_grille
    x_index = get_index(cipher_grille)
    password = get_password(x_index, ciphered_password)
    flag = 3
    while flag:
        grille = []
        for i in range(4):
            grille.append(cipher_grille[3][i] + cipher_grille[2][i] + cipher_grille[1][i] + cipher_grille[0][i])
        cipher_grille = grille

        x_index = get_index(grille)
        pwd = get_password(x_index, ciphered_password)
        password += pwd
        flag -= 1
    return password
def get_index(cipher_grille):
    index = []
    for n in range(4):
        count = cipher_grille[n].count('X')
        i = 1
        line = cipher_grille[n]
        while i:
            if i == count + 1:
                break
            else:
                index.append((n, line.index('X')))
                line = line.replace('X', '.', 1)
            i += 1
    return index

def get_password(x_index, ciphered_password):
    password = ''
    for i in range(4):
        x, y = x_index[i][0], x_index[i][1]
        password += ciphered_password[x][y]
    return password

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'