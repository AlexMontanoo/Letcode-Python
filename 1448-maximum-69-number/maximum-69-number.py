class Solution:
    def maximum69Number (self, num: int) -> int:
        
        s_num = list(str(num))
        for i, digit in enumerate(s_num):
            if digit == '6':
                s_num[i] = '9'
                break
        return int("".join(s_num))