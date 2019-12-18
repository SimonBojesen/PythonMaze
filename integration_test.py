import unittest
import test_backend_functionality
import test_maze_generator
import test_Maze_Solver
import test_exceptions

if __name__ == '__main__':
    tests1 = unittest.TestLoader().loadTestsFromModule(test_backend_functionality)
    tests2 = unittest.TestLoader().loadTestsFromModule(test_maze_generator)
    tests3 = unittest.TestLoader().loadTestsFromModule(test_Maze_Solver)
    #tests4 = unittest.TestLoader().loadTestsFromModule(test_exceptions)

    unittest.TextTestRunner(verbosity=2).run(tests1)
    unittest.TextTestRunner(verbosity=2).run(tests2)
    unittest.TextTestRunner(verbosity=2).run(tests3)
    # unittest.TextTestRunner(verbosity=2).run(tests4)
