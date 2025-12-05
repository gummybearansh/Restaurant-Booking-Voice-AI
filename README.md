# 🍽️ AI Restaurant Booking Voice Agent

> A production-ready, intelligent voice agent for restaurant reservations powered by LiveKit, OpenAI, and Deepgram. Customers engage in natural voice conversations to make bookings, receive weather-based seating recommendations, and get instant confirmations.

[![LiveKit](https://img.shields.io/badge/LiveKit-Enabled-blue)](https://livekit.io/)
[![OpenAI](https://img.shields.io/badge/OpenAI-Compatible-green)](https://openrouter.ai/)
[![Deepgram](https://img.shields.io/badge/Deepgram-STT%2FTTS-purple)](https://deepgram.com/)

## 🎬 Demo

Watch the AI voice agent in action:

https://github.com/user-attachments/assets/demo-video.mp4

![Demo Video](Demo%20Video.mp4)

## ✨ Key Features

### 🎙️ **Natural Voice Conversations**
- Real-time voice interaction with sub-second latency
- Advanced speech-to-text powered by Deepgram Nova 2
- Natural text-to-speech with Deepgram Aura
- Seamless conversation flow with interrupt handling

### 🤖 **Intelligent AI Agent**
- Powered by Amazon Nova 2 Lite (completely free tier)
- Context-aware conversation management
- Smart date and time parsing from natural language
- Automatic booking confirmation workflow

### 🌤️ **Smart Weather Integration**
- Real-time weather forecasts for booking dates
- Intelligent seating recommendations:
  - 🏠 Indoor seating for cold/rainy weather
  - ☀️ Outdoor seating for pleasant conditions
- Integrated with WeatherAPI.com

### 💬 **Live Conversation Transcripts**
- Real-time chat-style interface showing full conversation
- User messages displayed with blue bubbles (left-aligned)
- AI responses shown with green bubbles (right-aligned)
- Visual "AI is thinking..." indicator with animated dots
- Auto-scrolling message history

### 📊 **Robust Data Management**
- MongoDB integration for persistent booking storage
- Complete booking history with timestamps
- Searchable and filterable records
- RESTful API for booking operations

### 🎨 **Modern Web Interface**
- Clean, responsive Next.js frontend
- Dark mode design with glassmorphism effects
- Real-time connection status indicators
- Intuitive microphone controls

## 🏗️ Architecture

```
┌─────────────────┐         ┌──────────────────┐         ┌─────────────────┐
│   Next.js       │         │   Node.js        │         │   Python        │
│   Frontend      │◄───────►│   Backend        │◄───────►│   AI Agent      │
│                 │         │                  │         │                 │
│ • Live UI       │  HTTP   │ • REST API       │  LiveKit│ • LLM           │
│ • Transcripts   │         │ • Token Gen      │         │ • STT/TTS       │
│ • Audio Stream  │         │ • MongoDB        │         │ • Tools         │
└─────────────────┘         └──────────────────┘         └─────────────────┘
                                     │                           │
                                     ▼                           ▼
                            ┌─────────────────┐       ┌──────────────────┐
                            │   MongoDB       │       │   LiveKit Cloud  │
                            │   Database      │       │   WebRTC         │
                            └─────────────────┘       └──────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- **Node.js** v18+ 
- **Python** v3.10+
- **MongoDB** (local or Atlas)
- **API Keys** (free tiers available):
  - [OpenRouter](https://openrouter.ai/keys) - LLM access
  - [Deepgram](https://console.deepgram.com/) - Speech services
  - [WeatherAPI](https://weatherapi.com/) - Weather data
  - [LiveKit Cloud](https://cloud.livekit.io/) - Real-time communication

### 1. Clone & Install

```bash
git clone https://github.com/gummybearansh/Restaurant-Booking-Voice-AI.git
cd Restaurant-Booking-Voice-AI
```

### 2. Environment Setup

Create a `.env` file in the project root:

```env
# LiveKit Configuration
LIVEKIT_URL=wss://your-project.livekit.cloud
LIVEKIT_API_KEY=your_api_key
LIVEKIT_API_SECRET=your_api_secret

# AI Services
OPEN_ROUTER_KEY=your_openrouter_api_key
DEEPGRAM_KEY=your_deepgram_api_key
WEATHER_API_KEY=your_weatherapi_key

# Database
MONGO_CONNECTION_STRING=mongodb://localhost:27017/
# Or for MongoDB Atlas:
# MONGO_CONNECTION_STRING=mongodb+srv://user:pass@cluster.mongodb.net/
```

### 3. Install Dependencies

**Backend:**
```bash
cd backend
npm install
```

**Frontend:**
```bash
cd frontend
npm install
```

**AI Agent:**
```bash
cd agent
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Start All Services

Open **3 terminals**:

**Terminal 1 - Backend:**
```bash
cd backend
node server.js
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

**Terminal 3 - AI Agent:**
```bash
cd agent
source venv/bin/activate
python agent.py dev
```

### 5. Access the Application

Open your browser and navigate to:
```
http://localhost:3001
```

Click **"Start Conversation"** and begin speaking!

## 📁 Project Structure

```
restaurant-booking-voice-ai/
├── agent/                      # Python AI agent
│   ├── agent.py               # Main agent with LLM + tools
│   ├── requirements.txt       # Python dependencies
│   └── venv/                  # Virtual environment
│
├── backend/                    # Node.js API server
│   ├── models/
│   │   └── Booking.js         # MongoDB booking schema
│   ├── routes/
│   │   └── bookings.js        # RESTful booking endpoints
│   ├── server.js              # Express server + LiveKit token gen
│   └── package.json
│
├── frontend/                   # Next.js web application
│   ├── app/
│   │   ├── layout.tsx         # Root layout
│   │   ├── page.tsx           # Main UI with live transcripts
│   │   └── globals.css        # Styling
│   └── package.json
│
├── delete_room.py             # Utility to clear ghost LiveKit rooms
├── .env                       # Environment variables (not in git)
└── README.md
```

## 🎯 How It Works

### Conversation Flow

1. **User Connects** → Frontend requests LiveKit token from backend
2. **Agent Joins** → Python agent automatically joins the LiveKit room
3. **Voice Interaction** → User speaks; Deepgram transcribes in real-time
4. **AI Processing** → LLM understands intent and manages conversation
5. **Information Gathering**:
   - Preferred date
   - Weather check → Seating recommendation
   - Time preference
   - Number of guests
   - Guest name
   - Special requests
6. **Confirmation** → Agent summarizes all details
7. **Booking Creation** → Data validated and saved to MongoDB
8. **Completion** → User receives confirmation

### Sample Conversation

```
AI:  Welcome to The Golden Spoon! I'd be happy to help you book a table. 
     What date would you like to visit?

User: This Saturday

AI:  Let me check the weather for Saturday, December 7th...
     The forecast is sunny with 66°F. Perfect weather for outdoor dining! 
     Would you prefer outdoor seating?

User: Yes, outdoor sounds great

AI:  Wonderful! What time would you like to come?

User: 6 PM please

AI:  Perfect, 6 PM. How many guests will be joining you?

User: Three of us

AI:  Great! And what name should I put the reservation under?

User: Harry

AI:  Excellent! Any special requests or dietary restrictions?

User: No, nothing in particular

AI:  Let me confirm: Table for 3 on Saturday, December 7th at 6 PM, 
     outdoor seating, under the name Harry. Is this correct?

User: Yes, perfect

AI:  Wonderful! Your reservation is confirmed. We look forward to seeing 
     you at The Golden Spoon!
```

## 🛠️ Customization

### Change Restaurant Details

Edit `agent/agent.py`:

```python
instructions=(
    "You are a friendly restaurant host for 'YOUR RESTAURANT NAME' in YOUR CITY. "
    # ...
)
```

### Change Weather Location

Edit `agent/agent.py`:

```python
location = "Your City"  # Change from "Bhopal"
```

### Switch LLM Model

Edit `agent/agent.py`:

```python
llm_plugin = openai.LLM(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPEN_ROUTER_KEY"),
    model="your-preferred-model",  # e.g., "meta-llama/llama-3.1-70b-instruct"
)
```

## 🐛 Troubleshooting

### Agent Not Receiving Connections

**Symptom:** Agent registers but entrypoint never called

**Solution:**
```bash
# Clear ghost LiveKit room
python delete_room.py

# Restart agent
cd agent
python agent.py dev
```

### No Voice Output

**Check:**
1. Microphone permissions in browser
2. Deepgram API key is valid
3. Browser supports WebRTC (use Chrome/Edge/Safari)

### Weather API Not Working

**Verify:**
1. `WEATHER_API_KEY` is set in `.env`
2. WeatherAPI.com account is active
3. Check agent logs for detailed error messages

### Database Connection Failed

**Check:**
1. MongoDB is running: `mongosh`
2. Connection string is correct in `.env`
3. Database name matches: `Restaurant-AI`

## 📊 API Reference

### Create Booking
```http
POST /api/bookings
Content-Type: application/json

{
  "customerName": "John Doe",
  "numberOfGuests": 4,
  "bookingDate": "2024-12-25",
  "bookingTime": "19:00",
  "specialRequests": "Birthday celebration",
  "seatingPreference": "indoor"
}
```

### Get All Bookings
```http
GET /api/bookings
```

### Get Booking by ID
```http
GET /api/bookings/:id
```

### Delete Booking
```http
DELETE /api/bookings/:id
```

## 🎨 Features Showcase

### Live Transcripts
- **User messages:** Blue bubbles on the left with user icon
- **AI responses:** Green bubbles on the right with bot icon
- **Thinking indicator:** Animated dots when AI is processing
- **Auto-scroll:** Always shows latest messages

### Weather Intelligence
- Fetches real-time forecast for booking date
- Analyzes conditions (temperature, weather)
- Provides intelligent seating recommendations
- Seamlessly integrated into conversation flow

### Smart Parsing
- Understands natural date formats: "next Friday", "December 25th"
- Converts to proper YYYY-MM-DD format
- Handles time formats: "7 PM" → "19:00"
- Validates seating preferences

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

MIT License - feel free to use this project for your own purposes!

## 🙏 Acknowledgments

- **[LiveKit](https://livekit.io/)** - Real-time communication platform
- **[Deepgram](https://deepgram.com/)** - Speech AI services  
- **[OpenRouter](https://openrouter.ai/)** - LLM API gateway
- **[WeatherAPI](https://weatherapi.com/)** - Weather data provider
- **[Next.js](https://nextjs.org/)** - React framework
- **[MongoDB](https://mongodb.com/)** - Database platform

## 👨‍💻 Author

**Ansh Lachhwani**

---

⭐ If this project helped you, please consider giving it a star on GitHub!


## ✨ Features

- 🎤 **Natural Voice Conversations**: Real-time voice interaction using Deepgram STT/TTS
- 🤖 **Intelligent AI Agent**: Powered by Meta's Llama 3.1 70B via OpenRouter
- 🌤️ **Weather Integration**: Automatic weather checks with seating recommendations
- 📅 **Smart Booking System**: Handles dates, times, party sizes, and special requests
- 💾 **MongoDB Storage**: Persistent booking records with validation
- 🎨 **Modern Web Interface**: Clean, responsive Next.js frontend
- 🔄 **Real-time Communication**: WebRTC-based audio streaming via LiveKit

## 🛠️ Tech Stack

### Frontend
- **Next.js 16** - React framework with Turbopack
- **LiveKit Components React** - Pre-built voice UI components
- **Tailwind CSS** - Utility-first styling

### Backend
- **Node.js + Express** - REST API server
- **MongoDB + Mongoose** - Database and ODM
- **LiveKit Server SDK** - Token generation

### AI Agent (Python)
- **LiveKit Agents SDK** - Agent framework
- **Deepgram** - Speech-to-Text and Text-to-Speech
- **OpenAI SDK** - LLM integration (via OpenRouter)
- **Meta Llama 3.1 70B** - Language model
- **Weather API** - Real-time weather data

## 📋 Prerequisites

- **Node.js** (v18 or higher)
- **Python** (v3.10 or higher)
- **MongoDB** (local or Atlas)
- **LiveKit Cloud** account (free tier available)
- **API Keys**:
  - OpenRouter API key
  - Deepgram API key
  - WeatherAPI key

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/gummybearansh/restaurant-booking-voice-agent.git
cd restaurant-booking-voice-agent
```

### 2. Environment Setup

Create a `.env` file in the project root:

```env
# LiveKit Configuration
LIVEKIT_URL=wss://your-project.livekit.cloud
LIVEKIT_API_KEY=your_api_key
LIVEKIT_API_SECRET=your_api_secret

# AI Services
OPEN_ROUTER_KEY=your_openrouter_api_key
DEEPGRAM_KEY=your_deepgram_api_key
WEATHER_API_KEY=your_weatherapi_key

# Database
MONGO_CONNECTION_STRING=mongodb://localhost:27017/
```

### 3. Backend Setup

```bash
cd backend
npm install
node server.js
```

The backend will start on `http://localhost:3000`

### 4. Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

The frontend will start on `http://localhost:3001`

### 5. Python Agent Setup

```bash
cd agent
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python agent.py dev
```

## 📁 Project Structure

```
restaurant-booking-voice-agent/
├── agent/                      # Python AI agent
│   ├── agent.py               # Main agent logic
│   └── requirements.txt       # Python dependencies
├── backend/                    # Node.js API server
│   ├── models/
│   │   └── Booking.js         # MongoDB schema
│   ├── routes/
│   │   └── bookings.js        # Booking endpoints
│   └── server.js              # Express server
├── frontend/                   # Next.js web app
│   ├── app/
│   │   ├── layout.tsx
│   │   └── page.tsx           # Main voice UI
│   └── package.json
└── .env                       # Environment variables
```

## 🎯 How It Works

1. **User Connects**: Opens the web interface and clicks "Start Conversation"
2. **Agent Joins**: Python agent automatically joins the LiveKit room
3. **Voice Interaction**: User speaks naturally; agent responds with voice
4. **Information Gathering**: Agent collects:
   - Preferred date
   - Weather check & seating recommendation
   - Time preference
   - Number of guests
   - Guest name
   - Special requests
5. **Confirmation**: Agent summarizes details and asks for confirmation
6. **Booking Creation**: Data is validated and saved to MongoDB
7. **Confirmation**: User receives booking confirmation

## 🌟 Key Features Explained

### Weather-Based Recommendations

The agent automatically checks the weather forecast for the booking date and intelligently recommends:
- **Indoor seating** when weather is cold, rainy, or unpleasant
- **Outdoor seating** when conditions are nice
- **Any seating** as a default fallback

### Smart Date & Time Parsing

The agent handles natural language inputs:
- "5th December" → automatically converts to `2024-12-05`
- "9 PM" → converts to `21:00` (24-hour format)
- Validates and formats all data before database storage

### Robust Validation

- Enum validation for seating preferences
- Date format validation
- Guest count validation (minimum 1)
- Required fields enforcement

## 🔧 API Endpoints

### `POST /api/bookings`
Create a new booking

**Request Body:**
```json
{
  "customerName": "John Doe",
  "numberOfGuests": 4,
  "bookingDate": "2024-12-25",
  "bookingTime": "19:00",
  "specialRequests": "Birthday celebration",
  "seatingPreference": "indoor"
}
```

### `GET /api/bookings`
Retrieve all bookings

### `GET /api/bookings/:id`
Get a specific booking

### `DELETE /api/bookings/:id`
Cancel a booking

### `GET /api/token`
Generate LiveKit access token

## 🎨 Customization

### Change Restaurant Name

Edit `agent/agent.py`:
```python
instructions=(
    "You are a friendly and helpful restaurant host for 'Your Restaurant Name' in Your City."
    # ...
)
```

### Change Location for Weather

The weather API is hardcoded to **Bhopal**. To change:

Edit `agent/agent.py`:
```python
location = "Your City"
```

### Modify LLM Model

Edit `agent/agent.py`:
```python
llm_plugin = openai.LLM(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPEN_ROUTER_KEY"),
    model="your-preferred-model",  # Change here
)
```

## 🐛 Troubleshooting

### Agent Not Connecting

1. Ensure all three services are running (backend, frontend, agent)
2. Check LiveKit credentials in `.env`
3. Verify the agent terminal shows: `🚀 Entrypoint called for room: restaurant-booking`

### Database Connection Failed

1. Verify MongoDB is running: `mongosh`
2. Check `MONGO_CONNECTION_STRING` in `.env`
3. Ensure database name is `Restaurant-AI`

### No Audio/Voice

1. Allow microphone permissions in browser
2. Check Deepgram API key is valid
3. Verify browser supports WebRTC (Chrome, Edge, Safari recommended)

### Weather API Not Working

1. Verify `WEATHER_API_KEY` in `.env`
2. Check WeatherAPI.com account is active
3. Free tier has rate limits - ensure not exceeded

## 📝 License

MIT License - feel free to use this project for your own purposes!

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 👤 Author

Created by Ansh Lachhwani

## 🙏 Acknowledgments

- [LiveKit](https://livekit.io/) - Real-time communication platform
- [Deepgram](https://deepgram.com/) - Voice AI services
- [OpenRouter](https://openrouter.ai/) - LLM API gateway
- [WeatherAPI](https://weatherapi.com/) - Weather data

---

⭐ If you found this project helpful, please consider giving it a star!
