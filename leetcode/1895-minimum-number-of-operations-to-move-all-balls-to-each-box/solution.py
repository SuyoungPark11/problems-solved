class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        n = len(boxes)
        distances = [0] * n
        prefixCount, prefixSum = 0, 0
        for i in range(n):
            distances[i] = prefixCount * i - prefixSum
            if boxes[i] == '1':
                prefixCount += 1
                prefixSum += i

        suffixCount, suffixSum = 0, 0
        for i in range(n-1, -1, -1):
            distances[i] += suffixSum - suffixCount * i
            if boxes[i] == '1':
                suffixCount += 1
                suffixSum += i

        return distances
        
