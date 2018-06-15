'''
Nicola has built a semi-automatized painting system, but this system can paint only one side of an item. After that, an operator must reload the machine and paint the other side (the system detects painted sides automatically). The painting process always takes the same amount of time. The camera can paint K surfaces at a time. Nicola wants Stephan to operate the painting machine and he needs to develop an algorithm for Stephan which will allow him to paint N (0 < N ≤ 10) surfaces in the shortest possible timeframe. Be careful that you don't paint the item more than two times.

system
The items are numbered from 0 to 9. You are given the paint holding capacity of the machine (K) and the quantity of items (N). You should return the sequence Stephen must paint as a string, where each action is the numbers of painted items. Actions separated by comma (",").

Input: Capacity of the painting system and quantity of items as integers.

Output: The sequence of actions as a string.

Example:

checkio(2, 3)  # "01,12,02"
checkio(6, 3)  # "012,012"
checkio(3, 6)  # "012,012,345,345"
checkio(1, 4)  # "0,0,1,1,2,2,3,3"
checkio(2, 5)  # "01,01,23,42,34"
    
How it is used: This is similar to cooking three steaks in one frying pan. Each steak has two sides and it takes a minute to cook one side of two steaks, how would you cook all steaks in three minutes? This task takes the concept and models it in a technical way. The ideas behind the task also model real technological process in a factories.

Precondition:
0 < capacity ≤ 10
0 < number ≤ 10
'''
