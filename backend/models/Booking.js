const mongoose = require('mongoose');

const BookingSchema = new mongoose.Schema({
    bookingId: {
        type: String,
        unique: true
    },

    customerName: {
        type: String,
        required: [true, 'Customer name is required'],
        trim: true
    },

    numberOfGuests: {
        type: Number,
        required: [true, 'Number of guests is required'],
        min: [1, 'Must have at least 1 guest']
    },

    bookingDate: {
        type: Date,
        required: [true, 'Booking date is required']
    },

    bookingTime: {
        type: String,
        required: [true, 'Booking time is required']
    },

    cuisinePreference: {
        type: String,
        default: 'Any'
    },

    specialRequests: {
        type: String,
        default: 'None'
    },

    weatherInfo: {
        type: Object,
        default: {}
    },

    seatingPreference: {
        type: String,
        enum: ['indoor', 'outdoor', 'any'],
        default: 'any'
    },

    status: {
        type: String,
        enum: ['confirmed', 'pending', 'cancelled'],
        default: 'confirmed'
    },

    createdAt: {
        type: Date,
        default: Date.now
    }
});

module.exports = mongoose.model('Booking', BookingSchema);
