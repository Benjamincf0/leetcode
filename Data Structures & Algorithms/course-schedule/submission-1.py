class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nexts = defaultdict(list)
        numPres = [0] * numCourses
        visited = set()
        q = deque()

        for n, pre in prerequisites:
            numPres[n] += 1
            nexts[pre].append(n)

        for i in range(numCourses):
            if numPres[i] == 0:
                q.append(i)
                visited.add(i)

        while q:
            i = q.popleft()
            for next_course in nexts[i]:
                if next_course not in visited:
                    numPres[next_course] -= 1
                    if numPres[next_course] == 0:
                        q.append(next_course)
                        visited.add(next_course)

        return len(visited) == numCourses