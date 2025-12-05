import requests
import json

url = "http://localhost:3000/api/bookings"

bookings = [
    {
        "customerName": "Demo User 1",
        "numberOfGuests": 2,
        "bookingDate": "2023-12-25",
        "bookingTime": "19:00",
        "specialRequests": "Window seat",
        "seatingPreference": "indoor"
    },
    {
        "customerName": "Demo User 2",
        "numberOfGuests": 4,
        "bookingDate": "2023-12-31",
        "bookingTime": "20:00",
        "specialRequests": "Vegan options",
        "seatingPreference": "any"
    }
]

for booking in bookings:
    try:
        response = requests.post(url, json=booking)
        print(f"Booking for {booking['customerName']}: Status {response.status_code}")
        print(response.text)
    except Exception as e:
        print(f"Error creating booking for {booking['customerName']}: {e}")
