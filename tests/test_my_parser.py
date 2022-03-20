import unittest
from my_parser import *


class Testing_parser(unittest.TestCase):
    def test_space_parsing(self):
        self.assertEqual(my_parser.parse_space('1 1'), [1, 1])

    # Test for wrong values
    def test_space_with_negative(self):
        with self.assertRaises(Exception):
            my_parser.parse_space('-1 1')

    # Test for wrong values
    def test_space_with_zero(self):
        with self.assertRaises(Exception):
            my_parser.parse_space('1 0')

    # Test for wrong dimensions
    def test_space_with_wrong_dimensions(self):
        with self.assertRaises(Exception):
            my_parser.parse_space('1 1 1')

    def test_position_parsing(self):
        self.assertEqual(my_parser.parse_pos('1 1 N'), [1, 1, 90])

    # Wrong position testing
    def test_position_with_negative(self):
        with self.assertRaises(Exception):
            my_parser.parse_pos('-1 1 N')

    # Wrong position testing
    def test_position_with_wrong_orientation(self):
        with self.assertRaises(Exception):
            my_parser.parse_pos('1 1 A')

    # Wrong position testing
    def test_position_with_wrong_dimensions(self):
        with self.assertRaises(Exception):
            my_parser.parse_pos('1 1 1 N')

    def test_command_parsing(self):
        self.assertEqual(my_parser.parse_command('LFRF'), ['L', 'F', 'R', 'F'])

    # Wrong command testing
    def test_command_with_lower_case(self):
        with self.assertRaises(Exception):
            my_parser.parse_command('lFRF')

    # Wrong command testing
    def test_command_with_wrong_instructions(self):
        with self.assertRaises(Exception):
            my_parser.parse_command('LFAF')


if __name__ == '__main__':
    unittest.main()
