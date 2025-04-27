# 3CLOUD-AUTOGEN Repository

Welcome to the 3CLOUD-AUTOGEN repository. This project provides a collection of examples, exercises, and tools demonstrating multi-agent systems using AutoGen, Semantic Kernel, Azure OpenAI services, and more.

## Repository Structure

- **0_BASIC AGENTS no GUI/**  
  Contains examples and exercises for multi-agent interactions without a graphical user interface. This folder includes instructions for running agents, generating and executing code remotely (for example, on Azure Container Apps), and more. See [README.md](0_BASIC AGENTS no GUI/README.md) for details.

- **1_BASIC AGENTS with GUI/**  
  Implements multi-agent systems with graphical interfaces using Streamlit. Refer to [README.md](1_BASIC AGENTS with GUI/README.md) for setup and usage instructions.

- **2_AUTOGEN-MAGENTIC1-NOTEBOOKS/**  
  Includes Jupyter Notebooks demonstrating AutoGen integration, Azure OpenAI Chat Completion, and advanced agent functionality. These notebooks offer step-by-step examples for generating, executing, and debugging code in a multi-agent setup.

- **.chainlit/**, **.coding/**, **.files/**  
  Configuration and auxiliary files for Chainlit and other development tools.

- **coding/** and **generated/**  
  Folders that contain additional code generation tools and output files.

## Prerequisites

- [Visual Studio Code](https://code.visualstudio.com/) with relevant extensions (e.g., Python, Dev Containers).
- Python 3.8 or later.
- Required dependencies as defined in the respective `requirements.txt` or `pyproject.toml` files.

## Getting Started

1. **Clone the Repository**

    ```bash
    git clone https://github.com/your_org/3CLOUD-AUTOGEN.git
    cd 3CLOUD-AUTOGEN
    ```

2. **Open in Visual Studio Code**

    Use the `Open Folder…` command in VS Code to open the repository.

3. **Set Up the Development Environment**

    - Create a virtual environment and install dependencies, or
    - Open the repository in a dev container if you prefer a containerized development setup.

4. **Deploy Azure Infrastructure (Optional)**

    For exercises that require Azure, deploy the prerequisites using the Azure Developer CLI (`azd`). See the [Infrastructure Setup](0_BASIC AGENTS no GUI/infra/README.md) for detailed instructions.

    To install the Azure Developer CLI and deploy, run:

    ```bash
    # For Linux/macOS:
    curl -fsSL https://aka.ms/install-azd.sh | bash

    # For Windows (Powershell):
    powershell -ex AllSigned -c "Invoke-RestMethod 'https://aka.ms/install-azd.ps1' | Invoke-Expression"
    ```

## Usage

Choose the appropriate subdirectory based on your needs:

- **No GUI Examples:** Explore and follow the instructions in [0_BASIC AGENTS no GUI/README.md](0_BASIC AGENTS no GUI/README.md).
- **GUI Examples:** Check out [1_BASIC AGENTS with GUI/README.md](1_BASIC AGENTS with GUI/README.md) for a Streamlit-based chat interface.
- **Notebooks:** Open the Jupyter notebooks in the [2_AUTOGEN-MAGENTIC1-NOTEBOOKS](2_AUTOGEN-MAGENTIC1-NOTEBOOKS/) folder to interactively run and modify multi-agent scenarios.

## Contributing

Contributions are welcome! Please see our [CONTRIBUTING.md](0_BASIC AGENTS no GUI/CONTRIBUTING.md) for guidance on submitting issues and pull requests.

## License

This repository is licensed under the MIT License. See [LICENSE.md](0_BASIC AGENTS no GUI/LICENSE.md) for further details.

## Additional Resources

- [Azure OpenAI and AutoGen Documentation](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/models.html)
- [Chainlit Documentation](https://docs.chainlit.io)

Happy coding!