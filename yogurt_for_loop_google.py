class Case:
    def __init__(self, bought, limit_per_day, yogurt_expiration):
        self.bought = bought
        self.limit_per_day = limit_per_day
        self.yogurt_expiration = sorted(yogurt_expiration)
        self.consumed = 0

    def consume(self):
        consumed_today = 0
        day = 0
        for i in range(bought):
            if consumed_today == limit_per_day:
                day += 1
                consumed_today = 0

            if yogurt_expiration[i] > day:
                consumed_today += 1
                self.consumed += 1

        return self.consumed


t = int(input())
for i in range(1, t + 1):
    bought, limit_per_day = [int(j) for j in input().split()]
    yogurt_expiration = [int(k) for k in input().split()]
    case = Case(bought, limit_per_day, yogurt_expiration)
    print(f'Case #{i}: {case.consume()}')
