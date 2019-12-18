import unittest
import GUI2


class TestExceptions(unittest.TestCase):

    def test_MazeSizeTooHigh(self):
        self.assertRaises(GUI2.MazeSizeTooHigh, GUI2.mazeSizeX)

    def test_MazeSizeTooLow(self):
        self.assertRaises(GUI2.MazeSizeTooLow, GUI2.mazeSizeY)


if __name__ == '__main__':
    unittest.main()
