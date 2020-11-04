# 我们可以发现分数不是最简分数，所以需要约分
def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n