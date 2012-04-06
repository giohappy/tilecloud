import math
import time


class Statistics(object):

    def __init__(self, format='%f'):
        self.format = format
        self.n = 0
        self.sum = 0.0
        self.sum_of_squares = 0.0
        self.minimum = None
        self.maximum = None

    def add(self, x):
        self.n += 1
        self.sum += x
        self.sum_of_squares += x * x
        self.minimum = x if self.minimum is None else min(self.minimum, x)
        self.maximum = x if self.maximum is None else max(self.maximum, x)

    def __str__(self):
        result = []
        if self.n:
            result.append('/'.join(self.format % value for value in (self.minimum, self.mean, self.maximum)))
        result.append('(n=%d)' % (self.n,))
        return ' '.join(result)

    @property
    def mean(self):
        return self.sum / self.n if self.n else None

    @property
    def variance(self):
        return self.sum_of_squares / self.n - (self.sum / self.n) ** 2

    @property
    def standard_deviation(self):
        return math.sqrt(self.variance)


class Benchmark(object):

    def __init__(self, attr='benchmark'):
        self.attr = attr
        self.statisticss = {}

    def sample(self, key=None):
        if key:
            if key in self.statisticss:
                statistics = self.statisticss[key]
            else:
                statistics = Statistics('%.3fs')
                self.statisticss[key] = statistics
        else:
            statistics = None

        def callback(tile):
            if tile:
                if hasattr(tile, self.attr):
                    times = getattr(tile, self.attr)
                    times.append(time.time())
                    if statistics:
                        statistics.add(times[-1] - times[-2])
                else:
                    setattr(tile, self.attr, [time.time()])
            return tile
        return callback
