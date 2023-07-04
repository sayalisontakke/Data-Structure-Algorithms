class Solution(object):
    def getSum(self, a, b):
        while b != 0:
            carry = a & b  # calculate the carry bits
            a = a ^ b      # calculate the sum without carry
            b = carry << 1  # shift the carry to the left by 1 position
        return a
