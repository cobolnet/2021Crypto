class Box:
    # Create box array
    box = None

    # Generate initial box with all -1's
    def __init__(self):
        self.box = [[-1] * 4 for _ in range(4)]

    # fill box with initial key list
    @staticmethod
    def fill_box(key):
        t_list = [-1 for _ in range(16)]
        zero_to_f = [0 for _ in range(16)]
        dec_to_hex = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8,
                      9: 9, 10: 0xa, 11: 0xb, 12: 0xc, 13: 0xd, 14: 0xe, 15: 0xf}

        # Mod key and fill box with hex
        index = 0
        for i in range(0, 256, 16):
            i_ascii = ord(key[i])
            i_ascii %= 16

            if zero_to_f[i_ascii] == 1:
                index += 1
                continue

            t_list[index] = dec_to_hex[i_ascii]
            zero_to_f[i_ascii] = 1
            index += 1

        # To fill list wasn't get hex
        for i in range(16):
            if t_list[i] == -1:
                for j in range(16):
                    if zero_to_f[j] == 0:
                        zero_to_f[j] = 1
                        t_list[i] = j#dec_to_hex[j]
                        break

        # Convert 1D to 2D list
        # for i in range(4):
        #     for j in range(4):
        #         self.box[i][j] = t_list[(i * 4) + j]

        return t_list

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
