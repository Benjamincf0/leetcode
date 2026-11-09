class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        nexts = defaultdict(list)
        num_pres = [0]*numCourses

        for course, pre in prerequisites:
            nexts[pre].append(course)
            num_pres[course]+=1
            
        q = deque()

        for course in range(numCourses):
            if num_pres[course] == 0:
                q.append(course)

        print(q)

        res = []
        while q:
            cur = q.popleft()
            # print(cur)
            
            res.append(cur)

            for course in nexts[cur]:
                num_pres[course] -= 1
                if num_pres[course] == 0:
                    q.append(course)

        return res if len(res) == numCourses else []