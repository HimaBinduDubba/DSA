class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for i in paragraph:
            if i in '?.,!;\'':
                paragraph = paragraph.replace(i, " ")
        s = paragraph.lower().split()
        set_s = set(s)
        max_count = 0
        count = 0
        most_common = ""
        for i in set_s:
            if i not in banned:
                count = s.count(i)
                if count > max_count:
                    max_count = count
                    most_common = i
        return most_common