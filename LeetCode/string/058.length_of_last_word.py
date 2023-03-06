'''
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.
给定一个由单词和空格组成的字符串 s，返回字符串中最后一个单词的长度。
一个字是最大的子串
仅由非空格字符组成
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
if __name__ == '__main__':
    while True:
        try:
            words = input()
            print(Solution().lengthOfLastWord(words))
        except Exception as e:
            print(e)
            break