class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # fucntion to build the final letters
        def new(s):
            news= []
            for i in s:
                if len(news) == 0:
                    if i != '#':
                        news.append(i)
                else:
                    if i == '#':
                        news.pop()
                    else:
                        news.append(i)
            return news
        return new(s), new(t)

    
 class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def convert(S):
            stack = []
            for i in S:
                if i == '#':
                    try:
                        stack.pop()
                    except:
                        pass
                else:
                    stack.append(i)
            return stack
        return convert(s) == convert(t)
                
