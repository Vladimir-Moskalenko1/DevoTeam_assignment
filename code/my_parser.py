class my_parser:
    @staticmethod
    def parse_space(space):
        space = space.split(' ')

        # check length of message
        if len(space) != 2:
            raise Exception('Incorrect size. Space should only contain "X" and "Y"!')
        output = [int(i) for i in space]

        # check for negative or 0
        if output[0] <= 0 or output[1] <= 0:
            raise Exception('Negative value or zero in space!')
        return output

    @staticmethod
    def parse_pos(position):
        position = position.split(' ')

        # check length of message
        if len(position) != 3:
            raise Exception('Incorrect position size. Position should only contain "X" "Y" and Orientation!')

        output = [int(i) for i in position[0:2]]

        # check for negatives
        if output[0] < 0 or output[1] < 0:
            raise Exception('Negative value in position!')

        # transform orientation into degrees
        if position[2] == 'N':
            output.append(90)
        elif position[2] == 'E':
            output.append(0)
        elif position[2] == 'S':
            output.append(270)
        elif position[2] == 'W':
            output.append(180)
        else:
            raise Exception('Orientation should only be "N E S W"!')

        return output

    @staticmethod
    def parse_command(command):
        command = list(command)

        # check for incorrect instructions
        for letter in command:
            if not (letter == 'L' or letter == 'R' or letter == 'F'):
                raise Exception('Command can contain only "R" "L" or "F"!')
        return command
