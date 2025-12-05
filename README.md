# 🍽️ Restaurant Booking Voice Agent

An intelligent AI-powered voice agent for restaurant reservations, built with LiveKit, OpenAI, and Deepgram. Customers can naturally converse with the AI to make table bookings, check weather forecasts, and receive seating recommendations.

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
git clone https://github.com/yourusername/restaurant-booking-voice-agent.git
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

Created by Ansh Tachwani

## 🙏 Acknowledgments

- [LiveKit](https://livekit.io/) - Real-time communication platform
- [Deepgram](https://deepgram.com/) - Voice AI services
- [OpenRouter](https://openrouter.ai/) - LLM API gateway
- [WeatherAPI](https://weatherapi.com/) - Weather data

---

⭐ If you found this project helpful, please consider giving it a star!
