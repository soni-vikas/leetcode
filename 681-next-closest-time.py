class Solution:

    def formatTime(self, h0, h1, m0, m1):
        return "%d%d:%d%d" % (h0, h1, m0, m1)

    def nextClosestTime(self, time: str) -> str:
        # assuming time as "h1h0:m1m0"
        h0 = int(time[0])
        h1 = int(time[1])
        m0 = int(time[3])
        m1 = int(time[4])

        _min = min([h0, h1, m0, m1])

        # closest minute by changing m1:
        for i in sorted([h0, h1, m0]):
            if i > m1:
                return self.formatTime(h0, h1, m0, i)

        # closest minute by changing m0:
        for i in sorted([h0, h1, m1]):
            if i > m0 and i < 6:
                return self.formatTime(h0, h1, i, _min)

        # closest hour by changing h1:
        for i in sorted([h0, m0, m1]):
            if i > h1 and (h0 * 10 + i) < 24:
                return self.formatTime(h0, i, _min, _min)

        # closest hour by changing h0:
        for i in sorted([h1, m0, m1]):
            if i > h0 and (i * 10 + h1) < 24:
                return self.formatTime(i, _min, _min, _min)

        return self.formatTime(_min, _min, _min, _min)
