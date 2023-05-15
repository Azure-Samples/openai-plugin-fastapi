# AI Plugin Quickstart (Python 🐍)

This is a quickstart for creating an AI plugin, from writing a simple API server to running it in ChatGPT.


[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=GitHub+Codespaces&message=Open&color=lightgrey&logo=github)](https://codespaces.new/azure-samples/openai-plugin-fastapi)
[![Open in Dev Container](https://img.shields.io/static/v1?style=for-the-badge&label=Dev+Container&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure-samples/openai-plugin-fastapi)

## Getting started

1. **📤 One-click setup**: [Open a new Codespace](https://codespaces.new/azure-samples/openai-plugin-fastapi), giving you a fully configured cloud developer environment.
2. **🪄 Make an API**: Add routes in `main.py`, done in a few minutes even without [FastAPI](https://fastapi.tiangolo.com/lo/tutorial/) experience, thanks to [GitHub Copilot](https://github.com/features/copilot/).
3. **▶️ Run, one-click again**: Use VS Code's built-in *Run* command and open the forwarded port *8000* in your browser.
4. **💬 Test in ChatGPT**: Copy the URL (make sure its public) and paste it in ChatGPT's [Develop your own plugin](https://platform.openai.com/docs/plugins/getting-started/debugging) flow.
5. **🔄 Iterate quickly:** Codespaces updates the server on each save, and VS Code's debugger lets you dig into the code execution.



## Run

### Run in Codespaces
1. Click here to open in GitHub Codespaces

    [![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=GitHub+Codespaces&message=Open&color=lightgrey&logo=github)](https://codespaces.new/azure-samples/openai-plugin-fastapi)

1. Open Codespaces Ports tab, right click 8000, and make it public.
1. Copy the Codesapces address for port 8000
1. Open Chat GPT and add the plugin with the Codespaces address
1. Run a query for 'hiking boots'

### Run in Dev Container

1. Click here to open in Dev Container

    [![Open in Dev Container](https://img.shields.io/static/v1?style=for-the-badge&label=Dev+Container&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure-samples/openai-plugin-fastapi)

1. Hit F5 to start the API
1. Open Chat GPT and add the plugin with `localhost:8000`
1. Run a query for 'hiking boots'


### Run Locally

1. Clone the repo to your local machine `git clone https://github.com/azure-samples/openai-plugin-fastapi`
1. Open repo in VS Code 
1. Create a new Python virtual environment and activate it
1. Hit F5 to start the API
1. Open Chat GPT and add the plugin with `localhost:8000`
1. Run a query for 'hiking boots'

## Deploy to Azure

> NOTE: If you are running locally, then you first need to [install the Azure Developer CLI](https://aka.ms/azd/install)

### Deploy with Azure Developer CLI

1. Open a terminal
1. Run `azd auth login`
1. Run `azd up`
1. Copy the endpoint printed to the terminal
1. Open Chat GPT and add the plugin with that endpoint
1. Run a query for 'hiking boots'

### Deploy with GitHub Actions

1. Fork this repo to your own account
1. Open your fork in Codespaces, Dev Container or Local
1. Open a terminal
1. Run `azd auth login`
1. Run `azd pipeline config`
1. Click on the printed actions link. Scroll to the bottom of the logs to find the endpoint.
1. Open Chat GPT and add the plugin with that endpoint
1. Run a query for 'hiking boots'


## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.