class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nexts = defaultdict(list)
        numPres = [0] * numCourses
        q = deque()
        num_visited = 0

        for n, pre in prerequisites:
            numPres[n] += 1
            nexts[pre].append(n)

        for i in range(numCourses):
            if numPres[i] == 0:
                q.append(i)
                num_visited += 1


        while q:
            i = q.popleft()
            for next_course in nexts[i]:
                numPres[next_course] -= 1
                if numPres[next_course] == 0:
                    q.append(next_course)
                    num_visited += 1

        print(numPres)
        return num_visited == numCourses