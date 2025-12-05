/**
 * server.js
 * 
 * This is the main entry point for our backend application.
 * It sets up the Express server, connects to MongoDB, and defines our API routes.
 */

const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const dotenv = require('dotenv');

// Load environment variables from the parent directory's .env file
// We use path.resolve to look for .env in the root folder
const path = require('path');
dotenv.config({ path: path.resolve(__dirname, '../.env') });

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
// CORS allows our frontend (and other origins) to talk to this API
app.use(cors());
// JSON parser allows us to read the body of POST requests
app.use(express.json());

// MongoDB Connection
// We use the connection string from our .env file
const mongoURI = process.env.MONGO_CONNECTION_STRING;

if (!mongoURI) {
    console.error("❌ Error: MONGO_CONNECTION_STRING is missing in .env file");
    process.exit(1);
}

mongoose.connect(mongoURI, { dbName: 'Restaurant-AI' })
    .then(() => console.log('✅ MongoDB Connected Successfully'))
    .catch(err => console.error('❌ MongoDB Connection Error:', err));

// Basic Route to check if server is running
app.get('/', (req, res) => {
    res.send('Restaurant Booking API is running...');
});

// Import Routes
// We will create this file next. It handles all booking-related logic.
const bookingsRouter = require('./routes/bookings');
const { AccessToken } = require('livekit-server-sdk');

app.use('/api/bookings', bookingsRouter);

app.get('/api/token', async (req, res) => {
    try {
        console.log('📝 Token requested for room: restaurant-booking');
        const roomName = 'restaurant-booking';
        const participantName = 'User-' + Math.floor(Math.random() * 1000);

        const at = new AccessToken(
            process.env.LIVEKIT_API_KEY,
            process.env.LIVEKIT_API_SECRET,
            {
                identity: participantName,
                ttl: '10m',
            }
        );

        at.addGrant({ roomJoin: true, room: roomName });

        const token = await at.toJwt();
        console.log(`✅ Token generated for ${participantName}`);
        res.json({ token, url: process.env.LIVEKIT_URL });
    } catch (error) {
        console.error('❌ Error generating token:', error);
        res.status(500).json({ error: 'Failed to generate token' });
    }
});

// Start the Server
app.listen(PORT, () => {
    console.log(`🚀 Server is running on http://localhost:${PORT}`);
});
