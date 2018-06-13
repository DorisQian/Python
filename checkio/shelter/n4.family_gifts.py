'''
Every Christmas in my family, each of us gives a present to only one other person. 
To organize who should offer a gift to whom (I call it the chain of presents), we introduced a few rules:

- There should be a single chain where every person in the family is present,
- Couples should not give to one another,
- Every person should give a gift to a different person than they had in previous years

So the problem would be to find and list the longest list of chains of presents. For 
example in a family {a,b,c,d} with couples=({a,b},{c,d}): [[a,c,b,d],[a,d,b,c]].

You are given a set of family member names and a list of couples in this family. Find 
the maximum number of chains with all family members. Gift chains should be represented 
as a list of names where i-th gives a present to i+1-th and the last person in the list to the first.

Input: Names of family members as a set of strings. Couple list as a tuple of sets with two strings in each.

Output: The longest list of gift chains as a list/tuple of lists/tuples with strings.

Example:

find_chains({'Gary', 'Jeanette', 'Hollie'}, ({'Gary', 'Jeanette'},)) # 0 chains
find_chains({'Curtis', 'Lee', 'Rachel', 'Javier'}, ({'Rachel', 'Javier'}, {'Curtis', 'Lee'})) # 2 chains
How it is used: This is a combinatorial task that can be useful for scheduling.

Precondition:

len(couples) <= 7

家人每逢圣诞节，我们每个人都只送一份礼物给另一个人。
为了组织谁应该为谁送礼（我称之为礼物链），我们引入了一些规则：

- 家庭中的每个人都应该有一个单链，
- 夫妻不应该互相给予，
- 每个人都应该送礼给不同于往年的人

所以问题是找到并列出礼物链最长的列表。对于
[a，c，b，d]，[a，d，b，c]中的夫妻= {{a，b}，{c，d} ]。

给你一套家庭成员名字和这个家庭的夫妻名单。找
与所有家庭成员的最大连锁数量。礼品链应该被代表
作为第i个给第i + 1个礼物并且列表中的最后一个人给第1个礼物的名字列表。

输入：家庭成员的姓名作为一组字符串。耦合列表作为每个集合中包含两个字符串的元组。
输出：作为包含字符串的列表/元组的列表/元组的礼品链的最长列表。

它是如何使用的：这是一个可以用于调度的组合任务。
'''