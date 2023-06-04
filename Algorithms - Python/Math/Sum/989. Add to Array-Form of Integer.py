class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # this approach would exceed the limit (4300) for integer string conversion
        # new_num = int(''.join([str(i) for i in num])) + k
        # return [int(i) for i in str(new_num)]
        nlen = len(num)
        nk = len(str(k))
        if nlen > nk:
            k = str(k)[::-1] + '0'*(nlen - nk)
        else:
            k = str(k)[::-1]
            num = [0] * (nk - nlen) + num
            nlen = len(num)
        for ind, ki in enumerate(k):
            ki = int(ki)
            #print(ki)
            num[nlen - ind - 1] += ki
            print(num[nlen - ind - 1])
            # increment previous digit when exceeding 10
            if num[nlen - ind - 1] >= 10:
                num[nlen - ind - 1] -= 10
                prev_dig = nlen - ind - 2
                if prev_dig >= 0:
                    num[prev_dig] += 1
                else:
                    num = [1] + num
        return num
