"""
Michael always knew that there was something wrong with his family. Many strangers were introduced to him as part of his family.

Michael should figure this out. He spent almost a month parsing family archives. He has all father-son connections of his entire family collected in one place.

With all that data Michel can easily understand who the strangers are. Or maybe the only stranger in this family is Michael? Let’s see.

You have a list of family relationships between father and son. Every element on this list has two elements. The first is the father's name, the second is a son’s name. All names in the family are unique. Check if the family tree is correct. There are no strangers in the family tree. All connections in the family are natural.

Input: list of lists. Every element has two strings. List has at least one element

Output: bool. Is family tree correct.



Example:

is_family([
  ['Logan', 'Mike']
]) == True
is_family([
  ['Logan', 'Mike'],
  ['Logan', 'Jack']
]) == True
is_family([
  ['Logan', 'Mike'],
  ['Logan', 'Jack'],
  ['Mike', 'Alexander']
]) == True
is_family([
  ['Logan', 'Mike'],
  ['Logan', 'Jack'],
  ['Mike', 'Logan']
]) == False  # Can you be a father for your father?
is_family([
  ['Logan', 'Mike'],
  ['Logan', 'Jack'],
  ['Mike', 'Jack']
]) == False  # Can you be a father for your brother?
is_family([
  ['Logan', 'William'],
  ['Logan', 'Jack'],
  ['Mike', 'Alexander']
]) == False  # Looks like Mike is stranger in Logan's family

Precondition: 1 <= len(tree) < 100

迈克尔总是知道他的家庭出了问题。许多陌生人被介绍给他作为他的家庭的一部分。
迈克尔应该明白这一点。他花了将近一个月的时间分析家庭档案。他的整个家庭的父子关系都集中在一个地方。
米歇尔很容易就能理解陌生人是谁。或者这个家里唯一的陌生人是迈克尔?让我们来看看。
你有一份父亲和儿子之间的家庭关系清单。这个列表中的每个元素都有两个元素。第一个是父亲的名字，第二个是儿子的名字。家中所有的名字都是独一无二的。检查家谱是否正确。在家谱中没有陌生人。家庭中的一切关系都是自然的。

输入:列表的列表。每个元素都有两个字符串。列表至少有一个元素
输出:bool。家谱是正确的。
"""

def is_family(tree):
    return True


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_family([
      ['Logan', 'Mike']
    ]) == True, 'One father, one son'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack']
    ]) == True, 'Two sons'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Alexander']
    ]) == True, 'Grandfather'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Logan']
    ]) == False, 'Can you be a father for your father?'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Jack']
    ]) == False, 'Can you be a father for your brather?'
    assert is_family([
      ['Logan', 'William'],
      ['Logan', 'Jack'],
      ['Mike', 'Alexander']
    ]) == False, 'Looks like Mike is stranger in Logan\'s family'
    print("Looks like you know everything. It is time for 'Check'!")

