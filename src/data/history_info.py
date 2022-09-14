class code_info:
    infos = list()
    code = ""

class history_info:
    code = ""
    date = ""
    open = 0
    close = 0
    high = 0
    low = 0
    volume = 0
    total = 0
    range = 0
    raise_volume = 0
    raise_total = 0
    exchange = 0

    def __str__(self):
        return '(%s %s %f %f %f %f %f %f %f %f %f %f )' % (
        self.code, self.date, self.open, self.close, self.high, self.low,
        self.volume, self.total, self.range, self.raise_volume, self.raise_total, self.exchange)
