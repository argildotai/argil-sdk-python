# Argil SDK for Python

This is the Python SDK for the Argil API. It provides a convenient way to interact with the Argil's API from Python applications.

## Installation

You can install the SDK with pip:

```bash
pip install argil
```

## Usage

Here's an example of how to use the SDK:

```
from argil import ArgilSdk

argilSdk = ArgilSdk('ARGIL_API_KEY')

# Run a workflow
response = argilSdk.workflows.run(WORKFLOW_ID, { 'input': {INPUT_OBJECT} })
print(response)

# List workflow runs
response = argilSdk.workflowRuns.list()
print(response)

# Get a specific workflow run
response = argilSdk.workflowRuns.get(WORKFLOWRUN_ID)
print(response)
```
