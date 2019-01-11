import unittest

import numpy as np
import scipy

from your_project_name import your_module


class YourModuleTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_root_endpoint(self):
        self.assertEqual(your_module.numpy_version(), np.__version__)
        self.assertEqual(your_module.scipy_version(), scipy.__version__)


if __name__ == '__main__':
    unittest.main()
