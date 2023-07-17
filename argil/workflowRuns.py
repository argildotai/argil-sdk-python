import requests, json
from typing import List
from .types import WorkflowRun
from pkg_resources import resource_string

class WorkflowRuns:
    def __init__(self, apiKey: str) -> None:
        self.headers: Dict[str, str] = {'authorization': f'Bearer {apiKey}'}
        config = json.loads(resource_string(__name__, 'config.json').decode('utf-8'))
        self.apiUrl: str = config['apiUrl']

    def list(self) -> List[WorkflowRun]:
        response = requests.get(f'{self.apiUrl}/getWorkflowRuns', headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get(self, id: str) -> WorkflowRun:
        response = requests.get(f'{self.apiUrl}/getWorkflowRun/{id}', headers=self.headers)
        response.raise_for_status()
        return response.json()
