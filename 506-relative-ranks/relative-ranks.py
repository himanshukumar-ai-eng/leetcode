class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        sorted_score = sorted(score, reverse=True)

        rank = {}

        for i in range(len(sorted_score)):
            rank[sorted_score[i]] = i + 1

        result = []

        for x in score:
            r = rank[x]

            if r == 1:
                result.append("Gold Medal")
            elif r == 2:
                result.append("Silver Medal")
            elif r == 3:
                result.append("Bronze Medal")
            else:
                result.append(str(r))

        return result