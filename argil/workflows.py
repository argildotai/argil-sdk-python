import requests, json
from typing import Dict, Any
from .types import WorkflowRun
from pkg_resources import resource_string

class Workflows:
    def __init__(self, apiKey: str) -> None:
        self.headers: Dict[str, str] = {'authorization': f'Bearer {apiKey}'}
        config = json.loads(resource_string(__name__, 'config.json').decode('utf-8'))
        self.apiUrl: str = config['apiUrl']

    # Run a workflow providing its id and input
    def run(self, id: str, input: Dict[str, Any]) -> WorkflowRun:
        response = requests.post(f'{self.apiUrl}/runWorkflow', json={'id': id, 'input': input}, headers=self.headers)
        response.raise_for_status()
        return response.json()
