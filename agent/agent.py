import logging
import os
from dotenv import load_dotenv
from livekit.agents import (
    Agent,
    AgentSession,
    JobContext,
    JobProcess,
    JobRequest,
    WorkerOptions,
    cli,
    llm,
)
from livekit.plugins import deepgram, openai
from typing import Annotated
import requests
import aiohttp

load_dotenv(dotenv_path="../.env")

logger = logging.getLogger("restaurant-agent")
logger.setLevel(logging.INFO)

class RestaurantAssistant(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions=(
                "You are a friendly and helpful restaurant host for 'The Golden Spoon' in Bhopal. "
                "Your goal is to help users book a table. Be warm, concise and conversational. "
                "\n"
                "CONVERSATION FLOW (follow strictly):\n"
                "1. Greet the customer warmly\n"
                "2. Ask for their preferred DATE\n"
                "3. IMMEDIATELY check weather for that date using check_weather tool\n"
                "4. Based on weather, RECOMMEND seating (indoor if cold/rainy, outdoor if nice)\n"
                "5. Ask what TIME they'd like to come\n"
                "6. Ask how many GUESTS\n"
                "7. Ask for NAME for the reservation\n"
                "8. Ask if they have any SPECIAL REQUESTS (dietary restrictions, occasions, etc.)\n"
                "9. Summarize the booking details and ask for confirmation\n"
                "10. Only after user confirms, call create_booking\n"
                "\n"
                "IMPORTANT RULES:\n"
                "- ALWAYS check weather before asking about time - this is MANDATORY\n"
                "- ALWAYS recommend seating based on weather forecast\n"
                "- When calling create_booking: use YYYY-MM-DD for dates, HH:MM for times\n"
                "- For seating_preference parameter: use ONLY 'indoor', 'outdoor', or 'any'\n"
                "- After successful booking, just say the booking is confirmed - do NOT read out the booking ID number\n"
                "- Be natural and conversational, ask one question at a time"
            ),
        )

    @llm.function_tool(description="Check the weather forecast for a specific date to suggest seating options.")
    async def check_weather(
        self,
        date: str,
    ) -> str:
        """
        Check the weather forecast.

        Args:
            date: The date to check weather for (e.g., '2023-10-27')
        """
        logger.info(f"Checking weather for {date}")
        api_key = os.getenv("WEATHER_API_KEY")
        if not api_key:
            return "Weather API key missing."

        location = "Bhopal" 
        url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={location}&dt={date}"

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        data = await response.json()
                        forecast = data['forecast']['forecastday'][0]['day']
                        condition = forecast['condition']['text'].lower()
                        avg_temp_f = forecast['avgtemp_f']
                        return f"The forecast for {date} in {location} is {condition} with an average temperature of {avg_temp_f}°F."
                    else:
                        return f"Weather API error: {response.status}"
        except Exception as e:
            return f"Failed to check weather: {e}"

    @llm.function_tool(description="Create a restaurant booking.")
    async def create_booking(
        self,
        customer_name: str,
        number_of_guests: int,
        booking_date: str,
        booking_time: str,
        special_requests: str = "None",
        seating_preference: str = "any",
    ) -> str:
        """
        Create a restaurant booking.

        Args:
            customer_name: Name of the customer
            number_of_guests: Number of people in the party
            booking_date: Date of the reservation in YYYY-MM-DD format (e.g., 2024-12-25)
            booking_time: Time of the reservation in HH:MM format (e.g., 19:00 for 7 PM)
            special_requests: Any special requests
            seating_preference: Preferred seating. MUST be EXACTLY one of: 'indoor', 'outdoor', or 'any'
        """
        logger.info(f"Creating booking for {customer_name}")
        
        # Sanitize seating_preference - extract just the enum value
        seating_lower = seating_preference.lower()
        if "indoor" in seating_lower:
            seating_preference = "indoor"
        elif "outdoor" in seating_lower:
            seating_preference = "outdoor"
        else:
            seating_preference = "any"
        
        # Try to parse and format the date properly
        try:
            from datetime import datetime
            import re
            
            # Try to extract year if present
            current_year = datetime.now().year
            
            # Handle formats like "5th December", "December 5", "25 December", etc.
            # Simple approach: try to parse common formats
            date_str = booking_date.lower().replace("th", "").replace("st", "").replace("nd", "").replace("rd", "")
            
            # Try parsing with datetime
            for fmt in ["%d %B", "%B %d", "%d %b", "%b %d", "%Y-%m-%d", "%d-%m-%Y"]:
                try:
                    parsed_date = datetime.strptime(date_str.strip(), fmt)
                    # If year not in original format, use current year
                    if fmt in ["%d %B", "%B %d", "%d %b", "%b %d"]:
                        parsed_date = parsed_date.replace(year=current_year)
                    booking_date = parsed_date.strftime("%Y-%m-%d")
                    break
                except:
                    continue
        except Exception as e:
            logger.warning(f"Could not parse date '{booking_date}', using as-is: {e}")
            
        url = "http://localhost:3000/api/bookings"
        payload = {
            "customerName": customer_name,
            "numberOfGuests": number_of_guests,
            "bookingDate": booking_date,
            "bookingTime": booking_time,
            "specialRequests": special_requests,
            "seatingPreference": seating_preference
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 201:
                return "Booking confirmed successfully!"
            else:
                return f"Failed to create booking: {response.text}"
        except Exception as e:
            return f"Error connecting to booking system: {str(e)}"

async def entrypoint(ctx: JobContext):
    logger.info(f"🚀 Entrypoint called for room: {ctx.room.name}")
    
    await ctx.connect()
    logger.info(f"✅ Connected to room: {ctx.room.name}")

    # Configure plugins BEFORE waiting for participant
    logger.info("� Configuring plugins...")
    stt_plugin = deepgram.STT(model="nova-2-general", api_key=os.getenv("DEEPGRAM_KEY"))
    tts_plugin = deepgram.TTS(model="aura-asteria-en", api_key=os.getenv("DEEPGRAM_KEY"))
    
    llm_plugin = openai.LLM(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPEN_ROUTER_KEY"),
        model="meta-llama/llama-3.1-70b-instruct",
    )

    logger.info("🎬 Starting agent session...")
    session = AgentSession(
        stt=stt_plugin,
        llm=llm_plugin,
        tts=tts_plugin,
    )

    await session.start(
        agent=RestaurantAssistant(),
        room=ctx.room,
    )

    logger.info("🤖 Agent session started and listening...")

if __name__ == "__main__":
    cli.run_app(
        WorkerOptions(
            entrypoint_fnc=entrypoint,
        )
    )
