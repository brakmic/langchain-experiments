# LangChain + Llamafile Experiments

This repository contains experiments and example code for using [LangChain](https://python.langchain.com/) with [Llamafile](https://github.com/Mozilla-Ocho/llamafile), running local LLMs in Python.

## Features

- **Python 3** project with [Pipenv](https://pipenv.pypa.io/en/latest/) for easy dependency management
- All required libraries for LangChain and Llamafile are specified in the included `Pipfile`
- Example code for interacting with a local LLM via LangChain in the `src` directory
- Ready-to-use [VSCode workspace](./langchain.code-workspace) for convenient development
- Easily switch between different local LLMs downloaded from [HuggingFace](https://huggingface.co/), e.g. [Mozilla/Llama-3.2-1B-Instruct-llamafile](https://huggingface.co/Mozilla/Llama-3.2-1B-Instruct-llamafile)

## Getting Started

### Prerequisites

- **Python 3.12** (or compatible version)
- [pipenv](https://pipenv.pypa.io/en/latest/) (recommended, but you can use any Python environment manager)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/brakmic/langchain-experiments.git
    cd langchain-experiments
    ```

2. **Install dependencies:**

    ```bash
    pipenv install
    ```

    Or, if you prefer another environment manager, use the `Pipfile` as a reference.

3. **Download a Llamafile model:**
    - Visit [HuggingFace](https://huggingface.co/Mozilla/Llama-3.2-1B-Instruct-llamafile) or another LLM provider.
    - Download the `.llamafile` model and run it locally (see the model's README for instructions).

4. **Set the Llamafile API URL (optional):**
    - By default, the code expects the Llamafile server at `http://localhost:8080`.
    - You can override this by setting the `LLAMAFILE_URL` environment variable.

### Usage

- Source code is in the `src` directory. For example, to run a simple prompt:

    ```bash
    python src/llamafile.py
    ```

- You can open the project in VSCode using the included workspace file:

    ```bash
    code langchain.code-workspace
    ```

## Notes

- The `.venv` and `local/` directories are excluded via `.gitignore`.
- You can use any Python 3 environment manager if you prefer not to use Pipenv.
- Example models and prompts are provided, but you can adapt them for your own experiments.

## License

[MIT](./LICENSE)
