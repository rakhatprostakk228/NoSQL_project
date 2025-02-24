import aiohttp
from ..config import settings

class AtlasApp:
    def __init__(self):
        self.base_url = f"https://realm.mongodb.com/api/client/v2.0/app/{settings.ATLAS_APP_ID}"
        self.headers = {
            "Authorization": f"Bearer {settings.ATLAS_API_KEY}",
            "Content-Type": "application/json"
        }

    async def call_function(self, func_name: str, args: dict):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.base_url}/functions/{func_name}/call",
                json={"arguments": [args]},
                headers=self.headers
            ) as response:
                return await response.json()

atlas_app = AtlasApp()