"""
Test discovery of functional dependencies
"""

import unittest

from func_dep.discovery import result_matches


class DependenciesDiscoveryTestSuite(unittest.TestCase):
    """
    Class that suppose to have the same description as the module
    """

    def test_trivial_dependency(self):
        """
        x->x
        """

        self.assertTrue(result_matches(lambda x: x, 1, 1))


if __name__ == '__main__':
    unittest.main()
