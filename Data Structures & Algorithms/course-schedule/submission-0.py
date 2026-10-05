class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nexts = defaultdict(list)
        pres = defaultdict(list)
        visited = set()
        q = deque()

        for n, pre in prerequisites:
            pres[n].append(pre)
            nexts[pre].append(n)

        for i in range(numCourses):
            if i not in pres:
                q.append(i)
                visited.add(i)

        while q:
            i = q.popleft()
            
            for next_course in nexts[i]:
                if next_course not in visited:
                    if all(i in visited for i in pres[next_course]):
                        q.append(next_course)
                        visited.add(next_course)

        return len(visited) == numCourses