class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        先去掉非数字字母，然后首尾逐字比较
        '''
        st = "".join(filter(str.isalnum, s)).lower()
        i, j = 0, len(st)-1

        while i < j:
            if st[i] != st[j]:
                return False
            i += 1
            j -= 1
        return True


class SolutionOneCycle:
    def isPalindrome(self, s: str) -> bool:
        '''
        一次循环，跳过非数字字母
        '''
        i, j = 0, len(s)-1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True


class SolutionStrComp:
    def isPalindrome(self, s: str) -> bool:
        st = "".join(filter(str.isalnum, s)).lower()
        lh = int(len(st)/2)
        if lh == 0:
            return True
        f, b = st[:lh], st[-lh:]
        return f == ''.join(b[len(b)-i-1] for i in range(len(b)))


if __name__ == '__main__':
    while True:
        try:
            s = input().strip('"')
            print(SolutionStrComp().isPalindrome(s))
        except Exception as e:
            print(e)
            break
