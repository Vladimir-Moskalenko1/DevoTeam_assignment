from my_parser import *
import math


class robot:
    def __init__(self, space='', position='', command=''):
        space = my_parser.parse_space(space)
        position = my_parser.parse_pos(position)
        command = my_parser.parse_command(command)
        self.X = position[0]
        self.Y = position[1]
        self.orient = position[2]
        self.space = space

        # check for out of bounds
        if self.X > self.space[0] or self.Y > self.space[1]:
            raise Exception('Out of bounds.')
        self.command = command

    def move(self):
        for instruction in self.command:

            if instruction == 'L':
                self.orient += 90
                if self.orient > 360:
                    self.orient -= 360

            elif instruction == 'R':
                self.orient -= 90
                if self.orient < 0:
                    self.orient += 360

            elif instruction == 'F':
                self.X += round(math.cos(math.radians(self.orient)))
                self.Y -= round(math.sin(math.radians(self.orient)))

                # check current position
                if self.X > self.space[0] or self.Y > self.space[1]:
                    raise Exception(f'Out of bounds. X: {self.X}, Y: {self.Y}')
                if self.X < 0 or self.Y < 0:
                    raise Exception(f'Out of bounds. X: {self.X}, Y: {self.Y}')

    def result(self):
        if self.orient == 90:
            self.orient = 'N'
        elif self.orient == 0:
            self.orient = 'E'
        elif self.orient == 180:
            self.orient = 'S'
        else:
            self.orient = 'W'

        return self.X, self.Y, self.orient
