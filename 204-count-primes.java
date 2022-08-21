class Solution {
    public int countPrimes(int n) {
        boolean arr[] = new boolean[n];
        for (int i=0; i<n; i++) {
            arr[i] = true;
        }
        
        int res = 0;
        for (int i=2; i<n; i++) {
            if (arr[i]) {
                res += 1;
                arr[i] = false;
                if ((long)i * i < Integer.MAX_VALUE) {
                    int j = i * i;
                    while (j < n) {
                        arr[j] = false;
                        j += i;
                    }
                }
            }
        }
        return res;
    }
}
