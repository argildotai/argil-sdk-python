import unittest
from argil_sdk.workflowRuns import WorkflowRuns

class TestWorkflowRuns(unittest.TestCase):
    def test_init(self):
        workflowRuns = WorkflowRuns('ARGIL_API_KEY')
        self.assertIsNotNone(workflowRuns)

if __name__ == '__main__':
    unittest.main()
