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
  call = list(calls)
  time = []
  for n in calls:
    if n.split(' ')[0] not in same_day:
      time.append(int(n.split(' ')[-1]))
      call.remove(n)
  for s in same_day:
    count = 0
    for n in call:
      if n.split(' ')[0] == s:
        count += int(n.split(' ')[-1])
    time.append(count)
  print(time)
'''
def count_call(num):
  if num % 60 == 0:
    time = num / 60
    if time <= 100:
      cou = time
    else:
      cou = 100 + 2 * (time - 100)
  else:
    time = num // 60 + 1
    if time <= 100:
      cou = time
    else:
      cou = 100 + 2 * (time - 100)
  return cou, time

def count_after(num):
  if num % 60 == 0:
    time = num / 60
    cou = time * 2
  else:
    time = num // 60 + 1
    cou = 2 * time
  return cou, time

def total_cost(calls):
  date = [d.split(' ')[0] for d in calls]
  same_day = set([d for d in date if date.count(d) > 1])
  print(same_day)
  count = 0
  call = list(calls)
  for d in calls:
    if d.split(' ')[0] not in same_day:
      count += count_call(int(d.split(' ')[-1]))[0]
      call.remove(d)
  for t in same_day:
    second = 0
    for c in call:
      if c.split(' ')[0] == t:
        if second * 60 + int(c.split(' ')[-1]) < 6000:
          cost, time = count_call(int(c.split(' ')[-1]))
          #count += count_call(int(c.split(' ')[-1]))
          count += cost
          #second += int(c.split(' ')[-1])
          second += time
        elif second > 100:
          #count += count_after(int(c.split(' ')[-1]))
          #second += int(c.split(' ')[-1])
          cost, time = count_after(int(c.split(' ')[-1]))
          count += cost
          second += time
        elif second == 0 and int(c.split(' ')[-1]) > 6000:
            #count += count_call(int(c.split(' ')[-1]))
            #second += int(c.split(' ')[-1])
            cost, time = count_call(int(c.split(' ')[-1]))
            count += cost
            second += time
        else:
          count += count_call(6000 - second * 60)[0]
          b = int(c.split(' ')[-1]) - (6000 - second * 60)
          count += count_after(b)[0]
          second += count_call(6000 - second * 60)[1] + count_after(b)[1]
  print(count)
  return count




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
    
    assert total_cost(["2054-07-17 10:21:08 1958",
      "2054-07-17 16:17:18 1388",
      "2054-07-18 00:30:57 729",
      "2054-07-18 03:55:30 4970",
      "2054-07-18 23:10:05 5397",
      "2054-07-19 16:37:31 5894",
      "2054-07-20 11:21:10 2537",
      "2054-07-20 17:09:49 4398",
      "2054-07-21 04:17:34 2839",
      "2054-07-21 06:23:25 6229",
      "2054-07-21 10:21:01 4540",
      "2054-07-21 22:10:46 5599",
      "2054-07-22 11:26:43 6199",
      "2054-07-23 02:02:52 818",
      "2054-07-23 14:30:19 3244",
      "2054-07-23 20:46:25 380",
      "2054-07-24 08:41:40 4774",
      "2054-07-24 23:33:14 5206",
      "2054-07-25 08:47:44 3848",
      "2054-07-25 11:32:40 694",
      "2054-07-25 18:28:25 5974",
      "2054-07-26 09:24:52 4550",
      "2054-07-26 13:06:07 6637",
      "2054-07-27 09:03:40 177",
      "2054-07-27 13:11:42 5736",
      "2054-07-27 15:53:26 5698",
      "2054-07-28 09:51:43 1996",
      "2054-07-28 14:03:30 432"]) == 2382
