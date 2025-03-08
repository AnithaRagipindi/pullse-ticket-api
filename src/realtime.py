from ably import AblyRest
from dotenv import load_dotenv
import os

load_dotenv()

ably = AblyRest(os.getenv("ABLY_API_KEY"))

async def publish_event(channel_name: str, event_name: str, data: dict):
    channel = ably.channels.get(channel_name)
    await channel.publish(event_name, data)  