# https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n, m = len(matrix), len(matrix[0])
        self.total = sum([sum(row) for row in matrix])
        self.before_row, self.after_row = defaultdict(int), defaultdict(int)
        self.before_col, self.after_col = defaultdict(int), defaultdict(int)
        self.inter_nw, self.inter_sw = defaultdict(int), defaultdict(int)
        self.inter_ne, self.inter_se = defaultdict(int), defaultdict(int)

        for i in range(n):
            self.before_row[i] = self.before_row[i-1] + sum(matrix[i])
            self.after_row[n-i-1] = self.after_row[n-i] + sum(matrix[~i])

        for i in range(m):
            self.before_col[i] = self.before_col[i-1] + sum([row[i] for row in matrix])
            self.after_col[m-i-1] = self.after_col[m-i] + sum([row[~i] for row in matrix])

        for i in range(n):
            for j in range(m):
                _i, _j = n-i-1, m-j-1
                inter_nw_sum = self.inter_nw[(i-1,j)] + self.inter_nw[(i,j-1)]
                inter_se_sum = self.inter_se[(_i+1,_j)] + self.inter_se[(_i,_j+1)]
                inter_ne_sum = self.inter_ne[(i-1,_j)] + self.inter_ne[(i,_j+1)]
                inter_sw_sum = self.inter_sw[(_i+1,j)] + self.inter_sw[(_i,j-1)]

                self.inter_nw[(i,j)] = inter_nw_sum - self.inter_nw[(i-1,j-1)] + matrix[i][j]
                self.inter_se[(_i,_j)] = inter_se_sum - self.inter_se[(_i+1,_j+1)] + matrix[_i][_j]
                self.inter_ne[(i,_j)] = inter_ne_sum - self.inter_ne[(i-1,_j+1)] + matrix[i][_j]
                self.inter_sw[(_i,j)] = inter_sw_sum - self.inter_sw[(_i+1,j-1)] + matrix[_i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        extra_rows = self.before_row[row1-1] + self.after_row[row2+1]
        extra_cols = self.before_col[col1-1] + self.after_col[col2+1]
        west_inters = self.inter_nw[(row1-1,col1-1)] + self.inter_sw[row2+1,col1-1]
        east_inters = self.inter_ne[(row1-1,col2+1)] + self.inter_se[row2+1,col2+1]

        return self.total - extra_rows - extra_cols + west_inters + east_inters
