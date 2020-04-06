class Frange:

    def __init__(self, start, stop, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step
        self.lst = []

    def __iter__(self):
        while self.start < self.stop:
            self.lst.append(self.start)
            self.start += self.step
        return iter(self.lst)


frange = Frange(0.25, 5.75, 0.1)

for i in frange:
    print(i)

