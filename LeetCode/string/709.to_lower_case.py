'''
给定一个字符串 s，将每个大写字母替换为相同的小写字母后返回该字符串。
'''
# 内置方法
class SolutionLower:
    def toLowerCase(self, s: str) -> str:
        return s.lower()
# 位操作
class SolutionBit:
    def toLowerCase(self, s: str) -> str:
        return ''.join(chr(ord(c)|32) if 65<=ord(c) <=90 else c for c in s )
if __name__ == '__main__':
    while True:
        try:
            input_str = input()
            print(SolutionBit().toLowerCase(input_str))
        except Exception as e:
            print(e)
            break