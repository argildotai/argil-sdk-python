import requests

class Workflows:
    def __init__(self, apiKey):
        self.headers = {'authorization': apiKey}

    def run(self, id, input):
        response = requests.post('https://argil.ai/runWorkflow', json={'id': id, 'input': input}, headers=self.headers)
        response.raise_for_status()
        return response.json()
