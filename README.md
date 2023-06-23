# Argil SDK for Python

This is the Python SDK for the Argil API. It provides a convenient way to interact with the API from Python applications.

## Installation

You can install the SDK with pip:

```bash
pip install argil-sdk
```

## Usage

Here's an example of how to use the SDK:

```
from argil_sdk import ArgilSdk

argil_sdk = ArgilSdk('ARGIL_API_KEY')

# Run a workflow
response = argil_sdk.workflows.run(WORKFLOW_ID, { 'input': {INPUT_OBJECT} })
print(response)

# List workflow runs
response = argil_sdk.workflowRuns.list()
print(response)

# Get a specific workflow run
response = argil_sdk.workflowRuns.get(WORKFLOWRUN_ID)
print(response)
```
