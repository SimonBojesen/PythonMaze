import unittest
import backend_functionality

class TestMazeSolver(unittest.TestCase):
    def setUp(self):
        self.sizeX = 5
        self.sizeY = 15
        self.maze = backend_functionality.maze_generate(self.sizeX, self.sizeY)

    def test_solver_found_goal(self): #Test if solver finds goal and returns true
        backend_functionality.set_grid(self.maze)
        true_or_false = backend_functionality.search(1, 1)
        self.assertTrue(true_or_false, 'Test failed')

if __name__ == '__main__':
    unittest.main()