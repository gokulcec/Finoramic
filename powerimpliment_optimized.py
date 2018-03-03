class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        if n==0:
            return 1
        power= self.pow(x,n/2,d)
        return abs((x*power*power)%d) if (n &1 ) else (power*power)%d
        
