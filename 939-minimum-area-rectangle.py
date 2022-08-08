from typing import List

MAX_AREA = 10 ** 10


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        point_set = {}
        for x, y in points:
            point_set[x] = point_set.get(x, set())
            point_set[x].add(y)

        # a ----- b
        # |       |
        # |       |
        # d ----- c

        min_area = MAX_AREA

        # visited = set()
        n = len(points)
        for i in range(n - 1):
            for j in range(i + 1, n):
                a = points[i]
                c = points[j]
                if a[0] != c[0] and a[1] != c[1]:
                    b = (a[0], c[1])
                    d = (c[0], a[1])
                    if (b[0] in point_set and b[1] in point_set[b[0]]) and (
                            d[0] in point_set and d[1] in point_set[d[0]]):
                        min_area = min(min_area, abs(c[1] - a[1]) * abs(c[0] - a[0]))

        return 0 if min_area == MAX_AREA else min_area


# Python Solution might return TLE for larger input. Here is the java solution with same logic.

"""

// Java Solution

class Solution {
    public int minAreaRect(int[][] points) {
        HashMap<Integer, HashSet<Integer>> map = new HashMap<Integer, HashSet<Integer>>();
        for (int[] p: points) {
            if (!map.containsKey(p[0])) {
                map.put(p[0], new HashSet<Integer>());
            }

            map.get(p[0]).add(p[1]);
        }

        int res = Integer.MAX_VALUE;

        for (int i=0; i<points.length-1; i++) {
            for (int j=i+1; j<points.length; j++) {
                int[] a = points[i];
                int[] c = points[j];
                int[] b = new int[]{a[0], c[1]};
                int[] d = new int[]{c[0], a[1]};
                if (
                    a[0] != c[0] && a[1] != c[1] &&
                    (map.containsKey(b[0]) && map.get(b[0]).contains(b[1])) &&
                    (map.containsKey(d[0]) && map.get(d[0]).contains(d[1]))
                ) {
                    res = Math.min(res, Math.abs(a[1] - c[1]) * Math.abs(a[0] - c[0]));
                }
            }
        }

        if (res == Integer.MAX_VALUE) {
            return 0;
        }

        return res;
    }
}

"""
