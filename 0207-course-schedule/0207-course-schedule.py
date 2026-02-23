class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_dict = [[] for i in range(numCourses)]
        for (course, pre) in prerequisites:
            pre_dict[course].append(pre)
        
        visit = set()

        def dfs(course):
            if not pre_dict[course]:
                return True
            if course in visit:
                return False
            visit.add(course)
            for c in pre_dict[course]:
                if not dfs(c):
                    return False
            pre_dict[course] = []
            visit.remove(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True