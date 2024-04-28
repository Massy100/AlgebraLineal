class SumaMatrices:
    def __init__(self, size):
        self.size = size

    def create_matrix_from_entries(self, entries):
        matrix = []
        for row_entries in entries:
            row = [float(entry.get()) for entry in row_entries]
            matrix.append(row)
        return matrix

    def sumar_matrices(self, m1, m2):
        return [[m1[i][j] + m2[i][j] for j in range(self.size)] for i in range(self.size)]

    def restar_matrices(self, m1, m2):
        return [[m1[i][j] - m2[i][j] for j in range(self.size)] for i in range(self.size)]
    
    
