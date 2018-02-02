'''
The mission is in Reviewing Mode. You can't see the solutions Leader Board, 
but you can see other user solutions through the Random Review after you 
solve the mission.
﻿

Gerrymandering is a practice intended to establish a political advantage 
for a particular party or group by manipulating district boundaries. The 
resulting district is known as a gerrymander (/ˈdʒɛriˌmændər/); however, 
that word can also refer to the process. The term gerrymandering has negative 
connotations. Two principal tactics are used in gerrymandering: "cracking" 
(i.e. diluting the voting power of the opposing party's supporters across 
many districts) and "packing" (concentrating the opposing party's voting 
power in one district to reduce their voting power in other districts).

In addition to its use achieving desired electoral results for a particular 
party, gerrymandering may be used to help or hinder a particular demographic, 
such as a political, ethnic, racial, linguistic, religious, or class group, 
such as in U.S. federal voting district boundaries that produce a majority 
of constituents representative of African-American or other racial minorities, 
known as "majority-minority districts". Gerrymandering can also be used to protect incumbents.

Read more about it on wikipedia or watch this episode Gerrymandering: 
Last Week Tonight with John Oliver (HBO)

You have a map of units. Every unit has two elements (amount of people voted 
for candidate A and amount of people voted for candidate B). Your mission is 
to split a given area on X amount of districts in such a way so candidate A 
gets more districts voted for him than candidate B.

There are two main rules of building districts. All districts should have same 
amount of people. All units should be connected inside of one district.

Input: Two arguments. Amount of people for each district (as integer) , grid of 
all electoral zone (as list of list (each unit has [A-peoples, B-peoples]))

Output: united districts (as List of string). The same letters of string represents 
the same district. If candidate A can not win more, return empty list([]).

Example:

unfair_districts(5, [[[2, 1], [1, 1], [1, 2]],
                     [[2, 1], [1, 1], [0, 2]]]) == ['AAC',
                                                    'BBC]


unfair_districts(9, [[[0, 3], [3, 3], [1, 1]],
                     [[1, 2], [1, 0], [1, 1]],
                     [[0, 3], [2, 1], [2, 2]]]) == ['ABB',
                                                    'ABC',
                                                    'ACC'] 

Precondition:
2 ≤ grid_rows, grid_columns ≤ 6
4 ≤ grid_rows * grid_columns ≤ 25
Total_population % amuout_of_people == 0
Total_population == sum(sum(unit) for unit in chain(*grid))
0 ≤ each_votes ≤ 9

任务处于审阅模式。你看不到解决方案领袖委员会，但您可以通过随机审阅查看其他用户解决方案
解决使命。


Gerrymandering是一种旨在建立政治优势的做法通过操纵地区边界，为特定的政党或集团。该
由此产生的地区被称为gerrymander（/dʒɛriˌmændər/）;然而，
这个词也可以指这个过程。 gerrymandering这个词是负面的
内涵。在gerrymandering中使用了两个主要的策略：“破解”
（即削弱对方支持者的投票权许多地区）和“包装”（集中对方的投票
在一个地区的权力，以减少其他地区的投票权）。

除了使用达到特定的所需选举结果党派，gerrymandering可能被用来帮助或阻碍特定的人口，
如政治，种族，种族，语言，宗教或阶级群体，例如在产生多数的美国联邦投票区边界
代表非裔美国人或其他少数族裔的三方成员，被称为“多数少数民族地区”。 
Gerrymandering也可以用来保护在职者。

在wikipedia上阅读更多关于它的信息或观看本集Gerrymandering：
上周与约翰奥利弗（HBO）今晚

你有一个单位的地图。每个单位都有两个要素（人数投票为候选人A和人数投票候选人B）。你的任务是
以这样一种方式在X个区域上划分给定区域，使得候选人A得到更多的地区投票给他比候选人B.

有两个建设区的主要规则。所有地区都应该有人数。所有单位应该连接在一个地区的内部。

输入：两个参数。每个区的人数（如整数），网格所有选举区（列表清单（每个单位都有[A族，B族]））

输出：联合区（如字符串列表）。字符串的相同字母表示
同一个地区如果候选人A不能赢得更多，则返回空列表（[]）。
'''

def unfair_districts(amount_of_people, grid):

    return []

if __name__ == '__main__':

    from itertools import chain
    from collections import defaultdict

    def checker(solution, amount_of_people, grid, win_flg=True):

        w, h = len(grid[0]), len(grid)
        size = w * h
        cell_dic = {}

        # make cell_dic
        def adj_cells(cell):
            result = []
            if cell % w != 1 and cell - 1 > 0:
                result.append(cell - 1)
            if cell % w and cell + 1 <= size:
                result.append(cell + 1)
            if (cell - 1) // w:
                result.append(cell - w)
            if (cell - 1) // w < h - 1:
                result.append(cell + w)
            return set(result)

        for i, v in enumerate(chain(*grid)):
            cell_dic[i + 1] = {'vote': v, 'adj': adj_cells(i + 1)}

        answer = solution(amount_of_people, grid)

        if answer == [] and not win_flg:
            return True

        if not isinstance(answer, list):
            print('wrong data type :', answer)
            return False
        else:
            if len(answer) != h:
                print('wrong data length', answer)
                return False
            for an in answer:
                if len(an) != w:
                    print('wrong data length', an)
                    return False

        ds_dic = defaultdict(list)
        for i, r in enumerate(''.join(answer), start=1):
            ds_dic[r].append(i)

        # answer check
        def district_check(d):
            all_cells = set(d[1:])
            next_cells = cell_dic[d[0]]['adj'] & set(d)
            for _ in range(len(d)):
                all_cells -= next_cells
                next_cells = set(chain(*[list(cell_dic[nc]['adj']) for nc in next_cells])) & set(d)
            return not all_cells

        for ch, cells in ds_dic.items():
            dist_people = sum(sum(cell_dic[c]['vote']) for c in cells)
            if not district_check(cells):
                print('wrong district: ', ch)
                return False
            if dist_people != amount_of_people:
                print('wrong people:', ch)
                return False

        # win check
        win, lose = 0, 0
        for part in ds_dic.values():
            vote_a, vote_b = 0, 0
            for p in part:
                a, b = cell_dic[p]['vote']
                vote_a += a
                vote_b += b
            win += vote_a > vote_b
            lose += vote_a < vote_b

        return win > lose

    assert checker(unfair_districts, 5, [
        [[2, 1], [1, 1], [1, 2]],
        [[2, 1], [1, 1], [0, 2]]]), '3x2grid'

    assert checker(unfair_districts, 9, [
        [[0, 3], [3, 3], [1, 1]],
        [[1, 2], [1, 0], [1, 1]],
        [[0, 3], [2, 1], [2, 2]]]), '3x3gid'

    assert checker(unfair_districts, 8, [
        [[1, 1], [2, 0], [2, 0], [3, 3]],
        [[1, 1], [1, 2], [1, 1], [0, 3]],
        [[1, 1], [1, 1], [1, 2], [0, 3]],
        [[1, 1], [1, 1], [1, 1], [2, 0]]]), '4x4gid'

    print('check done')

