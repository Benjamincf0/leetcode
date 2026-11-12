class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        s = {letter for word in words for letter in word}
        # print(s)
        d = defaultdict(set)
        prevs = defaultdict(set)

        self.is_shit = False
        
        def dfs(depth, l, r):
            if l >= r: return
            for i in range(l,r):
                # print(i,  words[i][depth], words[i+1][depth])
                if depth < len(words[i]) and depth < len(words[i+1]) and words[i][depth] != words[i+1][depth]:
                    d[words[i][depth]].add(words[i+1][depth])
                    prevs[words[i+1][depth]].add(words[i][depth])
                    # print(i,  words[i][depth], words[i+1][depth])
                    dfs(depth+1, l, i)
                    l = i+1
                elif depth < len(words[i]) and depth < len(words[i+1]) and i == r-1: dfs(depth+1, l, r)
                if len(words[i])-1 > depth and len(words[i+1])-1 == depth: self.is_shit = True

        dfs(0, 0, len(words)-1)

        if self.is_shit: return ""

        q = deque(filter(lambda el:el not in prevs, s))
        res = []
        while q:
            cur = q.popleft()
            res.append(cur)

            for child in d[cur]:
                try:
                    prevs[child].remove(cur)
                except:
                    pass

                if len(prevs[child]) == 0:
                    q.append(child)

        # print(d)

        return "".join(res) if len(res) == len(s) else ""

# h < e
# e < r
# n < f
# r < n
# 
# hernf