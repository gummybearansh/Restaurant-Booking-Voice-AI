/**
 * routes/bookings.js
 * 
 * This file handles all the API endpoints for bookings.
 * It defines what happens when a user (or our AI agent) sends a request to /api/bookings.
 */

const express = require('express');
const router = express.Router();
const mongoose = require('mongoose');
const Booking = require('../models/Booking');

// @route   POST /api/bookings
// @desc    Create a new booking
// @access  Public (for now)
router.post('/', async (req, res) => {
    try {
        console.log('📝 Received booking request:', req.body);

        // Generate a unique booking ID
        const bookingId = 'BOOK-' + Date.now();

        // Ensure seatingPreference has a valid value
        let seatingPreference = req.body.seatingPreference;
        if (!seatingPreference || seatingPreference.trim() === '') {
            seatingPreference = 'any';
        }

        // Create a new booking document
        const booking = new Booking({
            bookingId: bookingId,
            customerName: req.body.customerName,
            numberOfGuests: req.body.numberOfGuests,
            bookingDate: req.body.bookingDate,
            bookingTime: req.body.bookingTime,
            specialRequests: req.body.specialRequests || 'None',
            seatingPreference: seatingPreference
        });

        // Save to database
        const savedBooking = await booking.save();
        console.log('✅ Booking saved successfully:', savedBooking.bookingId);

        // Return the saved booking
        res.status(201).json(savedBooking);
    } catch (error) {
        console.error('❌ Error saving booking:', error);
        res.status(400).json({
            error: 'Failed to create booking',
            details: error.message
        });
    }
});

// @route   GET /api/bookings
// @desc    Get all bookings
// @access  Public
router.get('/', async (req, res) => {
    try {
        const bookings = await Booking.find().sort({ createdAt: -1 }); // Newest first
        res.json(bookings);
    } catch (err) {
        res.status(500).json({ error: 'Failed to fetch bookings' });
    }
});

// @route   GET /api/bookings/:id
// @desc    Get a specific booking by ID
// @access  Public
router.get('/:id', async (req, res) => {
    try {
        const booking = await Booking.findById(req.params.id);
        if (!booking) return res.status(404).json({ error: 'Booking not found' });
        res.json(booking);
    } catch (err) {
        res.status(500).json({ error: 'Server error' });
    }
});

// @route   DELETE /api/bookings/:id
// @desc    Cancel/Delete a booking
// @access  Public
router.delete('/:id', async (req, res) => {
    try {
        const booking = await Booking.findById(req.params.id);
        if (!booking) return res.status(404).json({ error: 'Booking not found' });

        await booking.deleteOne();
        res.json({ message: 'Booking cancelled successfully' });
    } catch (err) {
        res.status(500).json({ error: 'Server error' });
    }
});

module.exports = router;
