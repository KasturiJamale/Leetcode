class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """

        totalOutEle = r * c
        outputMat = [[0 for _ in range(c)] for _ in range(r)]

        # for matrix
        rows = len(mat)
        cols = len(mat[0])
        totalMatEle = rows * cols

        if totalMatEle != totalOutEle:
            return mat

        for i in range(r):
            for j in range(c):
                index = i * c + j
                outputMat[i][j] = mat[index // cols][index % cols]

        return outputMat