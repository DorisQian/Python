'''
There are few things that are so unpardonably neglected in our country as poker. 
The upper class knows very little about poker. Now and then you find ambassadors 
who have sort of a general knowledge of poker, but the ignorance of the people is 
fearful. Why, I have known clergymen, good men, kind-hearted, liberal, sincere, and 
all that, who did not know the meaning of a "flush". It is enough to make one ashamed of the species.
-- Mark Twain
Texas hold'em is a variation of the standard card game of poker. Two cards (hole cards) 
are dealt face down to each player and then five community cards are placed face-up by 
the dealer. And when all openings we need to define what is the combination a player have.

You are given a sequence of 7 cards and you should choose the best hand (5 cards) in it. 
Card sequence are described as a string, where each card are defined by two character - 
rank and suit. Cards separated by commas.

The descending ranks are: "A" (Ace), "K" (King), "Q" (Queen), "J" (Jack), "T" (Ten), and "9" to "2".
The descending suits are "h" (hearts), "d" (diamonds), "c" (clubs), "s" (spades).

Texas holdem uses the classical poker hand list: Straight flush, Four of a kind, Full 
house, Flush, Straight, Three of a kind, Two Pair, One Pair and High card.

Because of the presence of community cards in Texas hold 'em, different players' hands 
can often come very close in value. As a result, it is common for kickers to be used to 
determine the winning hand for cases where two or more hands tie. A kicker is a card which 
is part of the five-card poker hand, but is not used in determining a hand's rank. For instance, 
in the hand A-A-A-K-Q, the king and queen are kickers.

In our version of Texas Hold'em cards of differing suits have different values. This means that 
there is only ever one best five-card hand to return. So "Td" is higher than "Tc", but lower then "Jc".

Your goal is to choose the best hand with 5 cards and return them as a string, where cards are 
separated by commas and ordering from the highest to lowest value. For example: We have two pair 
by queens (heart and spades) and eights (diamonds and clubs) and nine heart as a kicker. The 
result: "Qh,Qs,9h,8d,8c". Be careful with order.

Input: A list of cards as a string.

Output: The best hand as a string.

Example:
texas_referee("Kh,Qh,Ah,9s,2c,Th,Jh") == "Ah,Kh,Qh,Jh,Th"
texas_referee("Qd,Ad,9d,8d,Td,Jd,7d") == "Qd,Jd,Td,9d,8d",

How it is used: This concept is a good example of combinatorial optimisation process, and could 
come in handy should you make a poker game in Python.

Precondition:

cards_quantity == 7
All cards correct and unique.

有几件事在我们国家如此不可原谅地被忽视，比如扑克。
上流社会对扑克知之甚少。不时有你找到大使
谁拥有扑克的一般知识，但人民的无知是
可怕。我为什么认识神职人员，善良的人，善良的，自由的，真诚的，以及
所有这些，谁不知道“同花顺”的含义。对这个物种感到羞愧就足够了。
- 马克吐温
德州扑克是扑克标准扑克游戏的变种。两张卡片（孔卡）
面向每个玩家处理，然后五张公共牌面朝上放置
经销商。当我们需要确定一个球员的组合时，我们需要所有的开局。

给你一个7张牌的顺序，你应该选择最好的牌（5张牌）。
卡片序列被描述为一个字符串，其中每张卡片由两个字符定义 - 
等级和西装。卡片以逗号分隔。

降序排列：“A”（王牌），“K”（王），“Q”（女王），“J”（杰克），“T”（十）和“9”到“2”。
下降服装是“h”（心脏），“d”（钻石），“c”（俱乐部），“s”（黑桃）。

德州扑克使用古典扑克手牌名单：直冲，四种，全
房子，冲洗，直，三种，两对，一对和高卡。

由于德克萨斯州持有他们的公共牌，不同牌手的手牌
往往可以非常接近价值。因此，使用起搏器很常见
确定双手或两手以上情况下的胜手。踢球者是一张牌
是五张牌扑克牌的一部分，但不用于确定牌的等级。例如，
在手A-A-A-K-Q中，国王和王后是踢手。

在我们不同套装的德州扑克牌版本中有不同的价值。这意味着
只有一次最好的五张牌返回。所以“Td”高于“Tc”，但低于“Jc”。

你的目标是用5张牌选择最好的牌，并将它们作为一个字符串返回，其中牌是牌
用逗号分隔并从最高值到最低值进行排序。例如：我们有两双
由女王（心脏和黑桃）和八分之一（钻石和俱乐部）和九心作为踢球。该
结果：“Qh，Qs，9h，8d，8c”。订购时要小心。

输入：卡片列表作为字符串。
输出：作为一个字符串的最佳手牌。

如何使用：这个概念是组合优化过程的一个很好的例子，可以
如果您使用Python制作扑克游戏，请派上用场。

前提：
cards_quantity == 7
所有卡片都是正确和唯一的
'''