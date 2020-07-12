class Case:
    def __init__(self, bought, limit_per_day, bucket):
        self.bought = bought
        self.limit_per_day = limit_per_day
        self.consumed = 0
        self.bucket = bucket

    def consume(self):
        for i in range(self.bought, 0, -1):
            today = min(self.limit_per_day, self.bucket[i])
            self.consumed += today
            self.bucket[i-1] += self.bucket[i] - today
        return self.consumed


t = int(input())
for i in range(1, t + 1):
    bought, limit_per_day = [int(j) for j in input().split()]
    bucket = [0] * (bought + 1)
    for expire_day in input().split():
        ed = int(expire_day)
        if ed > bought:
            ed = bought
        bucket[ed] += 1
    case = Case(bought, limit_per_day, bucket)
    # print(f'Case #{i}: {case.consume()}')
    print('Case #{}: {}'.format(i, case.consume()))
