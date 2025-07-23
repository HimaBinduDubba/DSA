class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         res = [sorted(word) for word in strs]
         visited = [False] * len(strs)
         final = []

         for i in range(len(strs)):
            if not visited[i]:
                group = [strs[i]]
                visited[i] = True
                for j in range(i + 1, len(strs)):
                    if res[i] == res[j] and not visited[j]:
                        group.append(strs[j])
                        visited[j] = True
                final.append(group)

         return final


