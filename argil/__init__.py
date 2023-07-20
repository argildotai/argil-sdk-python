from typing import Optional
from .argil_config import ArgilConfig
from .api_definitions import Workflows, WorkflowRuns

class ArgilSdk:
    """
    Main SDK class that provides access to different services.
    This class is the entry point for using the Argil SDK.
    It includes instances of the Workflows and WorkflowRuns classes, which provide methods for interacting with the Argil API.
    It also includes an instance of the Configuration class, which manages the configuration for the SDK.
    """
    def __init__(self, api_key: Optional[str] = None, api_url: str = 'https://api.argil.ai', timeout: int = 2000):
        self.config = ArgilConfig(api_key, api_url, timeout)
        self.workflows = Workflows(self.config)
        self.workflowRuns = WorkflowRuns(self.config)

