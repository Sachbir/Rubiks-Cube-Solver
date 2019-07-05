from Face import Face


class Cubelet:

    # 0 indicates a blank face; 1-6 indicate sides
    # U, F, R, B, L, D

    def __init__(self):

        self.sides = [Face.Blank
                      for i in range(6)]

    def turn_u_cw(self):

        temp = self.sides[3]

        self.sides[3] = self.sides[4]
        self.sides[4] = self.sides[1]
        self.sides[1] = self.sides[2]
        self.sides[2] = temp

    def turn_u_ccw(self):

        temp = self.sides[3]

        self.sides[3] = self.sides[2]
        self.sides[2] = self.sides[1]
        self.sides[1] = self.sides[4]
        self.sides[4] = temp

    def turn_f_cw(self):

        temp = self.sides[0]

        self.sides[0] = self.sides[4]
        self.sides[4] = self.sides[5]
        self.sides[5] = self.sides[2]
        self.sides[2] = temp

    def turn_f_ccw(self):

        temp = self.sides[0]

        self.sides[0] = self.sides[2]
        self.sides[2] = self.sides[5]
        self.sides[5] = self.sides[4]
        self.sides[4] = temp

    def turn_r_cw(self):
        temp = self.sides[0]

        self.sides[0] = self.sides[1]
        self.sides[1] = self.sides[5]
        self.sides[5] = self.sides[3]
        self.sides[3] = temp

    def turn_r_ccw(self):
        temp = self.sides[0]

        self.sides[0] = self.sides[3]
        self.sides[3] = self.sides[5]
        self.sides[5] = self.sides[1]
        self.sides[1] = temp
