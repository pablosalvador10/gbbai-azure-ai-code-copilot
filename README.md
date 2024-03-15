# Azure AI Code Copilot <img src="./utils/images/azure_logo.png" alt="Azure Logo" style="width:30px;height:30px;"/>

Welcome to the Azure AI Code Copilot Project! This repository is designed to facilitate the development of AI projects using Azure AI services and OpenAI's GPT-4 model.


## Project Overview

This project includes:

- **Azure AI Integration**: Utilize Azure AI services like OpenAI, Speech AI, and Language Service to build advanced AI applications.
- **Code Migration with Copilot**: Leverage the power of OpenAI's GPT-3 model to translate code from one programming language to another.
- **Chatbot Development**: Develop a chatbot using Azure AI services and OpenAI's GPT-3 model.

## Requirements

> Modify as needed by project 

### Setting Up Azure AI Services

- Azure OpenAI Service: You need to create an Azure OpenAI service instance and obtain the API key. [start here](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- Azure Speech AI Service: Required for speech-to-text conversion. Set up the service and get the subscription key and region. [start here](https://azure.microsoft.com/en-us/products/ai-services/ai-speech)
- Azure Language Service: Necessary for language understanding and intent recognition.[start here](https://azure.microsoft.com/en-us/products/ai-services/ai-language)

### Configuration Env variables

We will now use environment variables to store our configuration. This is a more secure practice as it prevents sensitive data from being accidentally committed and pushed to version control systems.

Create a `.env` file in your project root and add the following variables:

```env
# Your Azure Speech Service subscription key
SPEECH_KEY=<Your_Azure_Speech_Service_Subscription_Key>

# Your Azure Speech Service region
SPEECH_REGION=<Your_Azure_Speech_Service_Region>

# Your Azure Machine Learning workspace key
INTENT_KEY=<Your_Azure_Machine_Learning_Workspace_Key>

# Your Azure OpenAI API key
OPENAI_KEY=<Your_Azure_OpenAI_API_Key>

# The model used for chat
CHAT_MODEL=<Your_Chat_Model>

# The model used for completions
COMPLETION_MODEL=<Your_Completion_Model>

# The base URL for the OpenAI API
OPENAI_API_BASE=<Your_OpenAI_API_Base_URL>

# The version of the OpenAI API
OPENAI_API_VERSION=<Your_OpenAI_API_Version>

# Your Azure Storage connection string
AZURE_STORAGE_CONNECTION_STRING=<Your_Azure_Storage_Connection_String>
``` 

`SPEECH_KEY` and `SPEECH_REGION` are used for the Azure Speech Service.
`INTENT_KEY` is used for the Azure Machine Learning workspace.
`OPENAI_KEY`, `CHAT_MODEL`, `COMPLETION_MODEL`, `OPENAI_API_BASE`, and `OPENAI_API_VERSION` are used for the Azure OpenAI API.
`AZURE_STORAGE_CONNECTION_STRING` is used for Azure Storage.

> 📌 Note Remember not to commit the .env file to your version control system. Add it to your .gitignore file to prevent it from being tracked.

## 🌲 Project Tree Structure

```markdown
📂 gbbai-azure-ai-template
┣ 📂 notebooks <- For development, EDA, and quick testing (Jupyter notebooks for analysis and development).
┣ 📂 src <- Houses main source code for data processing, feature engineering, modeling, inference, and evaluation.
┣ 📂 test <- Runs unit and integration tests for code validation and QA.
┣ 📂 utils <- Contains utility functions and shared code used throughout the project.
┣ 📜 .env.sample <- Sample environment variables file. Replace with your own.
┣ 📜 .pre-commit-config.yaml <- Config for pre-commit hooks ensuring code quality and consistency.
┣ 📜 01-workshop.ipynb <- Jupyter notebook for the workshop.
┣ 📜 CHANGELOG.md <- Logs project changes, updates, and version history.
┣ 📜 USAGE.md <- Guidelines for using this template.
┣ 📜 environment.yaml <- Conda environment configuration.
┣ 📜 Makefile <- Simplifies common development tasks and commands.
┣ 📜 pyproject.toml <- Configuration file for build system requirements and packaging-related metadata.
┣ 📜 README.md <- Overview, setup instructions, and usage details of the project.
┣ 📜 requirements-codequality.txt <- Requirements for code quality tools and libraries.
┣ 📜 requirements.txt <- General project dependencies.
```