# Argil Python SDK

Welcome to the Argil Python SDK. This library provides a simple and intuitive interface to interact with Argil's API, allowing you to leverage the power of AI-driven workflows and automations in your Python applications.

For the full Argil documentation, please visit https://docs.argil.ai.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)

## Installation

This library is distributed on PyPI. In order to add it as a dependency, run the following command:

```bash
pip install argil
```

## Usage

Here is a quick example of how to use the Argil Python SDK:

```python
from argil import ArgilSdk

sdk = ArgilSdk(api_key='your-api-key')

# Run a workflow
run = sdk.workflows.run('workflow-id', {
    "input_field_name1": $input_value1,
    "input_field_name2": $input_value2
    // Input fields depends on the workflow you run, please look at our full documentation.
})

# Get a workflow run
workflow_run = sdk.workflowRuns.get(run['id'])

# List all workflow runs
workflow_run = sdk.workflowRuns.list()

print(workflow_run)
```

## API Reference

The Argil Python SDK provides the following classes:

- ArgilSdk: The main class that provides access to the different services.
- Workflows: A class for interacting with the Workflows service of the Argil API.
- WorkflowRuns: A class for interacting with the WorkflowRuns service of the Argil API.
- ArgilConfig: A class for managing the configuration for the SDK.
- ArgilError: A custom error class for providing more detailed and specific error messages.

For more detailed information, please refer to the source code and inline comments.

## Contributing

We welcome contributions from the community.

## License

This project is licensed under the GPL-3.0-or-later license. For more information, see the  [LICENSE.md](LICENSE.md) file.

## Support

If you encounter any problems or have any questions, please open an issue on our [GitHub repository](https://github.com/argildotai/argil-sdk-python/issues).

## Acknowledgements

This project uses the following open-source packages:

- [requests](https://github.com/psf/requests): A simple, yet elegant HTTP library.

## Contact

For any inquiries, please contact us at briva@argil.ai.

