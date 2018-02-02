'''
Find distance and direction to enemy in a HEX-grid
Input: three arguments, your corrent coordinates, your current absolute
direction, enemy's coordinates.

Output: list, relative direction to the enemy and distance to the enemy .

Example:

find_enemy('B2', 'S', 'B4') == ['F', 2]


How it is used:

War-game design using hex-grid

Precondition:
'A1' ≤ coordinates ≤ 'Z9'.
direction in ('N', 'NE', 'SE', 'S', 'SW', 'NW').
your coordinates ≠ enemy's coordinates.

在HEX网格中找到敌人的距离和方向
输入：三个参数，您的电流坐标，您当前的绝对值
方向，敌人的坐标。

输出：列表，敌人的相对方向和距离敌人的距离。

如何使用它：
使用六角网格的战争游戏设计
'''

def find_enemy(you, dir, enemy):
    pass


if __name__ == '__main__':
    assert find_enemy('G5', 'N', 'G4') == ['F', 1], "N-1"
    assert find_enemy('G5', 'N', 'I4') == ['R', 2], "NE-2"
    assert find_enemy('G5', 'N', 'J6') == ['R', 3], "SE-3"
    assert find_enemy('G5', 'N', 'G9') == ['B', 4], "S-4"
    assert find_enemy('G5', 'N', 'B7') == ['L', 5], "SW-5"
    assert find_enemy('G5', 'N', 'A2') == ['L', 6], "NW-6"
    assert find_enemy('G3', 'NE', 'C5') == ['B', 4], "[watch your six!]"
    assert find_enemy('H3', 'SW', 'E2') == ['R', 3], "right"
    assert find_enemy('A4', 'S', 'M4') == ['L', 12], "true left"
    print("You are good to go!")
