"""
Sofia has had a very stressful month and decides to take a vacation for a week. To avoid any stress during her vacation she wants to forward any email with stressful subject lines to Stephen.
The function should recognise if a subject line is stressful. A stressful subject line means that all letters are uppercase, and/or ends by at least 3 exclamation marks and/or contains at least one of the following “red” words "help", "asap", "urgent". Any of those "red" words can be spelled in different ways - "HELP", "help", "HeLp", "H!E!L!P!", "H-E-L-P", even in a very loooong way "HHHEEEEEEEEELLP"
Input: Subject line as a string
Output: Boolean.
Example:

is_stressful("Hi") == False
is_stressful("I neeed HELP") == True

Precondition: subject can be up to 100 letters

索菲亚度过了一个充满压力的一个月，决定休一个星期的假。为了避免在休假期间出现压力，她想把任何有压力的邮件转发给斯蒂芬。
这个功能应该能识别出一个主题是否有压力。一个有压力的主题行意味着所有的字母都是大写的，并且/或结尾至少有三个感叹号和/或至少包含下列“红色”单词中的一个“帮助”，“asap”，“紧急”。任何一个“红色”字都可以用不同的方式拼写出来——“帮助”、“帮助”、“帮助”、“H !E!，“h - e - l - p”，即使是非常非常的“hhheeeeeeellp”
输入:主题行作为字符串
输出:布尔。

先决条件:subject可以多达100个字母
"""


def is_stressful(subj):
    """
        recoognise stressful subject
    """
    if subj.isupper():return True
    elif subj.endswith('!!!'):return True
    else:
#    	newsubj=(''.join(w for w in subj if w.isalpha())).lower()
    	newsubj = subj.replace(',',' ').lower().split()
#    	print(newsubj)
    	for i in newsubj:
    		word = ''.join(w for w in i if w.isalpha())           
    		seq=sorted(set(word),key=word.index)
    		wo = ''
    		for w in seq:
    			wo += w
#    		print(wo)
    		if wo in ('help','asp','urgent'):
    			return True
    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    assert is_stressful("I need your,hE-lp")==True,"third"
    assert is_stressful("hey!!!")== True,"forth"
    assert is_stressful("i need your,HHHEEEEEEEEELLP") == True,"fivth"
    assert is_stressful("We need you A.S.A.P.!!") == True,"asap"
    print('Done! Go Check it!')

