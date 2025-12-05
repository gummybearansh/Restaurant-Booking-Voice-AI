/**
 * models/Booking.js
 * 
 * This file defines the structure (schema) of a "Booking" in our MongoDB database.
 * Mongoose uses this schema to validate data before saving it.
 */

const mongoose = require('mongoose');

const BookingSchema = new mongoose.Schema({
    // Unique identifier for the booking (optional, MongoDB creates _id automatically, 
    // but having a custom one can be useful for reference)
    bookingId: {
        type: String,
        unique: true
    },

    // The name of the person making the reservation
    customerName: {
        type: String,
        required: [true, 'Customer name is required'],
        trim: true
    },

    // How many people are in the party
    numberOfGuests: {
        type: Number,
        required: [true, 'Number of guests is required'],
        min: [1, 'Must have at least 1 guest']
    },

    // The date of the reservation
    bookingDate: {
        type: Date,
        required: [true, 'Booking date is required']
    },

    // The time of the reservation (e.g., "19:00")
    bookingTime: {
        type: String,
        required: [true, 'Booking time is required']
    },

    // Cuisine preference (e.g., Italian, Chinese)
    cuisinePreference: {
        type: String,
        default: 'Any'
    },

    // Any special requests (e.g., "Birthday", "Vegan")
    specialRequests: {
        type: String,
        default: 'None'
    },

    // Weather info cached at the time of booking (optional, but good for history)
    weatherInfo: {
        type: Object,
        default: {}
    },

    // Where they want to sit (Indoor/Outdoor)
    seatingPreference: {
        type: String,
        enum: ['indoor', 'outdoor', 'any'],
        default: 'any'
    },

    // Status of the booking
    status: {
        type: String,
        enum: ['confirmed', 'pending', 'cancelled'],
        default: 'confirmed'
    },

    // When the booking record was created
    createdAt: {
        type: Date,
        default: Date.now
    }
});

module.exports = mongoose.model('Booking', BookingSchema);
