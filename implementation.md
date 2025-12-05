# Implementation Plan & Learning Guide

## 📚 Concepts & Q&A

### Q1: "Since we put the routes in a new folder, does it actually hit `/api/bookings`?"
**Answer**: Yes! Here is how it works:
1.  **In `server.js`**: We wrote `app.use('/api/bookings', bookingsRouter);`. This tells Express: *"Any request that starts with `/api/bookings`, hand it over to the `bookingsRouter`."*
2.  **In `routes/bookings.js`**: We wrote `router.get('/', ...);`. This matches the "root" of *that specific router*.
3.  **Combined**: When you combine the prefix (`/api/bookings`) with the route (`/`), you get the full path: `http://localhost:3000/api/bookings`.
    *   If you added `router.get('/test', ...)` in the bookings file, the URL would be `/api/bookings/test`.

### Q2: "What is `venv` and `source venv/bin/activate`?"
**Answer**:
*   **`venv` (Virtual Environment)**: Think of it as a "sandbox" for your current project.
    *   Without it, if Project A needs `library v1.0` and Project B needs `library v2.0`, they would conflict on your main computer.
    *   With `venv`, Project A gets its own folder with `v1.0`, and Project B gets its own folder with `v2.0`.
*   **`source venv/bin/activate`**: This command "turns on" the sandbox for your current terminal window.
    *   It tells your terminal: *"When I type `python` or `pip`, use the ones inside the `venv` folder, not the global system ones."*

---

## 🚀 Implementation Progress

### Phase 1: Backend API (Node.js) - **[COMPLETED]** ✅
*   **Server**: Running on Port 3000.
*   **Database**: Connected to MongoDB.
*   **Endpoints**: `POST /api/bookings` (Create), `GET /api/bookings` (List).

### Phase 2: Voice Agent (Python) - **[COMPLETED]** ✅
*Goal: Create the intelligent agent that can listen, think, and speak.*

#### 1. Environment Setup
*   [x] Create `agent/` directory.
*   [x] Create `requirements.txt` with dependencies:
    *   `livekit-agents`: The core framework.
    *   `livekit-plugins-openai`: For using LLMs (compatible with OpenRouter).
    *   `livekit-plugins-deepgram`: For Speech-to-Text (STT) and Text-to-Speech (TTS).
    *   `python-dotenv`: To read our `.env` file.
    *   *(Note: `livekit-plugins-silero` was removed due to compatibility issues. The agent runs without explicit VAD.)*
*   [x] Create Virtual Environment (`venv`) and install libraries.

#### 2. The Agent Brain (`agent.py`)
*   [x] Configure the agent to connect to LiveKit.
*   [x] Set up Deepgram for voice (hearing/speaking).
*   [x] Set up OpenRouter (via OpenAI plugin) for intelligence.
*   [x] Define the "System Prompt" (e.g., "You are a helpful restaurant host...").

#### 3. The Agent's Hands (`tools.py`)
*   [x] `check_weather(date)`: Fetch weather to suggest seating.
*   [x] `create_booking(...)`: Send data to our Node.js backend.

### Phase 3: Frontend (Next.js) - **[IN PROGRESS]** 🚧
*Goal: Create the user interface to talk to the agent.*

#### [NEW] [frontend/](file:///Users/gummybearansh/Desktop/Coding Work/Restaurant Booking Voice Agent/frontend)
- **`npx create-next-app`**: Initialize the web app.
- **`npm install livekit-client @livekit/components-react`**: Install LiveKit's React components.
- **`page.tsx`**: We'll build a simple UI with a "Connect" button that launches the `VoiceAssistantControlBar`.
