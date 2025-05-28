# Task List for Fitness Diet Advisor AI

## Phase 1: ADK Agent Setup & Core Tool Development

### P1.T1: Setup ADK Project (Task 1 from Planning)
- [ ] Initialize a new Python project using Poetry: `poetry init`
- [ ] Add `google-adk` to `pyproject.toml` and install: `poetry add google-adk`
- [ ] Add `streamlit` to `pyproject.toml` and install: `poetry add streamlit`
- [ ] Add `pytest` for testing: `poetry add pytest --group dev`
- [ ] Create basic project structure (e.g., `src/fitness_diet_advisor_ai`, `tests/`)
- [ ] Create initial `src/fitness_diet_advisor_ai/__init__.py`
- [ ] Create initial `src/fitness_diet_advisor_ai/main.py` (for Streamlit app entry point)
- [ ] Create initial `src/fitness_diet_advisor_ai/agent.py` (for ADK agent logic)
- [ ] Create initial `src/fitness_diet_advisor_ai/tools.py` (for ADK tool definitions)

### P1.T2: Design Data Sources/APIs (Task 2 from Planning)
- [ ] Research and select a nutrition API (e.g., USDA FoodData Central, Open Food Facts API, Edamam). Document choice and base URL/access method.
- [ ] Research and select an exercise API or data source (e.g., WGER API, or compile a local dataset). Document choice and access method.

### P1.T3: Develop Food Information Tool (Task 3 from Planning & M1.1)
- [ ] In `tools.py`, define a Python function `get_nutritional_info(food_item: str) -> dict`.
- [ ] Implement mock data retrieval (e.g., return a hardcoded dict for "apple" and "banana").
    - Example mock response: `{'food': 'apple', 'calories': 95, 'protein': '0.5g', 'carbs': '25g', 'fat': '0.3g'}`
- [ ] Add a detailed docstring to `get_nutritional_info` explaining its purpose, arguments, and return value for ADK.
- [ ] In `tests/test_tools.py`, write a unit test for `get_nutritional_info` using mock data.

### P1.T4: Develop Exercise Information Tool (Task 4 from Planning & M1.2)
- [ ] In `tools.py`, define a Python function `get_exercise_data(exercise_name: str) -> dict`.
- [ ] Implement mock data retrieval (e.g., return hardcoded dict for "push-ups" and "jumping jacks").
    - Example mock response: `{'exercise': 'push-ups', 'category': 'strength', 'calories_burned_30min_avg_person': 300, 'instructions': '...'}`
- [ ] Add a detailed docstring to `get_exercise_data` for ADK.
- [ ] In `tests/test_tools.py`, write a unit test for `get_exercise_data` using mock data.

### P1.T5: Develop Core ADK Agent (Task 5 from Planning & M1.3, M1.4)
- [ ] In `agent.py`, import `LlmAgent` from `google.adk.agents` and the tool functions from `tools.py`.
- [ ] Instantiate `LlmAgent`:
    -   Set `name` (e.g., "FitnessDietAdvisorAgent").
    -   Set `model` (e.g., a Gemini model like 'gemini-1.5-flash-latest' - ensure API key is configured if needed).
    -   Write a comprehensive `instruction` prompt guiding the agent on how to respond, when to use tools, and how to interpret their outputs.
    -   Register `get_nutritional_info` and `get_exercise_data` in the `tools` list.
- [ ] Create a simple test script (e.g., `tests/test_agent_cli.py` or a runnable block in `agent.py`) to interact with the agent.

### P1.T6: Basic Agent Runner & Testing (Task 6 from Planning & M1.3, M1.4)
- [ ] In the test script / `agent.py` runnable block:
    -   Import `Runner` and `InMemorySessionService` from ADK.
    -   Instantiate `InMemorySessionService`.
    -   Instantiate `Runner` with the agent and session service.
    -   Create a function to send a query to the runner and print the response.
    -   Test with a food query (e.g., "calories in an apple"). Verify tool call and mock response.
    -   Test with an exercise query (e.g., "tell me about push-ups"). Verify tool call and mock response.
- [ ] Run `pytest` to ensure all tool tests pass.

## Phase 2: Streamlit UI & ADK Integration

### P2.T1: Develop Streamlit UI (Task 1 from Planning & M2.1, M2.2)
- [ ] In `main.py`:
    -   Import `streamlit` as `st`.
    -   Set up basic page title: `st.title("Fitness Diet Advisor AI")`.
    -   Initialize chat history in `st.session_state` if it doesn't exist (e.g., `st.session_state.messages = []`).
    -   Display existing chat messages by iterating through `st.session_state.messages`.
    -   Create a chat input field: `prompt = st.chat_input("Ask about food or exercise...")`.

### P2.T2: Integrate ADK Agent with UI (Task 2 from Planning & M2.1, M2.2)
- [ ] In `main.py`:
    -   Import the configured ADK `Runner` instance from `agent.py` (or an initialization function that returns it).
    -   If `prompt` (from `st.chat_input`) is received:
        -   Add user message to `st.session_state.messages` and display it.
        -   Call the ADK `Runner` with the user's `prompt` (ensure you handle the async nature if `runner.run_async` is used, Streamlit typically runs in a single thread, might need `asyncio.run()`).
        -   Extract the agent's textual response from the ADK runner's output.
        -   Add agent's response to `st.session_state.messages` and display it.
- [ ] Ensure tool outputs (still mock) are formatted nicely in the Streamlit chat.

### P2.T3: Implement Session Memory with ADK (Task 3 from Planning & M2.3)
- [ ] Verify that ADK `InMemorySessionService` is correctly maintaining context across multiple turns in the Streamlit app.
    -   Each call to the `Runner` should use the same session ID (Streamlit's session can provide this implicitly if `Runner` is initialized per session, or manage explicitly).
- [ ] Test a multi-turn conversation in Streamlit:
    -   User: "Calories in a banana?"
    -   Agent: (Responds with mock banana nutrition)
    -   User: "What about fiber in it?"
    -   Agent: (Agent should ideally use context. If using a simple LLM and mock tools, it might re-call the tool with "fiber in banana" or the LLM might remember the context of "banana" from the previous turn. For ADK, ensure the LLM prompt and agent setup encourage using conversational history, which `InMemorySessionService` helps provide to the model).

### P2.T4: UI/Agent Interaction Testing (Task 4 from Planning)
- [ ] Manually test various queries (food, exercise, mixed, out-of-scope) in the Streamlit UI.
- [ ] Check for clear display of messages and tool outputs.
- [ ] Verify conversational flow and basic memory.

## Phase 3: Tool Enhancement (Live Data), Agent Refinement & Persistence

### P3.T1: Live Data for Tools (Task 1 from Planning & M3.1, M3.2)
- [ ] **Food Tool (`get_nutritional_info` in `tools.py`):**
    - [ ] Choose a Python library for making HTTP requests (e.g., `requests`, `httpx`). Add to `pyproject.toml` (`poetry add requests`).
    - [ ] Implement API call to the selected nutrition API (from P1.T2).
    - [ ] Parse the API response to extract relevant nutritional information.
    - [ ] Implement error handling (e.g., API key errors, food not found, network issues). Return a structured error message or raise a specific exception that the agent can interpret.
    - [ ] Update unit tests in `tests/test_tools.py` to mock the API call (e.g., using `unittest.mock.patch` or `requests-mock`).
- [ ] **Exercise Tool (`get_exercise_data` in `tools.py`):**
    - [ ] If using an API, implement API call similar to the food tool.
    - [ ] If using a local dataset (e.g., CSV/JSON), implement file reading and searching logic (use `pathlib` for paths).
    - [ ] Parse data and implement error handling.
    - [ ] Update unit tests for the exercise tool with live/local data logic, mocking external calls if any.

### P3.T2: ADK Agent Enhancement (Task 2 from Planning & M3.2, M3.3)
- [ ] In `agent.py`, refine the `LlmAgent`'s `instruction` prompt:
    -   Improve guidance on how to handle tool errors (e.g., "If a tool returns an error, inform the user politely and do not try again for that specific item.").
    -   Add instructions for formatting tool outputs clearly for the user.
    -   Consider how to handle ambiguous queries (e.g., "Tell me about apple" - food or company? Prompt the LLM to ask for clarification if needed).
- [ ] (Optional) Explore ADK callbacks (e.g., `before_tool_callback` in agent definition) for tasks like input sanitization/validation before a tool is called, or `after_tool_callback` for response post-processing.

### P3.T3: SQLite Database Integration (Task 3 from Planning & M3.4)
- [ ] Add `SQLAlchemy` to `pyproject.toml`: `poetry add SQLAlchemy`.
- [ ] Design a simple SQLite database schema for caching API responses (e.g., a table for food nutrition, a table for exercise data, with query parameters as keys and response + timestamp).
- [ ] Create a module (e.g., `src/fitness_diet_advisor_ai/database.py`):
    -   Initialize SQLAlchemy engine for SQLite.
    -   Define table models.
    -   Create functions to save data to cache and retrieve from cache.
- [ ] Modify `tools.py` functions (`get_nutritional_info`, `get_exercise_data`):
    -   Before calling an external API, check the cache for valid (non-expired) data.
    -   If data found in cache, return it.
    -   If not in cache or expired, call API, then save the new response to cache.
- [ ] Add unit tests for caching logic, mocking database interactions.

### P3.T4: Comprehensive Testing (Task 4 from Planning)
- [ ] Expand unit tests in `tests/test_tools.py` and `tests/test_agent_cli.py` (or equivalent for agent testing) to cover more edge cases with live data (mocked APIs).
- [ ] Create basic integration tests that involve the Streamlit UI, ADK agent, and live (mocked) tools.
- [ ] Manually test a wider range of conversational scenarios, including error conditions and ambiguous queries, in the Streamlit UI.
- [ ] Run `pytest .` and ensure all tests pass.

## Phase 4: Future Scope - Advanced ADK Features, Deployment & Maintenance

### P4.T1: Explore Advanced ADK Structures (Task from Planning)
- [ ] Research ADK `SequentialAgent`, `ParallelAgent`, and `AgentTool` for wrapping agents as tools.
- [ ] If complex multi-step queries are identified as a need (e.g., "Find high-protein vegan foods and then suggest 3 exercises to complement them"), sketch out how this could be implemented using these advanced ADK structures.
- [ ] (Optional PoC) Implement a small proof-of-concept for a sequential task using these structures.

### P4.T2: Containerization (Task from Planning)
- [ ] Create a `Dockerfile` in the project root.
    -   Use a Python base image.
    -   Set up Poetry environment: install Poetry, copy `pyproject.toml` and `poetry.lock`, run `poetry install --no-dev`.
    -   Copy application code into the container.
    -   Set the `CMD` to run the Streamlit application (e.g., `streamlit run src/fitness_diet_advisor_ai/main.py`).
- [ ] Create a `.dockerignore` file.
- [ ] Build the Docker image locally and test running the container.

### P4.T3: Deployment Strategy (Task from Planning)
- [ ] Research deployment options for Streamlit applications (e.g., Streamlit Community Cloud, Hugging Face Spaces, cloud platforms like GCP App Engine, AWS Elastic Beanstalk, Azure App Service).
- [ ] Document the chosen strategy and initial steps/considerations.

### P4.T4: Implement Comprehensive Logging (Task from Planning)
- [ ] Add `logging` configuration to the application (e.g., in `main.py` or a dedicated `logger_config.py`).
-   Use `logging.getLogger(__name__)` in different modules.
- [ ] Add INFO level logs for key events (e.g., app start, agent query received, tool called, response sent).
- [ ] Add WARNING level logs for recoverable errors (e.g., API retries, data not found but handled).
- [ ] Add ERROR level logs for critical errors.
- [ ] Ensure logs are visible when running locally and consider how they would be accessed in a deployed environment.

### P4.T5: Update README.md (Task from Planning)
- [ ] Add detailed setup instructions (Poetry, Python version, environment variables if any).
- [ ] Add instructions on how to run the application locally (e.g., `poetry run streamlit run ...`).
- [ ] Add instructions on how to run tests (`poetry run pytest .`).
- [ ] (If applicable) Add instructions for building/running the Docker container.
- [ ] Briefly describe the project architecture and key components.

## General Tasks (Throughout Project)
- [ ] Commit changes to Git regularly with descriptive messages.
- [ ] Push changes to the GitHub repository.
- [ ] Maintain code quality (PEP8, Pylint checks if configured).
- [ ] Refactor code as needed to improve clarity and maintainability.