import requests
from typing import Dict, Any
from .types import WorkflowRun

class Workflows:
    def __init__(self, apiKey: str) -> None:
        self.headers: Dict[str, str] = {'authorization': apiKey}
        with open('../config.json') as config_file:
            config = json.load(config_file)
        self.apiUrl: str = config['apiUrl']

    def run(self, id: str, input: Dict[str, Any]) -> WorkflowRun:
        response = requests.post(f'{self.apiUrl}/runWorkflow', json={'id': id, 'input': input}, headers=self.headers)
        response.raise_for_status()
        return response.json()
