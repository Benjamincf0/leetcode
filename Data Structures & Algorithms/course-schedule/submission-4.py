class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nexts = defaultdict(list)
        num_pres = [0]*numCourses

        for c, p in prerequisites:
            nexts[p].append(c)
            num_pres[c] += 1

        num_visited = 0
        q = deque()

        for course in range(numCourses):
            if num_pres[course] == 0:
                q.append(course)

        while q:
            cur_course = q.pop()
            num_visited += 1

            for child in nexts[cur_course]:
                num_pres[child] -= 1
                if num_pres[child] == 0:
                    q.append(child)

        return num_visited == numCourses