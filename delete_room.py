import os
import asyncio
from livekit import api
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

async def main():
    url = os.getenv("LIVEKIT_URL")
    api_key = os.getenv("LIVEKIT_API_KEY")
    api_secret = os.getenv("LIVEKIT_API_SECRET")

    lkapi = api.LiveKitAPI(url, api_key, api_secret)
    
    room_name = "restaurant-booking"
    try:
        print(f"Deleting room: {room_name}...")
        await lkapi.room.delete_room(api.DeleteRoomRequest(room=room_name))
        print(f"✅ Room deleted successfully.")
    except Exception as e:
        print(f"❌ Failed to delete room (might not exist): {e}")
    finally:
        await lkapi.aclose()

if __name__ == "__main__":
    asyncio.run(main())
