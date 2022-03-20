from robot import *


def main():
    while True:
        # inputs
        space = input('Please enter room space: ')
        position = input('Please enter position and orientation: ')
        command = input('Please enter list of instructions: ')

        # robot movement
        my_robot = robot(space, position, command)
        my_robot.move()
        x, y, orientation = my_robot.result()
        print(f'X: {x}, Y: {y}, Facing: {orientation}\n')
        ans = input('Do you want to continue? [Y/N]: ')
        if ans == 'N' or ans == 'n':
            break


if __name__ == '__main__':
    main()
