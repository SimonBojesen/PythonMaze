import unittest
import backend_functionality

class TestMazeSolver(unittest.TestCase):
    def setUp(self):
        self.sizeX = 5
        self.sizeY = 5
        self.maze = backend_functionality.maze_generate(self.sizeX, self.sizeY)
        self.solve = backend_functionality.search(self.sizeX,self.sizeY)

    def test_solver_found_goal(self): #Test if solver finds goal and prints ("found at %d,%d" % (x, y))
        self.assertEqual(int(self.maze[len(self.maze)-2][len(self.maze[0])-2]), 2, "Test failed")
        self.assertEqual(int(self.solve[len(self.solve)-2][len(self.solve[0])-2]), 2, "Test failed")
        #self.assertTrue(True,("found at %d,%d" % (self.sizeX, self.sizeY)))
        #("found at %d,%d" % (x, y))
if __name__ == '__main__':
    unittest.main()