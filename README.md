# 🏋️‍♀️🥗 Fitness Diet Advisor AI 🤖

Welcome to the Fitness Diet Advisor AI project! This chatbot, powered by the Google ADK (Python), is designed to be your intelligent companion for all things exercise and nutrition.

## 🌟 Overview

The core goal is to provide users with accurate information and actionable advice on their fitness and dietary queries. Leveraging specialized tools and a conversational Streamlit UI, this AI aims to make health and fitness knowledge more accessible and interactive.

## ✨ Features

*   **Food Information Tool**: Get detailed nutritional insights for various food items. 🍎
*   **Exercise Information Tool**: Discover information about different exercises, their benefits, and how to perform them. 🤸‍♂️
*   **Conversational Interface**: Interact with the AI through an intuitive Streamlit chat UI. 💬
*   **Session-Based Memory**: The chatbot remembers the context of your conversation within a session for a more natural interaction flow. 🧠
*   **Google ADK Powered**: Built on the robust Google Agent Development Kit for efficient tool usage and agent orchestration.
*   *(Planned)* SQLite integration for caching and potential future persistent storage.

## 🛠️ Technology Stack

*   **Core Logic & Agent**: Python with Google ADK
*   **LLM Agent**: Google ADK `LlmAgent` (e.g., using a Gemini model)
*   **User Interface**: Streamlit
*   **Package Management**: Poetry
*   **Testing**: Pytest
*   *(Planned)* **Database**: SQLite

## 🚀 Getting Started

Follow these instructions to get the Fitness Diet Advisor AI up and running on your local machine.

### Prerequisites

*   Python (version >=3.9.0, !=3.9.7, <4.0.0 - as defined in `pyproject.toml`)
*   Poetry (for managing dependencies and virtual environment)

### Installation

1.  **Clone the repository (if you haven't already):**
    ```bash
    git clone <your-repository-url>
    cd fitness-diet-advisor-ai
    ```

2.  **Install dependencies using Poetry:**
    This command will create a virtual environment (if one doesn't exist) and install all the necessary packages defined in `pyproject.toml`.
    ```bash
    poetry install
    ```

    *Note: If you encounter any Python version compatibility issues during `poetry install`, ensure your active Python version matches the constraints in `pyproject.toml` (`>=3.9.0, !=3.9.7, <4.0.0`). You can use tools like `pyenv` to manage multiple Python versions.*

## 🏃‍♀️ How to Run

Once the installation is complete, you can run the Streamlit application:

```bash
poetry run streamlit run src/fitness_diet_advisor_ai/main.py
```

This will start the Streamlit development server, and you can access the chatbot in your web browser (usually at `http://localhost:8501`).

## ✅ How to Run Tests

To ensure everything is working as expected, run the unit tests using Pytest:

```bash
poetry run pytest .
```

## 🤝 Contributing

We welcome contributions to make the Fitness Diet Advisor AI even better! If you're interested in contributing, please feel free to:

*   Fork the repository.
*   Create a new branch for your feature or bug fix.
*   Make your changes and ensure all tests pass.
*   Submit a pull request with a clear description of your changes.

(Further details on contribution guidelines, coding standards, and issue tracking will be added as the project evolves.)

---

Happy coding, and let's build a healthier future together! 💪