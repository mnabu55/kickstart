'''
Problem
Isyana is given the number of visitors at her local theme park on N consecutive days. The number of visitors on the i-th day is Vi. A day is record breaking if it satisfies both of the following conditions:
The number of visitors on the day is strictly larger than the number of visitors on each of the previous days.
Either it is the last day, or the number of visitors on the day is strictly larger than the number of visitors on the following day.
Note that the very first day could be a record breaking day!

Please help Isyana find out the number of record breaking days.

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a line containing the integer N. The second line contains N integers. The i-th integer is Vi.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the number of record breaking days.

Limits
Time limit: 20 seconds per test set.
Memory limit: 1GB.
1 ≤ T ≤ 100.
0 ≤ Vi ≤ 2 × 105.

Test set 1
1 ≤ N ≤ 1000.

Test set 2
1 ≤ N ≤ 2 × 105 for at most 10 test cases.
For the remaining cases, 1 ≤ N ≤ 1000.

Sample

Input

Output

4
8
1 2 0 7 2 0 2 0
6
4 8 15 16 23 42
9
3 1 4 1 5 9 2 6 5
6
9 9 9 9 9 9


Case #1: 2
Case #2: 1
Case #3: 3
Case #4: 0
'''


class Case:
    def __init__(self, days, visitors):
        self.days = days
        self.visitors = visitors
        self.record_break_days = 0

    def get_break_day(self):
        previous_record = 0

        for i in range(len(self.visitors)):
            greater_than_previous_days = i == 0 or self.visitors[i] > previous_record
            greater_than_following_days = i == len(self.visitors) - 1 or self.visitors[i] > self.visitors[i + 1]
            if greater_than_previous_days and greater_than_following_days:
                self.record_break_days += 1
            previous_record = max(previous_record, self.visitors[i])
        return self.record_break_days


t = int(input())
for i in range(1, t + 1):
    days = int(input())
    visitors = [int(x) for x in input().split()]
    case = Case(days, visitors)
    print('Case #{}: {}'.format(i, case.get_break_day()))
