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
    
    try:
        rooms = await lkapi.room.list_rooms(api.ListRoomsRequest())
        for room in rooms.rooms:
            print(f"Room: {room.name}")
            participants = await lkapi.room.list_participants(api.ListParticipantsRequest(room=room.name))
            for p in participants.participants:
                print(f" - Participant: {p.identity} (Kind: {p.kind})")
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        await lkapi.aclose()

if __name__ == "__main__":
    asyncio.run(main())
