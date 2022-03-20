import unittest
from robot import *


class Testing_robot(unittest.TestCase):
    def test_robot_init(self):
        my_robot = robot('5 5', '1 2 N', 'RFL')
        self.assertEqual(my_robot.space, [5, 5])
        self.assertEqual(my_robot.X, 1)
        self.assertEqual(my_robot.Y, 2)
        self.assertEqual(my_robot.orient, 90)
        self.assertEqual(my_robot.command, ['R', 'F', 'L'])

    # Wrong initial pos testing
    def test_robot_init_out_of_bounds(self):
        with self.assertRaises(Exception):
            robot('5 5', '6 2 N', 'RFL')

    # Wrong initial pos testing
    def test_robot_init_out_of_bounds_negative(self):
        with self.assertRaises(Exception):
            robot('5 5', '2 -1 N', 'RFL')

    def test_robot_movement(self):
        my_robot = robot('5 5', '1 2 N', 'RFRFFRFRF')
        my_robot.move()
        x, y, orientation = my_robot.result()
        self.assertEqual(x, 1)
        self.assertEqual(y, 3)
        self.assertEqual(orientation, 'N')

    # Moves into the wall
    def test_robot_movement_out_of_bounds(self):
        with self.assertRaises(Exception):
            my_robot = robot('5 5', '1 2 N', 'RFRFFFFRFRF')
            my_robot.move()


if __name__ == '__main__':
    unittest.main()
