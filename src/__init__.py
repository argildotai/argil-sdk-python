from .workflows import Workflows
from .workflowRuns import WorkflowRuns

class ArgilSdk:
    def __init__(self, apiKey: str) -> None:
        self.workflows: Workflows = Workflows(apiKey)
        self.workflowRuns: WorkflowRuns = WorkflowRuns(apiKey)
