class Case:
    def __init__(self, bought, limit_per_day, yogurt_expiration):
        self.bought = bought
        self.limit_per_day = limit_per_day
        self.consumed = 0
        self.yogurt_expiration = sorted(yogurt_expiration)
        

    def consume(self):

        for i in range(self.bought - 1, -1, -1):
            today = min(self.limit_per_day, self.yogurt_expiration[i])
            self.consumed += today
            self.yogurt_expiration[i-1] += self.yogurt_expiration[i] - today
        return self.consumed


t = int(input())
for i in range(1, t + 1):
    bought, limit_per_day = [int(j) for j in input().split()]
    yogurt_expiration = [int(k) for k in input().split()]
    case = Case(bought, limit_per_day, yogurt_expiration)
    print(f'Case #{i}: {case.consume()}')



'''
4
2 1
1 1
5 1
3 2 3 2 3
2 2
1 1
6 2
1 1 1 7 7 7
'''