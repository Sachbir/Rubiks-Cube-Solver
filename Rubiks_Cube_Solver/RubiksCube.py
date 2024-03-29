from Cubelet import Cubelet
from Face import Face


class RubiksCube:

    def __init__(self):

        # arranged left to right, back to front, top to bottom
        # noinspection PyUnusedLocal
        self.cubelets = [Cubelet()
                         for i in range(27)]
        self.initialize_cube()

    def initialize_cube(self):

        for cubelet in self.get_up_cubelets():
            cubelet.sides[0] = Face.Yellow

        for cubelet in self.get_front_cubelets():
            cubelet.sides[1] = Face.Blue

        for cubelet in self.get_right_cubelets():
            cubelet.sides[2] = Face.Red

        for cubelet in self.get_back_cubelets():
            cubelet.sides[3] = Face.Green

        for cubelet in self.get_left_cubelets():
            cubelet.sides[4] = Face.Orange

        for cubelet in self.get_down_cubelets():
            cubelet.sides[5] = Face.White

    @staticmethod
    def line_break(counter):

        counter += 1
        if counter > 2:
            print()
            counter = 0
        return counter

    def print_cube(self):

        counter = 0

        print("\nUp")
        for cubelet in self.get_up_cubelets():
            print(cubelet.sides[0], end='\t')
            counter = RubiksCube.line_break(counter)


        print("\nFront")
        for cubelet in self.get_front_cubelets():
            print(cubelet.sides[1], end='\t')
            counter = RubiksCube.line_break(counter)

        print("\nRight")
        for cubelet in self.get_right_cubelets():
            print(cubelet.sides[2], end='\t')
            counter = RubiksCube.line_break(counter)

        print("\nBack")
        for cubelet in self.get_back_cubelets():
            print(cubelet.sides[3], end='\t')
            counter = RubiksCube.line_break(counter)

        print("\nLeft")
        for cubelet in self.get_left_cubelets():
            print(cubelet.sides[4], end='\t')
            counter = RubiksCube.line_break(counter)

        print("\nDown")
        for cubelet in self.get_down_cubelets():
            print(cubelet.sides[5], end='\t')
            counter = RubiksCube.line_break(counter)

    @staticmethod
    def rotate_face_cw(cubelets, turn, side_to_set):

        for cubelet in cubelets:
            turn(cubelet)

        temp = cubelets[0]
        cubelets[0] = cubelets[6]
        cubelets[6] = cubelets[8]
        cubelets[8] = cubelets[2]
        cubelets[2] = temp

        temp = cubelets[1]
        cubelets[1] = cubelets[3]
        cubelets[3] = cubelets[7]
        cubelets[7] = cubelets[5]
        cubelets[5] = temp

        side_to_set(cubelets)

    @staticmethod
    def rotate_face_ccw(face_cubelets, turn_cubelet, set_face_cubelets):

        for cubelet in face_cubelets:
            turn_cubelet(cubelet)

        temp = face_cubelets[0]
        face_cubelets[0] = face_cubelets[2]
        face_cubelets[2] = face_cubelets[8]
        face_cubelets[8] = face_cubelets[6]
        face_cubelets[6] = temp

        temp = face_cubelets[1]
        face_cubelets[1] = face_cubelets[5]
        face_cubelets[5] = face_cubelets[7]
        face_cubelets[7] = face_cubelets[3]
        face_cubelets[3] = temp

        set_face_cubelets(face_cubelets)

    # Plane/side getters and setters

    def get_up_cubelets(self):

        return [self.cubelets[i]
                for i in range(0, 9)]

    def set_up_cubelets(self, cubelets):

        for i in range(0, 9):
            self.cubelets[i] = cubelets[i]

    def get_front_cubelets(self):

        front_cubelets = []

        for i in range(6, 27, 9):
            for j in range(3):
                front_cubelets.append(self.cubelets[i + j])

        return front_cubelets

    def set_front_cubelets(self, cubelets):

        index = 0

        for i in range(6, 27, 9):
            for j in range(3):
                self.cubelets[i + j] = cubelets[index]
                index += 1

    def get_right_cubelets(self):

        right_cubelets = []

        for i in range(8, 27, 9):
            for j in range(3):
                right_cubelets.append(self.cubelets[i - 3 * j])

        return right_cubelets

    def set_right_cubelets(self, cubelets):

        index = 0

        for i in range(8, 27, 9):
            for j in range(3):
                self.cubelets[i - 3 * j] = cubelets[index]
                index += 1

    def get_back_cubelets(self):

        back_cubelets = []

        for i in range(2, 27, 9):
            for j in range(3):
                cub = self.cubelets[i - j]
                back_cubelets.append(cub)

        return back_cubelets

    def set_back_cubelets(self, cubelets):

        index = 0

        for i in range(2, 27, 9):
            for j in range(3):
                self.cubelets[i - j] = cubelets[index]
                index += 1

    def get_left_cubelets(self):

        left_cubelets = []

        for i in range(0, 27, 9):
            for j in range(3):
                left_cubelets.append(self.cubelets[i + 3 * j])

        return left_cubelets

    def set_left_cubelets(self, cubelets):

        for i in range(0, 27, 3):
            self.cubelets[i] = cubelets[int(i / 3)]

    def get_down_cubelets(self):

        down_cubelets = []

        for i in range(24, 17, -3):
            for j in range(3):
                down_cubelets.append(self.cubelets[i + j])

        return down_cubelets

    def set_down_cubelets(self, cubelets):

        index = 0

        for i in range(24, 17, -3):
            for j in range(3):
                self.cubelets[i + j] = cubelets[index]
                index += 1

    def get_up_middle(self):

        return [self.cubelets[i]
                for i in range(9, 18)]

    def set_up_middle(self, cubelets):

        for i in range(9, 18):
            self.cubelets[i] = cubelets[i - 9]
