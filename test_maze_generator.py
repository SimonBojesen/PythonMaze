import unittest
import backend_functionality
import concurrent.futures

class TestMazeGen(unittest.TestCase):
    def setUp(self):
        self.sizeX = 5
        self.sizeY = 10
        self.maze = backend_functionality.maze_generate(self.sizeX, self.sizeY)

    def test_correct_goal_placement(self):
        self.assertEqual(int(self.maze[len(self.maze)-2][len(self.maze[0])-2]), 2, "Test failed")

    def test_correct_sizes(self):
        self.assertEqual(len(self.maze), 2*self.sizeY+1, "Test failed")
        self.assertEqual(len(self.maze[0]), 2*self.sizeX+1, "Test failed")

if __name__ == '__main__':
    unittest.main()