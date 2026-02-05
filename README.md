

# 💬 chatter_box_ai

<div align="center">

[![GitHub stars](https://img.shields.io/github/stars/vishal-247/chatter_box_ai?style=for-the-badge)](https://github.com/vishal-247/chatter_box_ai/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/vishal-247/chatter_box_ai?style=for-the-badge)](https://github.com/vishal-247/chatter_box_ai/network)
[![GitHub issues](https://img.shields.io/github/issues/vishal-247/chatter_box_ai?style=for-the-badge)](https://github.com/vishal-247/chatter_box_ai/issues)
[![GitHub license](https://img.shields.io/github/license/vishal-247/chatter_box_ai?style=for-the-badge)](LICENSE) <!-- TODO: Add a LICENSE file if this project is intended for public use. -->

**A collection of Python scripts demonstrating various AI chatbot functionalities, including conversational history, tool usage, and document processing.**

</div>

## 📖 Overview

`chatter_box_ai` is an experimental repository designed to showcase different approaches to building intelligent chatbots using Python. It explores key features such as maintaining conversational context, integrating external tools to extend bot capabilities, and processing documents to enhance the bot's knowledge base. Each script serves as a standalone example, making it a valuable resource for understanding the fundamental building blocks of AI-driven conversational agents.

## ✨ Features

Based on the individual scripts, this project offers demonstrations of:

-   🗣️ **Basic AI Chatbot Interaction:** Engage in simple, single-turn conversations.
-   🧠 **Chatbot with Conversational History:** Maintain context across multiple turns for more coherent dialogues.
-   🛠️ **Tool-Augmented Chatbot:** Empower the chatbot to use external tools (e.g., search, calculators) for enhanced responses.
-   📄 **Document Processing for RAG:** Process documents (likely PDFs) to create a knowledge base for chatbots, enabling Retrieval-Augmented Generation (RAG).
-   ⚙️ **Structured Output Generation:** Potentially guides AI models to produce responses in a specific, structured format.
-   🧪 **API Interaction/Testing:** Includes a script for testing external API integrations, likely for LLM providers.

## 🛠️ Tech Stack

**Core:**
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

**AI/LLM Libraries (Inferred):**
![LangChain](https://img.shields.io/badge/LangChain-0.1.0-green?style=for-the-badge&logo=python&logoColor=white) <!-- Inferred, version placeholder -->
![OpenAI](https://img.shields.io/badge/OpenAI-API-412991?style=for-the-badge&logo=openai&logoColor=white) <!-- Inferred -->
![python-dotenv](https://img.shields.io/badge/python--dotenv-v1.0.0-blue?style=for-the-badge) <!-- Inferred, version placeholder -->
![PyPDF2](https://img.shields.io/badge/PyPDF2-v3.0.0-red?style=for-the-badge) <!-- Inferred for document processing, version placeholder -->
![FAISS](https://img.shields.io/badge/FAISS-CPU-lightgrey?style=for-the-badge) <!-- Inferred for local vector store, if RAG is implemented -->

## 🚀 Quick Start

To get these scripts running on your local machine, follow these steps.

### Prerequisites
-   **Python 3.8+**

### Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/vishal-247/chatter_box_ai.git
    cd chatter_box_ai
    ```

2.  **Install dependencies**
    Since there isn't a `requirements.txt` file, you'll need to install the inferred dependencies manually. It's highly recommended to use a virtual environment.

    ```bash
    # Create a virtual environment
    python -m venv venv
    # Activate the virtual environment
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate

    # Install the inferred dependencies
    pip install openai langchain python-dotenv pypdf2 faiss-cpu
    ```
    *Note: The exact versions of these packages may vary or additional packages might be needed based on the specific implementations within the scripts. Adjust as necessary.*

3.  **Environment setup**
    Most AI projects require API keys for external services (e.g., OpenAI). Create a `.env` file in the root directory of the project based on the example below:

    ```bash
    cp .env.example .env # You'll need to create this file manually
    ```
    Then, open `.env` and add your API key:
    ```ini
    OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
    ```
    Replace `"YOUR_OPENAI_API_KEY"` with your actual OpenAI API key.

### Running a Script

To run any of the chatbot demonstration scripts, activate your virtual environment (if not already active) and execute the Python file:

```bash
# Example: Run the chatbot with history
python chatbot_with_history.py

# Example: Run the document processing script (make sure to place PDFs in the 'pdf/' directory first)
python documentprocessing.py
```
Each script will have its own interactive or output behavior. Follow any on-screen prompts.

## 📁 Project Structure

```
chatter_box_ai/
├── .gitignore          # Standard Git ignore file for Python projects
├── apitest.py          # Script for testing API interactions
├── bot_with_tools.py   # Chatbot implementation with external tool integration
├── chatbot_with_history.py # Chatbot maintaining conversation history/context
├── chatterbox.py       # Core basic chatbot implementation
├── documentprocessing.py # Script for processing documents (e.g., PDFs) for a knowledge base
├── pdf/                # Directory for storing PDF documents for processing
├── structured.py       # Script potentially demonstrating structured output from an LLM
└── tempCodeRunnerFile.py # Temporary file, typically generated by IDEs (can be ignored)
```

## ⚙️ Configuration

### Environment Variables
The following environment variable is expected to be configured in your `.env` file:

| Variable       | Description                       | Default | Required |
|----------------|-----------------------------------|---------|----------|
| `OPENAI_API_KEY` | Your API key for OpenAI services. | N/A     | Yes      |

### Document Storage
The `pdf/` directory is intended for placing PDF documents that the `documentprocessing.py` script will use to extract information and potentially build a knowledge base.

## 🤝 Contributing

We welcome contributions to expand this collection of AI chatbot demonstrations!

### Development Setup for Contributors
1.  Fork the repository.
2.  Clone your forked repository:
    ```bash
    git clone https://github.com/YOUR_USERNAME/chatter_box_ai.git
    cd chatter_box_ai
    ```
3.  Set up your virtual environment and install dependencies as described in the [Installation](#installation) section.
4.  Create a new branch for your feature or bug fix:
    ```bash
    git checkout -b feature/your-feature-name
    ```
5.  Develop your changes, adhering to good Python coding practices.
6.  Ensure your code runs as expected.
7.  Commit your changes and push to your fork.
8.  Open a Pull Request to the `master` branch of the original repository.

## 📄 License

This project is currently without an explicit license. Please consider adding a `LICENSE` file if this project is intended for public use.

---

<div align="center">

**⭐ Star this repo if you find it helpful for learning AI chatbots!**

Made with ❤️ by [vishal-247](https://github.com/vishal-247)

</div>
