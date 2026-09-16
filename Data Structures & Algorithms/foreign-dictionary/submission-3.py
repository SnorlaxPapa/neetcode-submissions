from collections import deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        indegree = {}

        for word in words:
            for char in word:
                if char not in adj:
                    adj[char] = set()
                    indegree[char] = 0

        for i in range(len(words) - 1):
            curr = words[i]
            nxt = words[i + 1]

            for j in range(len(curr)):
                if j == len(nxt):
                    return ""

                if curr[j] != nxt[j]:
                    if nxt[j] not in adj[curr[j]]:
                        adj[curr[j]].add(nxt[j])
                        indegree[nxt[j]] += 1
                    break

        queue = deque()

        for char, degree in indegree.items():
            if degree == 0:
                queue.append(char)

        res = ""

        while queue:
            curr = queue.popleft()
            res += curr

            for neighbor in adj[curr]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return res if len(res) == len(indegree) else ""