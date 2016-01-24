import unittest
import doctest

from .shelltest import converter

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(converter))
    return tests

if __name__ == '__main__':
    unittest.main()
