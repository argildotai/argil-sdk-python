from typing import Dict, List, Optional, Union
from .argil_config import ArgilConfig
from .argil_error import ArgilError
import requests

class Base:
    """
    Base class for interacting with the Argil API.
    This class provides the basic functionality for making HTTP requests to the API.
    """
    def __init__(self, config: ArgilConfig):
        self.config = config

    def request(self, method: str, url: str, data: Optional[Dict] = None) -> Union[Dict, List]:
        """
        A generic method to make HTTP requests.
        @param {str} method - The HTTP method.
        @param {str} url - The URL.
        @param {dict} [data] - The data for post, put and patch requests.
        @returns {dict} The response data.
        """
        try:
            response = self.config.session.request(method, self.config.api_url + url, json=data, timeout=self.config.timeout)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as error:
            if response:
                raise ArgilError(f"Request to {url} failed with status {response.status_code}: {response.text}", response.status_code, response.text)
            else:
                raise ArgilError(f"Request to {url} failed: {str(error)}")

class Workflows(Base):
    """
    Class for interacting with the Workflows service of the Argil API.
    """
    def run(self, id: str, input: Dict) -> Dict:
        """
        Run a workflow with the provided ID and input.
        @param {str} id - The ID of the workflow to run.
        @param {dict} input - The input for the workflow.
        @returns {dict} The workflow run.
        """
        return self.request('post', '/runWorkflow', { 'id': id, 'input': input })

class WorkflowRuns(Base):
    """
    Class for interacting with the WorkflowRuns service of the Argil API.
    """
    def list(self) -> List:
        """
        List all workflow runs.
        @returns {list} An array of workflow runs.
        """
        return self.request('get', '/getWorkflowRuns')

    def get(self, id: str) -> Dict:
        """
        Get a workflow run with the provided ID.
        @param {str} id - The ID of the workflow run to get.
        @returns {dict} The workflow run.
        """
        return self.request('get', f'/getWorkflowRun/{id}')
