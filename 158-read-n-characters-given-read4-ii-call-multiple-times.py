# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

new_buf = lambda: [" " for i in range(4)]


class Solution:

    def __init__(self):
        self.buf4 = new_buf()
        self.i = 0
        self.n4 = read4(self.buf4)

    def read4(self):
        self.i = 0
        self.n4 = read4(self.buf4)

    def read(self, buf: List[str], n: int) -> int:
        i = 0
        if self.n4 == 0:
            return i

        while i < n:
            if self.i < self.n4:
                buf[i] = self.buf4[self.i]
                self.i += 1
                i += 1

            else:
                self.read4()
                if self.n4 == 0:
                    return i

        return i
