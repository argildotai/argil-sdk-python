import requests
from typing import List, TypedDict
from .types import WorkflowRun

class WorkflowRuns:
    def __init__(self, apiKey: str) -> None:
        self.headers: Dict[str, str] = {'authorization': f'Bearer {apiKey}'}
        with open('../config.json') as config_file:
            config = json.load(config_file)
        self.apiUrl: str = config['apiUrl']

        response = requests.post(f'{self.apiUrl}/runWorkflow', json={'id': id, 'input': input}, headers=self.headers)
    def list(self) -> List[WorkflowRun]:
        response = requests.get(f'{self.apiUrl}/getWorkflowRuns', headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get(self, id: str) -> WorkflowRun:
        response = requests.get(f'{self.apiUrl}/getWorkflowRun/{id}', headers=self.headers)
        response.raise_for_status()
        return response.json()
