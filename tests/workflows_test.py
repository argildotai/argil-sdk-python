import unittest
from argil_sdk.workflows import Workflows

class TestWorkflows(unittest.TestCase):
    def test_init(self):
        workflows = Workflows(ARGIL_API_KEY)
        self.assertIsNotNone(workflows)

if __name__ == '__main__':
    unittest.main()
