from pprint import pprint

class LongestCommonSequence: 
    def __init__(self, first: str, second: str,):
        self.first = first
        self.second = second

        self.rows = len(first)
        self.cols = len(second)

        self.matrix = [
            [0 for _ in range(self.rows+1)] for _ in range(self.cols+1)
        ]


    def lcs(self):
        for i in range(1, self.rows+1):
            for j in range(1, self.cols+1):
                if self.first[i-1] == self.second[j-1]:
                    self.matrix[i][j] = self.matrix[i-1][j-1] + 1
                else:
                    self.matrix[i][j] = max(self.matrix[i-1][j], self.matrix[i][j-1])

        pprint(self.matrix)

        return self.matrix[self.rows][self.cols]
    
    def lcs_with_memorization(self):
        self.rec_matrix = [
            [-1 for _ in range(self.rows+1)] for _ in range(self.cols+1)
        ]
        self.calc_matrix(self.rows, self.cols)
        pprint(self.rec_matrix)
        return self.rec_matrix[self.rows][self.cols]


    def calc_matrix(self, index: int, jindex: int):

        if self.rec_matrix[index][jindex] != -1:
            return self.rec_matrix[index][jindex]

        if index <= 0 or jindex <= 0:
            return 0

        if self.first[index-1] == self.second[jindex-1]:
            self.rec_matrix[index][jindex] = self.calc_matrix(index-1, jindex-1) + 1
        else:
            self.rec_matrix[index][jindex] = max(self.calc_matrix(index-1, jindex), self.calc_matrix(index, jindex-1))

        return self.rec_matrix[index][jindex]
    
    def count_uncalculated_items(self):
        uncalculated_items = 0
        for i in range(1, self.rows+1):
            for j in range(1, self.cols+1):
                if self.rec_matrix[i][j] == -1:
                    uncalculated_items += 1

        return uncalculated_items


    def lcs_paralel(first: str, second: str):
        pass


    def get_word(self):
        pass
    


lcs_instance = LongestCommonSequence("baasaasdfasdfesrs", "aabsaasdfasdfesrs")

result = lcs_instance.lcs()
print(result)

result = lcs_instance.lcs_with_memorization()
print(result)

ratio = lcs_instance.count_uncalculated_items()
print(ratio)
        
