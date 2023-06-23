from .workflows import Workflows
from .workflowRuns import WorkflowRuns

class ArgilSdk:
    def __init__(self, apiKey):
        self.workflows = Workflows(apiKey)
        self.workflowRuns = WorkflowRuns(apiKey)
