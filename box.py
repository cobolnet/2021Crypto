class Box:
    # Create box array
    box = None

    # Generate initial box with all -1's
    def __init__(self):
        self.box = [[-1]*4 for _ in range(4)]

    # fill box with initial key list
    def en_box(self, key):
        pass

    def de_box(self, key):
        pass

    def fill_empty(self):
        pass

    def right_col_shift(self):
        c_temp = [self.box[0][3], self.box[1][3], self.box[2][3], self.box[3][3]]

        for x in range(2, -1, -1):
            for y in range(4):
                self.box[y][x + 1] = self.box[y][x]

        for i in range(4):
            self.box[i][0] = c_temp[i]

    def down_row_shift(self):
        r_temp = [self.box[3][0], self.box[3][1], self.box[3][2], self.box[3][3]]

        for y in range(2, -1, -1):
            for x in range(4):
                self.box[y + 1][x] = self.box[y][x]

        for i in range(4):
            self.box[0][i] = r_temp[i]

    def left_col_shift(self):
        c_temp = [self.box[0][0], self.box[1][0], self.box[2][0], self.box[3][0]]

        for x in range(1, 4):
            for y in range(4):
                self.box[y][x - 1] = self.box[y][x]

        for i in range(4):
            self.box[i][3] = c_temp[i]

    def up_row_shift(self):
        r_temp = [self.box[0][0], self.box[0][1], self.box[0][2], self.box[0][3]]

        for y in range(1, 4):
            for x in range(4):
                self.box[y - 1][x] = self.box[y][x]

        for i in range(4):
            self.box[3][i] = r_temp[i]

    def test_fill(self):
        for i in range(4):
            for j in range(4):
                self.box[i][j] = (i * 4) + j
