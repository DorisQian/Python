'''
In this time, you need to implement the solver of Lights Out the puzzle.

rule of the puzzle :

This puzzle uses 5x5 grid. Each panel has two state ( light on or off ).
if you click a panel, the panel and adjacent (4 directions) panels will flip. ( on <=> off )
The goal is all panels lights off.


Input: ON-state panels as a list of Integers.

Output: Clicked panels as a list of Integers.

Example:

wall_keeper([5, 7, 13, 14, 18]) == [2, 6, 7, 8, 10, 12, 15, 18, 24, 25]
1
How it is used: Get the puzzle's automatic answer.

Precondition:
all([1 <= p <= 25 for p in on_panels])
It does not have to be the shortest answer
'''
def wall_keeper(on_panels):
    return []

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    from itertools import chain


    def checker(solution, on_panels):
        answer = solution(on_panels)
        wk_p = list((0, 1)[n in on_panels] for n in range(1, 26))
        p = list(wk_p[n: n+5] for n in range(0, 25, 5))
        for a in answer:
            r, c = (a-1) // 5, (a-1) % 5
            p[r][c] = 1 - p[r][c]
            if r+1 < 5:
                p[r+1][c] = 1 - p[r+1][c]
            if r-1 > -1:
                p[r-1][c] = 1 - p[r-1][c]
            if c+1 < len(p[0]):
                p[r][c+1] = 1 - p[r][c+1]
            if c-1 > -1:
                p[r][c-1] = 1 - p[r][c-1]
        return sum(chain(*p)) == 0

    assert checker(wall_keeper, [5, 7, 13, 14, 18]), 'basic'
    assert checker(wall_keeper, list(range(1, 26))), 'all_lights'


