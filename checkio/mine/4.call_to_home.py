'''
Nicola believes that Sophia calls to Home too much and her phone bill is 
much too expensive. He took the bills for Sophia's calls from the last 
few days and wants to calculate how much it costs.

The bill is represented as an array with information about the calls. 
Help Nicola to calculate the cost for each of Sophia calls. Each call 
is represented as a string with date, time and duration of the call in 
seconds in the follow format:
"YYYY-MM-DD hh:mm:ss duration"
The date and time in this information are the start of the call.
Space-Time Communications Co. has several rules on how to calculate the cost of calls:

First 100 (one hundred) minutes in one day are priced at 1 coin per minute;
After 100 minutes in one day, each minute costs 2 coins per minute;
All calls are rounded up to the nearest minute. For example 59 sec ≈ 1 min, 61 sec ≈ 2 min;
Calls count on the day when they began. For example if a call was started 
2014-01-01 23:59:59, then it counted to 2014-01-01;
For example:

2014-01-01 01:12:13 181
2014-01-02 20:11:10 600
2014-01-03 01:12:13 6009
2014-01-03 12:13:55 200
First day -- 181s≈4m -- 4 coins;
Second day -- 600s=10m -- 10 coins;
Third day -- 6009s≈101m + 200s≈4m -- 100 + 5 * 2 = 110 coins;
Total -- 124 coins.
Input: Information about calls as a tuple of strings.

Output: The total cost as an integer.

Example:

total_cost(("2014-01-01 01:12:13 181",
            "2014-01-02 20:11:10 600",
            "2014-01-03 01:12:13 6009",
            "2014-01-03 12:13:55 200")) == 124
    
How it is used: This mission will teach you how to parse and analyse various 
types data. Sometimes you don't need the full data and should single out only important fragments.

Precondition: 0 < len(calls) ≤ 30
0 < call_duration ≤ 7200
The bill is sorted by datetime.

尼古拉认为，索菲娅太多呼吁回家，她的电话费是
太贵了。 他从最后一次拿索菲亚的电话
几天，想要计算多少成本。

账单被表示为一个有关呼叫信息的数组。
帮助尼古拉计算每个索菲亚电话的费用。 每次通话
被表示为具有日期，时间和呼叫持续时间的字符串
秒的格式如下：
“YYYY-MM-DD hh：mm：ss duration”
这个信息的日期和时间是通话的开始。
Space-Time Communications Co.在如何计算通话费用方面有几条规定：

一天前一百（一百）分钟的价格是每分钟1硬币;
一天100分钟后，每分钟每分钟2个硬币;
所有通话都会四舍五入到最接近的分钟。 例如59秒≈1分钟，61秒≈2分钟;
通话计数在他们开始的那一天。 例如，如果一个电话开始
2014-01-01 23:59:59，到2014-01-01为止;

如何使用：这个任务将教你如何解析和分析各种
类型数据。 有时你不需要完整的数据，只能挑出重要的片段。
'''
def total_cost(calls):
    return 0


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert total_cost(("2014-01-01 01:12:13 181",
                       "2014-01-02 20:11:10 600",
                       "2014-01-03 01:12:13 6009",
                       "2014-01-03 12:13:55 200")) == 124, "Base example"
    assert total_cost(("2014-02-05 01:00:00 1",
                       "2014-02-05 02:00:00 1",
                       "2014-02-05 03:00:00 1",
                       "2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    assert total_cost(("2014-02-05 01:00:00 60",
                       "2014-02-05 02:00:00 60",
                       "2014-02-05 03:00:00 60",
                       "2014-02-05 04:00:00 6000")) == 106, "Precise calls"
