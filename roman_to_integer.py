# https://leetcode.com/problems/roman-to-integer/
# Roman To integer (Easy) Problem
def romanToInt(s: str) -> int:
    m = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    res = 0
    for i in range(len(s)):
        if i + 1 < len(s) and m[s[i]] < m[s[i+1]]:
            res -= m[s[i]]
        else:
            res += m[s[i]]
    print(res)
romanToInt("IX")