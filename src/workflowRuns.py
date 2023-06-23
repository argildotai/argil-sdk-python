import requests

class WorkflowRuns:
    def __init__(self, apiKey):
        self.headers = {'authorization': apiKey}

    def list(self):
        response = requests.get('https://argil.ai/getWorkflowRuns', headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get(self, id):
        response = requests.get(f'https://argil.ai/getWorkflowRun/{id}', headers=self.headers)
        response.raise_for_status()
        return response.json()
