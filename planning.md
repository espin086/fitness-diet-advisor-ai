# Project Planning: Fitness Diet Advisor AI

## Overall Goal
To create an AI-powered chatbot using the Google ADK (Python) that provides users with information and advice on exercise and nutrition by leveraging specialized tools. The chatbot will feature a conversational UI (Streamlit) and maintain session-based memory.

## Scope
- **In Scope:**
    - Development of a Food Information Tool (Python function) integrated with the ADK Agent.
    - Development of an Exercise Information Tool (Python function) integrated with the ADK Agent.
    - A primary Google ADK `Agent` (e.g., `LlmAgent`) capable of understanding user queries and invoking the appropriate tool.
    - A Streamlit-based user interface for chat interactions.
    - Session-based conversational memory leveraging ADK's `InMemorySessionService` or similar state management.
    - Initial setup for a SQLite database for potential caching or future persistent storage.
    - Unit and basic integration tests for tools and agent interactions.
- **Out of Scope (Initially):**
    - Complex multi-agent workflows (e.g., `SequentialAgent`, `ParallelAgent`) beyond a single primary agent orchestrating tools. We can evolve to this if needed.
    - Advanced personalization beyond session memory.
    - Real-time coaching or tracking.
    - Integration with wearable devices or external fitness apps.
    - Complex meal planning or highly customized workout generation.
    - Production-grade deployment and scaling infrastructure.

## High-Level Direction & Technology Stack
- **Core Logic & Agent Framework:** Python with Google ADK.
    - We will start with a single `LlmAgent` as the primary orchestrator.
    - Food and Exercise information will be provided via custom Python functions registered as `tools` with this agent.
- **Tools:**
    - `get_nutritional_info(food_item: str) -> dict`: Custom Python function to fetch nutritional data.
    - `get_exercise_data(exercise_name: str) -> dict`: Custom Python function to fetch exercise details.
    - These tools will initially use mock data or simple lookups, with plans to integrate with external APIs/databases.
- **UI:** Streamlit.
- **Database (Optional):** SQLite for local storage (e.g., caching API responses).
- **Memory:**
    - Session-based memory managed by Google ADK's `SessionService` (e.g., `InMemorySessionService`).
    - Utilize ADK's state management features (`context.state`, `output_key`) for passing data and maintaining context within a session.
- **Installation:** `pip install google-adk` will be a core dependency.

## Phases and Milestones

### Phase 1: ADK Agent Setup & Core Tool Development
**Goal:** Establish a basic Google ADK Agent and implement the foundational Food and Exercise tools.
**ADK Focus:** Define `Agent`, register custom Python functions as `tools`, basic `Runner` setup.
**Tasks:**
1.  **Setup ADK Project:**
    -   [x] Initialize Python project (Poetry).
    -   [x] Install `google-adk` and other necessary libraries (e.g., `streamlit`).
2.  **Design Data Sources/APIs:** Identify and evaluate APIs or data sources for nutrition (e.g., USDA FoodData Central, Open Food Facts) and exercise (e.g., WGER Workout Manager).
3.  **Develop Food Information Tool (ADK compatible):**
    -   Create a Python function `get_nutritional_info(food_item: str) -> dict`.
    -   Initially, use hardcoded data or a small local CSV/JSON for testing.
    -   Ensure it has a clear docstring for the ADK agent to understand its purpose.
4.  **Develop Exercise Information Tool (ADK compatible):**
    -   Create a Python function `get_exercise_data(exercise_name: str) -> dict`.
    -   Initially, use hardcoded data.
    -   Ensure a clear docstring.
5.  **Develop Core ADK Agent:**
    -   Instantiate a Google ADK `LlmAgent`.
    -   Define its `instruction` to guide its behavior and tool usage.
    -   Register the `get_nutritional_info` and `get_exercise_data` functions as `tools`.
6.  **Basic Agent Runner & Testing:**
    -   Set up a simple ADK `Runner` and `InMemorySessionService`.
    -   Perform command-line tests sending queries to the agent to verify tool invocation and response generation.
    -   Unit tests for individual tool functions.

**Milestones:**
-   **M1.1:** Food Information Tool successfully returns mock nutritional data when called directly.
-   **M1.2:** Exercise Information Tool successfully returns mock exercise data when called directly.
-   **M1.3:** Core ADK Agent can receive a simple query (e.g., "What are the calories in an apple?"), correctly invoke the `get_nutritional_info` tool, and return its (mock) output.
-   **M1.4:** Core ADK Agent can receive an exercise query (e.g., "Tell me about push-ups"), correctly invoke the `get_exercise_data` tool, and return its (mock) output.

### Phase 2: Streamlit UI & ADK Integration
**Goal:** Create a user-facing Streamlit interface and enable conversational interaction with the ADK agent, including session memory.
**ADK Focus:** Integrate `Runner` with Streamlit, manage conversation state using `SessionService` and `context.state`.
**Tasks:**
1.  **Develop Streamlit UI:**
    -   Create a basic chat interface (input field, message display area).
2.  **Integrate ADK Agent with UI:**
    -   When a user submits a query in Streamlit, pass it to the ADK `Runner`.
    -   Display the agent's response (including formatted tool outputs) in the UI.
    -   Manage conversation history display.
3.  **Implement Session Memory with ADK:**
    -   Utilize ADK's `InMemorySessionService` to maintain conversation context across turns within a single session.
    -   Explore using `output_key` or `context.state` within the agent/tools if needed to pass information between turns explicitly.
4.  **UI/Agent Interaction Testing:** Test conversational flows, ensuring the agent uses context from previous turns (within the session).

**Milestones:**
-   **M2.1:** User can type a query into the Streamlit UI, the query is processed by the ADK agent, and a response is displayed.
-   **M2.2:** Responses from the Food and Exercise tools (still mock data) are displayed clearly in the Streamlit UI.
-   **M2.3:** Chatbot demonstrates basic session memory via ADK (e.g., User: "Calories in a banana?", Agent: "[Banana nutrition]", User: "What about fiber?", Agent: "[Fiber content for banana, retrieved from context or re-invoking tool with context]").

### Phase 3: Tool Enhancement (Live Data), Agent Refinement & Persistence
**Goal:** Connect tools to live data sources, improve agent robustness, and implement optional data persistence.
**ADK Focus:** Advanced tool error handling, more sophisticated agent instructions, potential use of `ToolContext` if tools become more complex.
**Tasks:**
1.  **Live Data for Tools:**
    -   Integrate the `get_nutritional_info` tool with a chosen nutrition API/database.
    -   Integrate the `get_exercise_data` tool with a chosen exercise API/database.
    -   Implement robust error handling within tools (API errors, data not found) and ensure these are passed gracefully to the agent.
2.  **ADK Agent Enhancement:**
    -   Refine agent `instruction` for better NLU, handling ambiguous queries, and formatting of tool outputs.
    -   Explore ADK callbacks (e.g., `before_tool_callback`) if needed for input validation or pre-processing before tool calls.
3.  **SQLite Database Integration (If Beneficial):**
    -   Design schema for caching API responses to reduce latency/costs.
    -   Implement database interaction logic within or alongside the tools.
4.  **Comprehensive Testing:**
    -   Expand unit tests for tools with live data.
    -   Integration tests for UI-agent-tool flows with live data.
    -   Manual testing for edge cases and conversational coherence.

**Milestones:**
-   **M3.1:** Food and Exercise tools fetch and return live data from external APIs/databases.
-   **M3.2:** ADK Agent handles API errors from tools gracefully and informs the user.
-   **M3.3:** Agent demonstrates improved understanding and response generation with live data.
-   **M3.4:** (If implemented) SQLite caching improves tool response times for repeated queries.

### Phase 4: Future Scope - Advanced ADK Features, Deployment & Maintenance
**Goal:** Explore advanced ADK capabilities, prepare for deployment, and ensure maintainability.
**ADK Focus:** Potential use of `SequentialAgent` or `ParallelAgent` for more complex tasks, custom `BaseAgent` if highly specialized logic is needed, evaluation tools if available in ADK.
**Tasks:**
-   **Explore Advanced ADK Structures:**
    -   If queries become complex (e.g., "Plan a meal and then tell me exercises to burn those calories"), consider refactoring to use `SequentialAgent` with the current agent and tools perhaps becoming sub-components or `AgentTool` instances.
-   Containerization (Docker with Poetry).
-   Deployment strategy.
-   Implement comprehensive logging (Python logging package).
-   [x] Update `README.md` thoroughly.

**Milestones:**
-   Application packaged in a Docker container.
-   Deployed to a staging/test environment.
-   Logging implemented and functional.