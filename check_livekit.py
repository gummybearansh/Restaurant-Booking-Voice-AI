import os
import asyncio
from livekit import api
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

async def main():
    url = os.getenv("LIVEKIT_URL")
    api_key = os.getenv("LIVEKIT_API_KEY")
    api_secret = os.getenv("LIVEKIT_API_SECRET")

    print(f"Checking LiveKit connection...")
    print(f"URL: {url}")
    print(f"API Key: {api_key[:5]}...")

    lkapi = api.LiveKitAPI(url, api_key, api_secret)
    
    try:
        rooms = await lkapi.room.list_rooms(api.ListRoomsRequest())
        print(f"✅ Successfully connected to LiveKit!")
        print(f"Active Rooms: {len(rooms.rooms)}")
        for room in rooms.rooms:
            print(f" - Room: {room.name}, Participants: {room.num_participants}")
    except Exception as e:
        print(f"❌ Failed to connect: {e}")
    finally:
        await lkapi.aclose()

if __name__ == "__main__":
    asyncio.run(main())
